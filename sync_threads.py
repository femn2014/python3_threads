import threading
from datetime import datetime
from time import ctime, sleep, time
#TODO 多线程：当要完成一项工作或多项工作时(但还是在一个主线程中)，单线程就好比一个工人，而多线程就是招了多个工人一起干活，效率当然快了！但管理就费劲了(死锁，竟争)，允许单个任务分成不同的部分运行
#TODO queue可以控制工人先做那(些)项工作，后做哪个(些). 或将要去工作的信息 保存在queue中

#TODO 线程同步,不轮换执行 处理多个任务，直到一个线程全部结束之后，才能进一个等待中的线程
#http://www.runoob.com/python/python-multithreading.html
import _thread

exitFlag = 0

class myThread (threading.Thread):   #继承父类threading.Thread
    def __init__(self,  name, delay):
        threading.Thread.__init__(self)
        # self.threadID = threadID
        self.name = name
        self.delay = delay
    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print( "Starting " + self.name)
        # 线程同步(为了确保数据的完整没有被其它的线程修改，必须要得锁和解锁，所以也导致了要一个线程全部结束之后，才能执行下一个的线程)
        # 获得锁，成功获得锁定后返回True
        # 可选的timeout参数不填时将一直阻塞直到获得锁定
        # 否则超时后将返回False
        # threadLock.acquire()  # 线程同步
        print_time(threadName=self.name, delay=self.delay, counter=5)
        # 释放锁
        # threadLock.release() # 线程同步
        print( "Exiting " + self.name)

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            _thread.exit()
        sleep(delay)
        print( "%s: %s" % (threadName, ctime(time())))
        counter -= 1

# #线程同步时 加如下
threadLock = threading.Lock() #如果多个线程共同对某个数据修改，则可能出现不可预料的结果，为了保证数据的正确性，需要对多个线程进行同步

threads = []
# 创建新线程 如果要线程同步的话，就要将线程同步的实例 生成在新线程的上面
thread1 = myThread(name="Thread-1", delay=1)
thread2 = myThread(name="Thread-2", delay=2)

# 开启线程
n = datetime.now()
thread1.start()
# thread1.join()# 先完成当时的线程，才启动并执行下一个线程
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()
print("Exiting Main Thread")

print(datetime.now()-n)
