#coding:utf-8
#search for a job in sydney as a python developer
import requests
import re
import Queue
import threading
'''
url = 'https://www.seek.com.au/python-jobs/in-All-Sydney-NSW'
head = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
a = requests.get(url=url, headers=head)
x = re.compile('<div data-sol-meta.*?<article aria-label="(.*?)".*?<span.*?<div href="(.*?)".*?</div',re.S)
link =  x.findall(a.content)
for a,b in link:
    print (a,b)
'''

link_que = Queue.Queue()
n = 27
class spider(object):



    def __init__(self):
        self.url1 = 'https://www.seek.com.au/python-jobs/in-All-Sydney-NSW?page='
        self.url2 = 'https://www.seek.com.au'
        self.head = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6)\
         AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
        self.n = 27

    def getlink(self):
        global n
        n = n-1
        url = self.url1+'%s'%n
        a = requests.get(url=url , headers=self.head)
        x = re.compile('<div data-sol-meta.*?<article aria-label="(.*?)".*?<span.*?<div href="(.*?)".*?</div', re.S)
        link = x.findall(a.content)
        for a, b in link:
            link_que.put((a,b))
            print ('第%s页'%n)
        #print link_que.get()

    def getcontent(self):
        contuple = link_que.get()
        jobtitle = contuple[0]
        src = self.url2 + contuple[1]





    def fast(self):
        x = 0
        while  n > 0:
            t = threading.Thread(target=self.getlink)
            t.start()
            t.join()
        for i in range(1,6):
            while not link_que.empty():
                t2 = threading.Thread(target=self.getcontent)
                t2.start()





if __name__=='__main__':
    t = spider()
    t.fast()





