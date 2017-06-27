import queue
import threading
from datetime import datetime

SHARE_Q = queue.Queue()  # 构造一个不限制大小的的队列
_WORKER_THREAD_NUM = 4  # 设置线程的个数

def worker():
    global SHARE_Q
    while not SHARE_Q.empty():
        one_dict = SHARE_Q.get()  # 获得任务
        print(one_dict)
        SHARE_Q.task_done()
def main():
    a= datetime.now()
    threads = []
    global SHARE_Q

    l =[1,2,3,4,5,6,7,8,9,10]
    for i in l:
        SHARE_Q.put(i)
    for i in range(_WORKER_THREAD_NUM):
        thr = threading.Thread(target=worker)# 必须要有 target去指定函数
        thr.start()
        threads.append(thr)
    for thread in threads:
        thread.join()
    SHARE_Q.join()
    print(datetime.now() -a)#0:00:00.376745
    print('success')

if __name__ == '__main__':
    main()
