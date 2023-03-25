import os
import csv

path_decide = input ("which path you want...") #輸入要走的路徑

if path_decide == "1":# 選擇第一條路徑
  # 開啟 CSV 檔案 path1
  with open('path1.csv', newline='') as path1_file:# 讀取 CSV 檔案內容
    rows = csv.reader(path1_file) #以rows存取每一行的內容

    path = open('path_decide.csv','w', newline='')#開啟path_decide檔案，把我們選擇的路徑內容存入最終決定路徑
    writer =csv.writer(path)#創建一個寫入器，負責寫入檔案
    for row in rows: #將路徑一行一行的存入
      print(row)
      writer.writerow(row)

elif path_decide == "2": # 選擇第二條路徑
  with open('path2.csv', newline='') as path2_file:# 讀取 CSV 檔案內容
    rows = csv.reader(path2_file) #以rows存取每一行的內容

    path = open('path_decide.csv','w', newline='') #開啟path_decide檔案，把我們選擇的路徑內容存入最終決定路徑
    writer =csv.writer(path) #創建一個寫入器，負責寫入檔案
    for row in rows: #將路徑一行一行的存入
      print(row)
      writer.writerow(row)

else: #輸入無效的路徑
  print("invalid")
  with open('path_stop.csv', newline='') as stop_file:# 讀取 CSV 檔案內容
    rows = csv.reader(stop_file) #以rows存取每一行的內容

    path = open('path_decide.csv','w', newline='')#開啟path_decide檔案，把我們選擇的路徑內容存入最終決定路徑
    writer =csv.writer(path)#創建一個寫入器，負責寫入檔案
    for row in rows: #將路徑一行一行的存入
      print(row)
      writer.writerow(row)
