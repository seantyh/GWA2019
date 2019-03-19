import gzip
from fastai.text import *

def build_lm(data_path, model_name):    
    with gzip.open(data_path, "rt", encoding="UTF-8") as fin:
        data = fin.readlines()
        n_data = len(data)
    print(f"load {n_data} texts")

    data_lm = TextLMDataBunch.from_tokens("", trn_tok=data, trn_lbls=[0]*n_data, 
                val_tok=[[]], val_lbls=[0])
    
    learn = language_model_learner(data_lm, AWD_LSTM, drop_mult=0.5, pretrained=False)
    learn.fit_one_cycle(1, 1e-2)
    learn.save(model_name)