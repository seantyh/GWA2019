import re
import unicodedata
import opencc

class Normalizer:
    def __init__(self):
        self.cc = opencc.OpenCC("s2t")

    def normalize(self, x):   
        x = re.sub(r"'''?", "", x)
        x = re.sub(r"==+", "", x)
        x = re.sub(r"\(.*\)", "", x)
        x = re.sub(r"\-\{.*\}\-", "", x)
        x = re.sub(r"《》", "", x)
        x = re.sub(r"link=\w+\s", " ", x)
        x = re.sub(r"File:.+\|", " ", x)
        x = re.sub(r"[a-zA-Z!-~0-9—\s]+", "", x)
        x = re.sub(r"\s+", " ", x)
        x = re.sub(r"（[^\u4E00-\u9FFF]*）", "", x) 
                
        norm_x = self.cc.convert(x)    
        # tokens = re.findall("[\u4E00-\u9FFF\uF900-\uFAFF\uFF00-\uFFEF]", x)
        return norm_x
    