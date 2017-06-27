
import threading
from time import ctime,sleep,time
from datetime import date,datetime,timedelta
#多个线程做同时做不同的事
def music(func):
    for i in range(2):
        print( "I was listening to %s. %s" %(func,ctime()),time())
        sleep(1)

def move(func):
    for i in range(2):
        print( "I was at the %s! %s" %(func,ctime()),time())
        sleep(3)

threads = [] # 装载多个线程的数组
t1 = threading.Thread(target=music,args=(u'爱情买卖',))
threads.append(t1)
t2 = threading.Thread(target=move,args=(u'阿凡达',))
threads.append(t2)


if __name__ == '__main__':
    for t in threads:# 子线程
        t.setDaemon(True)# 线程声明为守护线程，必须在start() 方法调用之前设置，如果不设置为守护线程程序会被无限挂起
        #子线程启动后，父线程也继续执行下去，当父线程执行完最后一条语句print "all over %s" %ctime()后，没有等待子线程，直接就退出了，同时子线程也一同结束。
        print('开始线程活动')
        t.start()#

    t.join()  # 在子线程完成运行之前，这个子线程的父线程将一直被阻塞.join() 实际上意味着等到队列为空，再执行别的操作 。
    # join()方法的位置是在for循环外的，也就是说必须等待for循环里的两个进程都结束后，才去执行主进程。
    print( "all over %s" %ctime(),time()) # 主线程


