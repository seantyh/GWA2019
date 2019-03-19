import gzip
from fastai.text import *

DATA_PATH = "data/zhwiki-20190301.sample.txt.gz"
with gzip.open(DATA_PATH, "rt", encoding="UTF-8") as fin:
    data = fin.readlines()
    n_data = len(data)

data_lm = TextLMDataBunch.from_tokens("", trn_tok=data, trn_lbls=[0]*n_data, 
            val_tok=[[]], val_lbls=[0])
learn = language_model_learner(data_lm, AWD_LSTM, drop_mult=0.5)
learn.fit_one_cycle(1, 1e-2)
learn.save("wiki_sample_model")