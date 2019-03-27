import random
from dataclasses import dataclass
from typing import Dict, List
from .cwn_sense_utils import SenseData, SenseExamples, Fstat
from .cwn_sense_utils import make_bert_statistics
from .cwn_sense_utils import compute_statistics
import numpy as np
from scipy.spatial.distance import cdist
import torch

SenseId = str

@dataclass
class PermutationResult:
    lemma: str
    senses: Fstat
    permutation: Fstat
    random: Fstat


def run_simulation(lemma, cwn_inst, sense_embed_obj):
    lsenses = extract_lemma_senses(lemma, cwn_inst, sense_embed_obj)
    perm_senses = permute_sense_examples(lsenses)
    rand_senses = fill_random_sense_examples(lsenses)
    lsenses_stat = compute_statistics(lsenses)
    perm_stat = compute_statistics(perm_senses)
    rand_stat = compute_statistics(rand_senses)
    
    perm_result = PermutationResult(
        lemma=lemma,
        senses=lsenses_stat,
        permutation=perm_stat,
        random=rand_stat)
    return perm_result

def extract_lemma_senses(lemma, cwn_inst, sense_embed_obj)\
    -> SenseData:
    lemmas = cwn_inst.find_lemma(f"^{lemma}$")
    sense_data_dict = {}
    for lemma_x in lemmas:
        senses = lemma_x.senses
        for sense_x in senses:
            sense_data_x = sense_embed_obj\
                .get(sense_x.id, {}).get(sense_x.id)
            if not sense_data_x: continue
            sense_data_dict[sense_x.id] = sense_data_x
    return sense_data_dict

def fill_random_sense_examples(lemma_senses):
    rand_sense_data: SenseData = {}
    for sid, ex_data in lemma_senses.items():
        # clone ex_data to a perm_ex_data
        # leave embeddings field blank
        rand_ex_data = SenseExamples(
                        ex_data.target_map,
                        ex_data.sentences)        
        rand_ex_data.embeddings = torch.randn(ex_data.embeddings.shape)
        rand_sense_data[sid] = rand_ex_data

    return rand_sense_data

def permute_sense_examples(lemma_senses: SenseData):
    perm_sense_data: SenseData = {}
    emb_buf = []
    for _, ex_data in lemma_senses.items():
        embs = ex_data.embeddings
        emb_buf.append(embs)
    emb_list = torch.cat(emb_buf, dim=0)

    perm_idxs = list(range(emb_list.shape[0]))
    random.shuffle(perm_idxs)
    for sid, ex_data in lemma_senses.items():
        # clone ex_data to a perm_ex_data
        # leave embeddings field blank
        perm_ex_data = SenseExamples(
                        ex_data.target_map,
                        ex_data.sentences)

        n_emb = ex_data.embeddings.shape[0]
        pidx = [perm_idxs.pop() for _ in range(n_emb)]
        gidx = torch.LongTensor(pidx).unsqueeze(0).reshape(-1,1)
        perm_emb = emb_list.gather(0, gidx.repeat([1, emb_list.shape[1]]))
        perm_ex_data.embeddings = perm_emb
        perm_sense_data[sid] = perm_ex_data

    return perm_sense_data

def gather_lemma_embedding(lemma_x, cwn_inst, sense_embed_obj):
    sense_data = extract_lemma_senses(lemma_x, cwn_inst, sense_embed_obj)        
    sense_emb = []
    sense_ids = []
    for sense_id, sense_ex_x in sorted(sense_data.items()):
        emb_x = sense_ex_x.embeddings
        emb_Mx = emb_x.mean(0)        
        sense_emb.append(emb_Mx.unsqueeze(0))
        sense_ids.append(sense_id)
    sense_emb = torch.cat(sense_emb, 0).numpy()
    return sense_ids, sense_emb

def link_senses(lemma_x, lemma_y, cwn_inst, sense_embed_obj, n=1):
    syn1_ids, syn1_emb = gather_lemma_embedding(lemma_x, cwn_inst, sense_embed_obj)
    syn2_ids, syn2_emb = gather_lemma_embedding(lemma_y, cwn_inst, sense_embed_obj)
    dist_mat = cdist(syn1_emb, syn2_emb, "euclidean")    
    idx_sort = np.argsort(dist_mat, axis=None)
    ret_list = []
    for arr_idx in idx_sort[:n]:        
        s1_id, s2_id = np.unravel_index(arr_idx, dist_mat.shape)
        s1 = cwn_inst.from_sense_id(syn1_ids[s1_id])
        s2 = cwn_inst.from_sense_id(syn2_ids[s2_id])
        ret_list.append(((s1, s2), dist_mat[s1_id, s2_id]))
    return ret_list
