import json
import gzip
from GWA2019 import utils
from multiprocessing import Pool
import time
import os


def normalize_sample(infile, n):
    outfile = infile.replace(".json.gz", ".sample.txt.gz")
    fin = gzip.open(infile)
    fout = gzip.open(outfile, "wt", encoding="UTF-8")    
    norm = utils.Normalizer()
    for _ in range(n):
        data_str = fin.readline()
        data_obj = json.loads(data_str)
        section_texts = "".join(x.strip() for x in data_obj["section_texts"])
        norm_text = norm.normalize(section_texts)
        fout.write(norm_text)
        fout.write("\n")
    fin.close()
    fout.close()

def normalize(infile):    
    outfile = infile.replace(".json.gz", ".txt.gz")
    fin = gzip.open(infile)
    fout = gzip.open(outfile, "wt", encoding="UTF-8")    
    
    counter = 0                
    batch_size = 50        

    for batch_x in batch_data(fin, batch_size=batch_size):        
        with Pool(6) as p:            
            norm_text_list = p.map(normalize_worker, batch_x)
        for norm_text in norm_text_list:
            if not norm_text: continue
            fout.write(norm_text)
            fout.write("\n")
        counter += batch_size
        
        if counter % 10000 == 0:
            print(f"[{time.asctime()}] Processed: {counter}")  
            
    fin.close()
    fout.close()

def batch_data(fobj, batch_size=100):
    data_str = fobj.readline()    
    data = []
    while data_str:
        data.append(data_str)
        if len(data) == batch_size:
            yield data
            data = []
        data_str = fobj.readline()

norm_inst = utils.Normalizer()
def normalize_worker(json_str):        
    try:
        data_obj = json.loads(json_str)
        section_texts = "".join(x.strip() for x in data_obj["section_texts"])
        norm_text = norm_inst.normalize(section_texts)
    except Exception as ex:
        print("ERROR: ", ex)
        norm_text = ""
    return norm_text