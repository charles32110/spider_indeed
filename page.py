#coding:utf-8
import requests
import re
import csv
#.*?<span class="_2njvnpA">,</span>(.*?)</span>
#

url = 'https://www.seek.com.au/job/37991435?type=standard&amp;searchrequesttoken=dc30b113-e600-4915-8f06-6723fe600512'
#url = 'https://www.seek.com.au/job/38032689?type=standout&amp;searchrequesttoken=155f2922-c20b-4ad2-bc20-647ac45dec6e'
#url = 'https://www.seek.com.au/job/38028591?type=standard&amp;searchrequesttoken=dbaff8ef-a832-418e-a543-790c407b222f'
a = requests.get(url=url)
#侧向标签分类
date = re.findall('<section role="region" aria-labelledby="jobInfoHeader">.*?\
<span class="lwHBT6d">(.*?)</span>',a.content,re.S)[0]
location = re.findall('<section role="region" aria-labelledby="jobInfoHeader">.*?\
<span class="eBOHjGN".*?</span>(.*?)</span>',a.content,re.S)[0]
jobtime = re.findall('<section role="region" aria-labelledby="jobInfoHeader">.*?\
data-automation="job-detail-work-type".*?class="lwHBT6d">(.*?)</span',a.content,re.S)[0]
jobtype = re.findall('<section role="region" aria-labelledby="jobInfoHeader">.*?\
<div.*?class="_2njvnpA">, </span>(.*?)</span',a.content,re.S)[0]

#print date,location,jobtime[0],jobtype[0]


jobtitle = re.findall('<div data-automation="desktopTemplate".*?\
<h1 class="jobtitle">(.*?)</h1>',a.content,re.S)[0]

context = re.findall('<div data-automation="desktopTemplate".*?\
class="templatetext">(.*?)</div',a.content,re.S)

context= re.sub('<[^<]+?>', '', context[0])
context = re.sub('  +','',context)
with open('test.csv', 'a') as f:
    writer = csv.writer(f )
    writer.writerow([date,jobtitle,jobtype,jobtime,location,context])
    f.close()
