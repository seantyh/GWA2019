import os
# pylint:disable=no-name-in-module
from PySide2.QtGui import QStandardItemModel, QStandardItem

class AnmorphItem(QStandardItem):
    def __init__(self, lemma):
        QStandardItem.__init__(self, lemma)
        self.unit1 = ""
        self.unit2 = ""
        self.hyper_rule = -1
        self.mero_rule = -1
        self.na_rule = -1
        self.unit1_syn = ""
        self.unit2_syn = ""

class AnmorphModel(QStandardItemModel):
    def __init__(self):    
        super(AnmorphModel, self).__init__()
        self.load_data("data/word_list.csv")
    
    def load_data(self, fpath):
        with open(fpath, "r", encoding="UTF-8") as fin:
            data = fin.readlines()
        for line_x in data:
            toks = line_x.strip().split(",")
            if len(toks) == 0:
                continue
            elif len(toks) == 1:
                lemma = toks[0]
            elif len(toks) == 8:
                lemma = toks[0]
                unit1 = toks[1]
                unit2 = toks[2]
                hyper_rule = int(toks[3])
                mero_rule = int(toks[4])
                na_rule = int(toks[5])
                unit1_syn = toks[6]
                unit2_syn = toks[7]
            else:
                pass
            self.appendRow(AnmorphItem(lemma))

