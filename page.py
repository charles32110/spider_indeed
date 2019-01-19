#coding:utf-8
import requests
import re
#.*?<span class="_2njvnpA">,</span>(.*?)</span>
#

url = 'https://www.seek.com.au/job/37991435?type=standard&amp;searchrequesttoken=dc30b113-e600-4915-8f06-6723fe600512'
a = requests.get(url=url)
#侧向标签分类
date = re.findall('<section role="region" aria-labelledby="jobInfoHeader">.*?\
<span class="lwHBT6d">(.*?)</span>',a.content,re.S)
location = re.findall('<section role="region" aria-labelledby="jobInfoHeader">.*?\
<span class="eBOHjGN".*?</span>(.*?)</span>',a.content,re.S)
jobtime = re.findall('<section role="region" aria-labelledby="jobInfoHeader">.*?\
data-automation="job-detail-work-type".*?class="lwHBT6d">(.*?)</span',a.content,re.S)
jobtype = re.findall('<section role="region" aria-labelledby="jobInfoHeader">.*?\
<div.*?class="_2njvnpA">, </span>(.*?)</span',a.content,re.S)

print date[0],location[0],jobtime[0],jobtype[0]


