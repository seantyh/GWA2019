import os
import csv
import time
# pylint:disable=no-name-in-module
from PySide2.QtGui import QStandardItemModel, QStandardItem, QBrush, QColor
from PySide2.QtCore import Qt

class AnmorphItem(QStandardItem):
    def __init__(self, lemma):
        QStandardItem.__init__(self, lemma)
        self.lemma = lemma
        self.pos = ""
        self.unit1 = ""
        self.unit2 = ""
        self.hyper_rule = -99
        self.mero_rule = -99
        self.na_rule = -99
        self.unit1_syn = ""    
        self.unit2_syn = ""
        self.note = ""
        self.status = "pending"

    def __repr__(self):
        return (f"{self.lemma}: [{self.unit1}-{self.unit2}] "
                f"{self.hyper_rule}/{self.mero_rule}/{self.na_rule}")

    def __setattr__(self, name, value):
        self.__dict__[name] = value
        try:
            self.update_status()
        except:
            pass

    def update_status(self):
        unit_checked = self.unit1 and self.unit2
        rule_checked = self.hyper_rule >= -1 and self.mero_rule >= -1
        na_rule = self.na_rule == 1
        valid_state = unit_checked and (na_rule or rule_checked)
        if valid_state:
            self.setData(QBrush(QColor(0xff,0xff,0xaa)), Qt.BackgroundColorRole)
            self.status = "complete"
        else:
            self.setData(QBrush(Qt.transparent), Qt.BackgroundColorRole)
    
    def to_list(self):
        return [
            self.lemma, self.pos, self.unit1, self.unit2, 
            self.hyper_rule, self.mero_rule, self.na_rule, 
            self.unit1_syn, self.unit2_syn,
            self.note
        ]

class AnmorphModel(QStandardItemModel):
    def __init__(self, data_path):    
        super(AnmorphModel, self).__init__()
        self.fpath = data_path
        self.load_data()
    
    def load_data(self):
        with open(self.fpath, "r", encoding="UTF-8") as fin:
            data = fin.readlines()
        for line_x in data:            
            toks = line_x.strip().split(",")    
            item = None        
            if len(toks) == 0:
                continue
            elif len(toks) == 1:
                lemma = toks[0]                
                item = AnmorphItem(lemma)
                item.pos = "Unk"
            elif len(toks) == 2:
                lemma = toks[0]
                pos = toks[1]
                item = AnmorphItem(lemma)
                item.pos = pos
            elif len(toks) == 11:
                if toks[0] == "serial":
                    continue                
                lemma = toks[1]
                item = AnmorphItem(lemma)
                item.pos = toks[2]
                item.unit1 = toks[3]
                item.unit2 = toks[4]
                item.hyper_rule = int(toks[5])
                item.mero_rule = int(toks[6])
                item.na_rule = int(toks[7])
                item.unit1_syn = toks[8]
                item.unit2_syn = toks[9]
                item.note = toks[10]
            else:
                pass

            if item:
                self.appendRow(item)
    
    def save_data(self):
        fout = open(self.fpath, "w", encoding="UTF-8", newline='')
        csvwriter = csv.writer(fout)
        csvwriter.writerow("serial,lemma,pos,unit1,unit2,"
            "hyper_rule,mero_rule,na_rule,"
            "unit1_syn,unit2_syn,note".split(","))
        for item_i in range(self.rowCount()):
            idx = self.index(item_i, 0)            
            item = self.itemFromIndex(idx)            
            csvwriter.writerow([item_i] + item.to_list())
        fout.close()
        print(f"[{time.asctime()}] data saved.")