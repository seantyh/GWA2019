import json
import logging
from . import parse_func as parse
from itertools import chain

class MOE:
    def __init__(self, fpath):
        self.moe_data = {}
        self.load_moe_data(fpath)        
        self.pos_map = {
            "動": "V", "名": "N", "副": "D"
        }
    
    def load_moe_data(self, fpath):
        try:
            with open(fpath, "r", encoding="UTF-8") as fin:
                raw_data = json.load(fin)
            
            # index data
            for data_x in raw_data:
                title = data_x.get("title")
                if not title: continue
                if title.startswith("{"): continue
                self.moe_data[title] = data_x
        except Exception as ex:
            print(ex)

    def query_senses(self, word):                

        moe_entry = self.moe_data.get(word, None)
        if not moe_entry:
            return {}
            
        heteronyms = moe_entry.get("heteronyms", [])
        sense_iter = chain.from_iterable([x.get("definitions", None) for x in heteronyms])
        sense_data = [x for x in sense_iter if x]
        ret = []
        for sense_x in sense_data:
            sense_obj = {
                "pos": self.pos_map.get(sense_x.get("type")),
                "definition": sense_x.get("def", ""),
                "example": sense_x.get("example", []),
                "quote": sense_x.get("quote", [])                
            }
            ret.append(sense_obj)
        return ret

def query_word_pos(word, moe_inst):
    return [query_char_pos(w, moe_inst) for w in word]

def query_char_pos(char, moe_inst):
    moe_senses = moe_inst.query_senses(char)
    pos_counter = {"N": 0, "V": 0}
    pos_freq = {"N": 0, "V": 0}
    first_pos = ""

    logger = logging.getLogger("word_pos_utils")
    logger.setLevel("DEBUG")
    ## iterate over moe_senses
    for sense_x in moe_senses:
        sense_pos = sense_x["pos"]

        ## only accept POS of N/V
        if sense_pos not in ("N", "V"):
            continue        

        ## check if it is a classic sense. ignore the classic sense and continue to next        
        is_classic_sense = parse.is_classic(''.join(sense_x.get("quote", "")))
        
        logger.debug("sense def [%s]: %s", sense_x.get("pos"), sense_x.get("definition", ""))
        logger.debug("quote[is_classic: %s]: %s", is_classic_sense, sense_x.get("quote"))        

        if is_classic_sense:
            continue

        ## set the first_pos if not yet set
        if not first_pos:
            first_pos = sense_pos

        ## retrieve examplar words to calculate word frequency
        examplar_words = parse.get_examplar_words(''.join(sense_x.get("example", "")))
        word_freqs = [parse.query_as4_freq(w) for w in examplar_words]        
        
        logger.debug("examplar_words: %s", examplar_words)
        logger.debug("word_freqs: %s", word_freqs)

        ## store the results: examplar words frequency and increment the POS count
        pos_freq[sense_pos] += sum(word_freqs)
        pos_counter[sense_pos] = pos_counter[sense_pos] + 1

    ## Compare pos_counter to determine POS. If tied, then compare pos_freq
    if pos_counter["N"] == pos_counter["V"]:
        # tie condition, compare pos_freq
        if pos_freq["N"] > pos_freq["V"]:
            return "N"
        elif pos_freq["N"] > pos_freq["V"]:
            return "V"
        elif first_pos:
            return first_pos
        else:
            return None

    elif pos_counter["N"] > pos_counter["V"]:
        return "N"
    else:
        return "V"
        
    
