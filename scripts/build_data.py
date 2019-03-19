import gzip
from pathlib import Path
import csv

def build_data(datafile, datadir):
    datadir_pth = Path(datadir)
    if not datadir_pth.exists():
        datadir_pth.mkdir(parents=True)
    train_dir = datadir_pth.joinpath("train")    
    train_dir.mkdir(exist_ok=True)

    fin = gzip.open(datafile, "rt", encoding="UTF-8")    
    batch_size = 1000

    for batch_i, batch_x in enumerate(batch_data(fin, batch_size)):
        train_file_x = train_dir/0/f"wiki_{batch_i:05d}.txt"
        fout = open(train_file_x, "w", encoding="UTF-8", newline='')
        csvwriter = csv.writer(fout)
        for line_x in batch_x:
            csvwriter.writerow([0, line_x.strip()])            
        fout.close()
        if batch_i > 3: break
    
    fin.close()
        
    
def batch_data(fobj, batch_size=100):
    data_str = fobj.readline()
    data = []
    while data_str:
        data.append(data_str)
        if len(data) == batch_size:
            yield data
            data = []
        data_str = fobj.readline()