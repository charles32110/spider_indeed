#coding:utf-8
#search for a job in sydney as a python developer
import requests
import re
import Queue
import threading
import csv
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
        #self.url1 = 'https://www.seek.com.au/it-jobs/in-All-Sydney-NSW?page=2'
        self.url2 = 'https://www.seek.com.au'
        self.head = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6)\
         AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
        #self.n = 50

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
        #jobtitle = contuple[0]
        src = self.url2 + contuple[1]
        a = requests.get(url=src)
        # 侧向标签分类
        date = re.findall('<section role="region" aria-labelledby="jobInfoHeader">.*?<span class="lwHBT6d">(.*?)</span>', a.content, re.S)[0]
        location = re.findall('<section role="region" aria-labelledby="jobInfoHeader">.*?<span class="eBOHjGN".*?</span>(.*?)</span>', a.content, re.S)[0]
        jobtime = re.findall('<section role="region" aria-labelledby="jobInfoHeader">.*?data-automation="job-detail-work-type".*?class="lwHBT6d">(.*?)</span', a.content, re.S)[0]
        jobtype = re.findall('<section role="region" aria-labelledby="jobInfoHeader">.*?<div.*?class="_2njvnpA">, </span>(.*?)</span', a.content, re.S)[0]
        #文章主体内容
        jobtitle = re.findall('<div data-automation="desktopTemplate".*?<h1 class="jobtitle">(.*?)</h1>', a.content, re.S)[0]
        context = re.findall('<div data-automation="desktopTemplate".*?class="templatetext">(.*?)</div', a.content, re.S)[0]
        context = re.sub('<[^<]+?>', '', context)#处理文本去掉标签
        context = re.sub('  +', '', context)
        with open('testpy.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([date, jobtitle, jobtype, jobtime, location, context])
            f.close()



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
                t2.join()





if __name__=='__main__':
    t = spider()
    t.fast()





