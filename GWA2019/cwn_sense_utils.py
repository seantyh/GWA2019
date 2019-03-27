import re
from dataclasses import dataclass
from typing import List, Dict, Tuple
from flair.embeddings import Sentence
from scipy.stats import f
from scipy.spatial.distance import cdist
import numpy as np
import torch
CwnSenseId = str
Example = str
SentenceIndex = int
TargetLocation = int
TargetLocList = List[TargetLocation]
SentenceInfo = Tuple[int, TargetLocList]
SenseData = Dict[CwnSenseId, "SenseExamples"]

@dataclass
class Fstat:
    stat: float
    df1: float
    df2: float
    pval: float
    
    def __repr__(self):
        return "<Fstat: F({df1}, {df2}) = {stat:.2f}, p = {pval:0.4f}>".format(
            **self.__dict__
        )

@dataclass
class SenseExamples:
    target_map: Dict[SentenceIndex, List[TargetLocation]]
    sentences: List[Sentence]
    embeddings: torch.FloatTensor = None  # pylint: disable=no-member    

def report_examples(ex_dict: Dict[CwnSenseId, List[Example]]):
    n_sense = len(ex_dict)
    n_examples = sum(len(x) for x in ex_dict.values())
    print(f"gather {n_examples} examples from {n_sense} senses")

def normalize_example(cwn_example) -> Tuple[TargetLocList, Sentence]:
    target = re.search(r"<(.+?)>", cwn_example)
    if not target:
        print("WARNING: target not found in, ", cwn_example)            
        return (None, cwn_example)
    ex_norm = cwn_example.replace("<", " ").replace(">", " ")
    ex_sent = Sentence(ex_norm)            
    targ_locs = [xi for xi, x in enumerate(ex_sent.tokens) 
                if x.text == target.group(1)]
    return (targ_locs, ex_sent)

def compute_sense_data(
        ex_dict: Dict[CwnSenseId, List[Example]],
        bert_inst: "BertEmbeddings",
        debug_random_embedding=False) \
        -> SenseData: 
    
    sense_data = {}
    for sense_id, ex_list in ex_dict.items():        
        targ_map = {}
        sent_list = []
        if not ex_list:
            continue
        for ex_x in ex_list:
            if not ex_x:
                continue
            targ_locs, ex_sent = normalize_example(ex_x)            
            if not targ_locs:                
                print("WARNING: cannot locate target locations: ", ex_x)
                continue

            sent_idx = len(sent_list)            
            targ_map[sent_idx] = targ_locs
            sent_list.append(ex_sent)
        sense_example = SenseExamples(targ_map, sent_list)
        if debug_random_embedding:
            # print("WARNING: debug flag is on, use random embedding")
            sense_embed = random_embed(sense_example)
        else:
            sense_embed = bert_embed(bert_inst, sense_example)
        
        sense_example.embeddings = sense_embed
        sense_data[sense_id] = sense_example
    return sense_data

def random_embed(sense_examples, ndim=3072):
    sent_list = sense_examples.sentences                    
    embed = torch.randn(len(sent_list), ndim)  #pylint: disable=no-member
    return embed

# pylint: disable=no-member
def bert_embed(bert_inst: "BertEmbeddings",
        sense_examples: SenseExamples) \
        -> torch.FloatTensor:
    sent_list = sense_examples.sentences    
    targ_map = sense_examples.target_map
    bert_inst.embed(sent_list)
    embeddings = []
    for sent_idx, sent_x in enumerate(sent_list):
        targ_idx = targ_map[sent_idx] 
        targ_emb = sent_x[targ_idx[0]].embedding
        embeddings.append(targ_emb.unsqueeze(0))
    if embeddings:
        embed = torch.cat(embeddings)
    else:
        raise Exception("No valid embeddings from examples")
    return embed

def compute_statistics(sense_data: SenseData):
    emb_Ms = []
    emb_SS = []  # List[tensor], length of elements might not be of the same length    
    for _, sense_ex_x in sense_data.items():
        emb_x = sense_ex_x.embeddings
        emb_Mx = emb_x.mean(0)
        emb_Ms.append(emb_Mx.unsqueeze(0))
        emb_SSx = ((emb_x-emb_Mx)**2).sum(1)
        emb_SS.append(emb_SSx)
    emb_Ms = torch.cat(emb_Ms, 0)

    ## compute sum of squares
    SSt_x = ((emb_Ms - emb_Ms.mean(0))**2).sum(1).numpy()
    n_x = np.array([len(x) for x in emb_SS])
    SST = (SSt_x * n_x).sum()
    SSE = np.array([x.numpy().sum() for x in emb_SS]).sum()

    ## compute F-statistics    
    k = len(emb_SS)
    N = n_x.sum()
    if k == 1:
        return Fstat(stat=np.nan, df1=k-1, df2=N-k, pval=np.nan)
    MST = SST / (k-1)
    MSE = SSE / (N-k)
    df1 = k-1
    df2 = N-k
    F = MST/MSE    
    
    probF = 1-f.cdf(F, df1, df2)        
    fstat = Fstat(stat=F, df1=df1, df2=df2, pval=probF)
    return fstat

def find_examples(senses):
    return {sense_x.id: sense_x.all_examples() 
            for sense_x in senses if sense_x.all_examples()}

def make_bert_statistics(lemma, cwn_inst, bert_inst, debug=False):
    senses = cwn_inst.find_senses(f"^{lemma}$")
    examples = find_examples(senses)  
    if not examples:
        print("Cannot find examples")
        return None
    sense_data = compute_sense_data(examples, bert_inst, debug_random_embedding=debug)    
    stats = compute_statistics(sense_data)
    return stats

def compute_sense_embedding(lemma, cwn_inst, bert_inst):
    senses = cwn_inst.find_senses(f"^{lemma}$")
    examples = find_examples(senses) 
    sense_data = compute_sense_data(examples, bert_inst)              
    sense_emb = []
    sense_ids = []
    for sense_id, sense_ex_x in sorted(sense_data.items()):
        emb_x = sense_ex_x.embeddings
        emb_Mx = emb_x.mean(0)        
        sense_emb.append(emb_Mx.unsqueeze(0))
        sense_ids.append(sense_id)
    sense_emb = torch.cat(sense_emb, 0).numpy()
    return sense_ids, sense_emb

def connect_lemma(lemma_x, lemma_y, cwn_inst, bert_inst, n=1):
    syn1_ids, syn1_emb = compute_sense_embedding(lemma_x, cwn_inst, bert_inst)
    syn2_ids, syn2_emb = compute_sense_embedding(lemma_y, cwn_inst, bert_inst)
    dist_mat = cdist(syn1_emb, syn2_emb, "euclidean")    
    idx_sort = np.argsort(dist_mat, axis=None)
    ret_list = []
    for arr_idx in idx_sort[:n]:        
        s1_id, s2_id = np.unravel_index(arr_idx, dist_mat.shape)
        s1 = cwn_inst.from_sense_id(syn1_ids[s1_id])
        s2 = cwn_inst.from_sense_id(syn2_ids[s2_id])
        ret_list.append(((s1, s2), dist_mat[s1_id, s2_id]))
    return ret_list



