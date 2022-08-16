import csv
import numpy as np
import glob
 
list_path = glob.glob('./*.csv');

for path in list_path:
    with open(path, mode='r', newline='', encoding='cp932') as f:
        csv_reader = csv.reader(f)
        read_data = [row for row in csv_reader]

    ans_data = read_data
    ans_data = np.char.replace(ans_data, "\r\n", "、")
    ans_data = np.char.replace(ans_data, "\n", "、")
    ans_data = np.char.replace(ans_data, ",", "、")

    with open('./shift_jis.csv', "w", newline="") as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(ans_data)
