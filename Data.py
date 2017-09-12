from Classifier import loadOutputDF
import pandas as pd
import numpy as np

df = pd.read_csv('100.csv')
df['pleural effusion']=np.zeros(len(df))
df['cardiomegaly']=np.zeros(len(df))
df['ascites']=np.zeros(len(df))
df['pulmonary edema']=np.zeros(len(df))
df['lymphadenopathy']=np.zeros(len(df))
df['gb thickening']=np.zeros(len(df))
df['hydronephrosis']=np.zeros(len(df))
df['hernia']=np.zeros(len(df))
df['atelectasis']=np.zeros(len(df))
df['enlarged liver']=np.zeros(len(df))
df['aortic aneurysm']=np.zeros(len(df))
df['atherosclerosis']=np.zeros(len(df))
df['previous surgery']=np.zeros(len(df))
df['pneumonia']=np.zeros(len(df))

gt = pd.read_excel('/Users/mop2014/Downloads/output.xlsx')

for i in range(0,91):
    for j in range(0,14):
        col_name = gt['Field'][j*14+j]
        #print col_name + str (gt['value'][i*14+j])
        df[col_name][i]=gt['value'][i*14+j]

df.to_csv('gt.csv')
