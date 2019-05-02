import csv
import time
import os

def writehistory(root_path_to_log_file,data):
    '''
    以cvs格式保存，第一个参数为保存到的路径
    文件以当前时间命名
    第二个参数格式如下:
    [ [URL,Status code] ]
    '''
    if not os.path.exists(root_path_to_log_file):
        os.mkdir(root_path_to_log_file)

    filename=time.ctime().replace(":","")+".csv"
    filename=filename.replace(' ','')
    root_path_to_log_file=os.path.join(root_path_to_log_file,filename)
    with open(root_path_to_log_file,'w',newline='') as csv_file:
        logwriter=csv.writer(csv_file,quotechar=',',delimiter='|',quoting=csv.QUOTE_MINIMAL)
        for row in data:
            logwriter.writerow(row)

def readhistory(root_path_to_log_file):
    '''
    从csv中读取记录
    '''
    for _ , _, files in os.walk(root_path_to_log_file):
        for index,file in enumerate(files):
            print(index,file)

    choose=int(input("Choose a log file you want to read: "))
    out=[]
    root_path_to_log_file=os.path.join(root_path_to_log_file,files[choose])
    with open(root_path_to_log_file) as csv_file:
        reader=csv.reader(csv_file,quotechar=',',delimiter='|')
        for row in reader:
            if row!=None:
                out.append(row)
    return out

if __name__ == "__main__":
    log_file_name="./log/"
    sample_log=[["http://debug.com dsa",404],["dasdasda fsda ffsd","Error"]]
    writehistory(log_file_name,sample_log)
    out=readhistory(log_file_name)
    print(out)
    print(out[1])

    