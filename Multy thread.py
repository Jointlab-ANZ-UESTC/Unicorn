import _thread as thread
from time import sleep,ctime
import requests

__testlink=["http://github.com/",
"http://www.baidu.com/",
"http://www.bilibili.com/",
"http://dasd.donit.com/",
"http://www.baidu.com/fdsfsdfsdfsdfas/",
"http://www.baidu.com/404",
"http://www.baidu.com/132123132123131331232310",
"http://www.bilibili.com/4544545460",
"http://www.github.com/dsadasd",
"http://www.github.com/45444444dsdasdasdAAA",
"http://192.168.1.111:8080",
"http://192.168.1.1"
]

def pause(sleeptime,times,lock):
    '''Use to test if MultyThread funciton works well'''
    print("No. {N} start at {TIME}".format(N=times,TIME=ctime()))
    sleep(sleeptime)
    print("No. {N} end at {TIME}".format(N=times,TIME=ctime()))
    lock.release()

def connect(url,lock,feedback):
    '''Use to test if MultyThread funciton works well'''
    report="[{statuscode}] {link}"
    try:
        r=requests.get(url)
        report=report.format(statuscode=r.status_code,link=url)
    except Exception:
        report=report.format(statuscode='Error',link=url)
    
#    print(report)
    feedback.append(report)
    lock.release()



def MultyThread(ConnectCheckFunction,Linklist):
    '''1.You need to give a function: which will be run by multy thread
    It will recieve a single url, lock ,and responce (which will be add to a list) you want to get 
    2.An parameter list is needed: to give information to that function'''

    locks=[]
    for i in range(len(Linklist)):
        lock=thread.allocate_lock()
        lock.acquire()
        locks.append(lock)
#    print("Start at {TIME}".format(TIME=ctime()))
    responce=[]
    for link,lock in zip(Linklist,locks):
        thread.start_new_thread(ConnectCheckFunction,[link,lock,responce])

    for lock in locks:
        while(lock.locked()):
            pass
#    print("End at {TIME}".format(TIME=ctime()))
    return responce



if __name__=='__main__':
    infolist=MultyThread(connect,__testlink)
    for info in infolist:
        print(info)