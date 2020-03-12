import csv,os

for csv_file in os.listdir("."):
    # csvファイル出ない場合スキップする
    if not csv_file.endswith(".csv"):
        continue
    
    
    csv_rows = []
    csv_file_obj = open(csv_file)
    csv_reader = csv.reader(csv_file_obj)
    # csvファイルの行を読み出す
    for row in csv_reader:
        csv_rows.append(row)
    csv_file_obj.close()
    # csvファイル名のtsvファイルに書き込む
    tsv_file_name = os.path.splitext(csv_file)
    tsv_file_name = tsv_file_name[0] + ".tsv"
    tsv_file = open(tsv_file_name,"w",newline="")
    tsv_writer = csv.writer(tsv_file,delimiter="\t",lineterminator="\n")
    for row in csv_rows:
        tsv_writer.writerow(row)
        
    tsv_file.close()





