import csv,os,openpyxl

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
    # csvファイル名のxlsxファイルに書き込む
    # excelWorkbookを開く
    wb = openpyxl.Workbook()
    sheet = wb.worksheets[0]
    
    wb_file_name = os.path.splitext(csv_file)
    wb_file_name = wb_file_name[0] + ".xlsx"

    # 行ごとに取り出す
    for row in csv_rows:
        sheet.append(row)
   
    wb.save(wb_file_name)
