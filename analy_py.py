
import pandas as pd
import nltk
import jieba
import wordcloud
import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib as mpl
import matplotlib.pyplot as plt
import pylab
import collections

import codecs
import re

pypath = './testpy.csv'
df = pd.read_csv(pypath,encoding = "ISO-8859-1")

df['discription'].to_csv('a.txt',index=False)


'''
mytext = jieba.cut(aa,cut_all=False)

wc = wordcloud.WordCloud(background_color= 'Black',
                         max_words=1000,
                         max_font_size=50,
                         random_state=30)
mycloud = wc.generate(mytext)
plt.imshow(mycloud)
plt.axis('off')
plt.show()

#print (df.isnull().sum())
#print (df.info())
#print (df.describe())
#(df['field'].value_counts()).plot.pie(autopct='%1.1f%%')#column
#plt.show()

#print showdf[['jobtitle','jobtype']]#columns

a = 'Dev'; b = 'Network'; c = 'Engineer';d = 'Analy';e = 'Info';f = 'amp';
w = 0; x =0 ; y = 0; z = 0;n =0;u = 0;v= 0
for i in df.field:
    if a in i:
        w += 1
    elif b in i:
        x += 1
    elif c in i:
        y += 1
    elif d in i:
        z += 1
    elif e in i:
        n += 1
    elif f in i:
        u += 1
    else:
        v += 1

series = pd.Series((w,x,y,z,n,u,v),index=['Python Developer','Network System','WebEngineer','Data Analysis',
                                          'Informtaion Tech','IT support','Other'])
series.plot.pie(autopct='%1.1f%%')
plt.show()

#(df['field'].value_counts()).plot.pie()#column
#plt.show()
#for g in df.field:
    #print (g)

#print(df['location'].value_counts())
#(df['location'].value_counts()).plot.pie(autopct='%1.1f%%')#column
#plt.show()

CBD, Inner West &amp; Eastern Suburbs                 285
Ryde &amp; Macquarie Park                              28
Developers/Programmers                                 24
North Shore &amp; Northern Beaches                     24
Parramatta &amp; Western Suburbs                       13


q=0;w=0;e=0;r=0
for key in df['location']:
    if 'CBD' in key:
        q = q+1
    elif 'Park'in key:
        w+=1
    elif 'North' in key:
        e +=1
    elif 'West' in key:
        r +=1
series = pd.Series((q,w,e,r),index=['CBD, Inner West &amp; Eastern Suburbs','Ryde &amp; Macquarie Park',
                                    'North Shore &amp; Northern Beaches','Parramatta &amp; Western Suburbs'])
series.plot(kind='bar')
plt.show()


'''
