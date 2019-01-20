
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




pypath = './testpy.csv'
df = pd.read_csv(pypath,encoding = "ISO-8859-1")
df['jobtitle'].value_counts().plot.bar()#column
plt.show()

#print showdf[['jobtitle','jobtype']]#columns