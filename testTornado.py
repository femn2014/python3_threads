import http.client
import queue
import threading
from datetime import datetime


def quickly():
    n = datetime.now()
    print(str(n)+': quickly begin')
    conn = http.client.HTTPSConnection("app.bzby365.com:8010")

    headers = {
        'cache-control': "no-cache",
        'postman-token': "fdf872b1-2082-cd96-bb8d-fd2f5cb1f618"
        }

    conn.request("GET", "/c/shuju_all", headers=headers)

    res = conn.getresponse()
    data = res.read()

    # print(data.decode("utf-8"))
    print(str(datetime.now()-n)+': quickly 耗时')

def slow():
    n = datetime.now()
    print(str(n)+': slow begin')
    conn = http.client.HTTPSConnection("app.bzby365.com:8010")

    headers = {
        'cache-control': "no-cache",
        'postman-token': "fdf872b1-2082-cd96-bb8d-fd2f5cb1f618"
    }

    conn.request("GET", "/a/businessmanage?_id=5821bc8e4406b72beb20581e", headers=headers)
    res = conn.getresponse()
    data = res.read()
    # print(data.decode("utf-8"))
    print(str(datetime.now()-n)+': slow 耗时')
q =queue.Queue()
for i in range(4):

    q.put(slow)

for i in range(4):
    q.put(quickly)

def worker():
    global q
    while not q.empty():
        url = q.get()  # 获得任务
        print(url)
        q.task_done()

if __name__ == '__main__':
    # worker()

    thread1 = threading.Thread(target=quickly())
    thread2 = threading.Thread(target=slow())
    #总是quickly先执行
    thread2.start()
    thread2.join()
    thread1.start()
    # 总是quickly先执行

