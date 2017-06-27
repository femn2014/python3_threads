import queue, time, threading, datetime

#多个线程做同一件事
class Job:
    def __init__(self, name):
        self.name = name

    def do(self):
        time.sleep(2)
        print("\t[Info] Job({0}) is done!".format(self.name))


que = queue.Queue()#FIFO即First in First Out,先进先出 a[len(a):1]=[queue] 加在后面的
# lifoqueue = queue.LifoQueue()#LIFO即Last in First Out,后进先出 a[0:0]=[queue] 加在最前面的
for i in range(20):
    # 保存要去工作的信息 在queue中
    que.put(Job(str(i + 1)))#调用队列对象的put()方法在队尾插入一个项目。put()有两个参数，第一个item为必需的，为插入项目的值；第二个block为可选参数，默认为1
# 1。如果队列当前满且block为1，put()方法就使调用线程暂停,直到空出一个数据单元。如果block为0，put方法将引发Queue.Full异常 http://xufive.blog.163.com/blog/static/1723261682012211104543905/
#http://www.cnblogs.com/itogo/p/5635629.html
print("\t[Info] Queue size={0}...".format(que.qsize()))#返回队列的大小
#


#######################################
def doJob(*args):
    queue = args[0]
    while queue.qsize() > 0:
        job = queue.get()
        #调用队列对象的get()方法从队头删除并返回一个项目。可选参数为block，默认为True。如果队列为空且block为True，get()就使调用线程暂停，直至有项目可用。如果队列为空且block为False，队列将引发Queue.Empty异常
        job.do()
        # Open three threads
thd1 = threading.Thread(target=doJob, name='Thd1', args=(que,))
thd2 = threading.Thread(target=doJob, name='Thd2', args=(que,))
thd3 = threading.Thread(target=doJob, name='Thd3', args=(que,))
thd4 = threading.Thread(target=doJob, name='Thd3', args=(que,))
thd5 = threading.Thread(target=doJob, name='Thd3', args=(que,))

# # Start activity to digest queue.
st = datetime.datetime.now()
thd1.start()
thd2.start()
thd3.start()
thd4.start()
thd1.join() #在子线程完成运行之前，这个子线程的父线程将一直被阻塞.join() 实际上意味着等到队列为空，再执行别的操作
#這會讓呼叫 join() 方法的線程被 blocked, 一直到被呼叫 join() 的線程結束為止
#不会再进行下面的线程了
thd5.start()
#首先當 Thread 類別被實例化, 你可以呼叫物件上面的方法 start() 來啟動該線程, 事實上該方法會再呼叫方法 run() (Method representing the thread’s activity.). 一旦線程啟動, 它的狀態會變成 "alive" ;
# 當執行完畢 run() 後狀態便不在是 "alive". 你可以使用方法 is_alive() 來檢視該線程是否停留在 "alive" 狀態

# Wait for all threads to terminate.
while thd1.is_alive() or thd2.is_alive() or thd3.is_alive() or thd4.is_alive() or thd5.is_alive():
    time.sleep(1)
################## ######################




#需要40秒
# while que.qsize() > 0:
#     job = que.get()
#     job.do()
#需要40秒


td = datetime.datetime.now() - st
print("\t[Info] Spending time={0}!".format(td))



#q.qsize() 返回队列的大小
# q.empty() 如果队列为空，返回True,反之False
# q.full() 如果队列满了，返回True,反之False
# q.full 与 maxsize 大小对应
# q.get([block[, timeout]]) 获取队列，timeout等待时间
# q.get_nowait() 相当q.get(False)
# 非阻塞 q.put(item) 写入队列，timeout等待时间
# q.put_nowait(item) 相当q.put(item, False)
# q.task_done() 在完成一项工作之后，q.task_done() 函数向任务已经完成的队列发送一个信号
# q.join() 实际上意味着等到队列为空，再执行别的操作
