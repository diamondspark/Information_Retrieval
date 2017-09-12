import pandas as pd
import re
import numpy as np
from utils_Clever_Heart_DL import dropStopWords

def makeOutputdf():
    output_df = pd.DataFrame(keys)
    output_df.columns=['Field']
    #output_df.set_index(['field'], inplace=True)
    output_df['value']=np.zeros(103)
    output_df['comments']=np.zeros(103)
    output_df['repo'] =None
    return output_df

def getFooter(text):
    prep = getWordIndex(text,'prepared by')
    diag = getWordIndex(text,'diagnosis')
    study = getWordIndex(text,'study interpreted and report approved by')
    if prep is not None:
        return prep.start()
    if diag is not None:
        return diag.start()
    if study is not None:
        return study.start()

def getWordIndex(string, word):
    a = re.search(r'\b('+word+r')\b', string)
    return a

df = pd.read_csv('freetext reports divided.csv')
output_df = pd.DataFrame()
output_df['value']=np.zeros(100)
output_df['repo'] =None

for i in range(0,100):
    if i ==91:
        continue
    report1 = df.iat[i,0].lower()
    header = getWordIndex(report1,'findings').start()
    footer = getFooter(report1)
    output_df['repo'][i]=report1[header:footer]
    
