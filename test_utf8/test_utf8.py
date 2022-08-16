from csv import reader,writer
from numpy import char
from glob import glob
import chardet

list_path = glob('./*.csv');

for path in list_path:
    
    with open(path, 'rb') as f:
    c = f.read()
    result = chardet.detect(c)
    
    if result['encoding'] == 'SHIFT_JIS':
        
        with open(path, mode='r', newline='', encoding='cp932') as f:
            csv_reader = reader(f)
            read_data = [row for row in csv_reader]

        ans_data = read_data
        ans_data = char.replace(ans_data, "\r\n", "、")
        ans_data = char.replace(ans_data, "\n", "、")
        ans_data = char.replace(ans_data, ",", "、")
        
        filename = path.replase('.csv','')
        filename = filename + '_置換済み.csv'

        with open(filename, "w", newline="") as f:
            writer = writer(f, lineterminator='\n')
            writer.writerows(ans_data)
    
    if result['encoding'] == 'UTF-8':

        with open(path, mode='r', newline='', encoding='utf_8') as f:
            csv_reader = reader(f)
            read_data = [row for row in csv_reader]

        ans_data = read_data
        ans_data = char.replace(ans_data, "\r\n", "、")
        ans_data = char.replace(ans_data, "\n", "、")
        ans_data = char.replace(ans_data, ",", "/")

        with open(filename, "w", newline="", encoding='utf_8') as f:
            writer = writer(f, lineterminator='\n')
            writer.writerows(ans_data)

