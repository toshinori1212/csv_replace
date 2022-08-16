from csv import reader,writer
from numpy import char
from glob import glob
import chardet

list_path = glob('./*.csv')

for path in list_path:
    
    with open(path, 'rb') as f:
        c = f.read()
        result = chardet.detect(c)
        f.close()

    if result['encoding'] == 'CP932':
        
        with open(path, mode='r', newline='', encoding='CP932') as f:
            csv_reader = reader(f)
            read_data = [row for row in csv_reader]
            f.close()

        ans_data = read_data
        ans_data = char.replace(ans_data, "\r\n", "、")
        ans_data = char.replace(ans_data, "\n", "、")
        ans_data = char.replace(ans_data, ",", "、")
        
        filename = path.replace('.csv','')
        filename = filename + '_置換済み.csv'

        with open(filename, "w", newline="") as f:
            writer1 = writer(f, lineterminator='\n')
            writer1.writerows(ans_data)
            f.close()
    
    if result['encoding'] == 'SHIFT_JIS':
        
        with open(path, mode='r', newline='', encoding='SHIFT_JIS') as f:
            csv_reader = reader(f)
            read_data = [row for row in csv_reader]
            f.close()

        ans_data = read_data
        ans_data = char.replace(ans_data, "\r\n", "、")
        ans_data = char.replace(ans_data, "\n", "、")
        ans_data = char.replace(ans_data, ",", "、")
        
        filename = path.replace('.csv','')
        filename = filename + '_置換済み.csv'

        with open(filename, "w", newline="") as f:
            writer2 = writer(f, lineterminator='\n')
            writer2.writerows(ans_data)
            f.close()
            
    if result['encoding'] == 'utf-8':

        with open(path, mode='r', newline='', encoding='utf_8') as f:
            csv_reader = reader(f)
            read_data = [row for row in csv_reader]
            f.close()

        ans_data = read_data
        ans_data = char.replace(ans_data, "\r\n", "、")
        ans_data = char.replace(ans_data, "\n", "、")
        ans_data = char.replace(ans_data, ",", "/")

        filename = path.replace('.csv','')
        filename = filename + '_置換済み.csv'

        with open(filename, "w", newline="", encoding='utf_8') as f:
            writer3 = writer(f, lineterminator='\n')
            writer3.writerows(ans_data)
            f.close()
