# -*- coding: utf-8 -*-
"""from load_data import Config
Created on Wed Mar  2 20:58:16 2022

@author: Joe Yuan
"""

import numpy as np
import random
import pandas as pd
import transformers
from torch.utils.data import DataLoader
import torch
class Config:
    EMO_CLASS=3
    MAXLEN=128
    TRAIN_BS=1
    VALID_BS=1
    EPOCHS=1
    BERT_PATH='D:/bert_weight_files/FinBERT'
    MODEL_PATH=BERT_PATH+'/models.bin'
    SAVE_PATH=BERT_PATH+'/c5_39.pkl'
    TRAIN_FILE='train.xlsx'
    VAL_FILE='val.xlsx'
    TOKENIZER=transformers.BertTokenizer.from_pretrained(BERT_PATH+'/')
    DEVICE=torch.device("cpu")#torch.device("cpu") if  not torch.cuda.is_available() else torch.device("cuda")
    
    

class DataSet:
    def __init__(self,text,label):
        self.texts=text
        self.labels=label
    def __len__(self):
        return len(self.texts)
    def __getitem__(self,item):
        text=self.texts[item]
        #print(text)
        label=self.labels[item]
        token=Config.TOKENIZER.encode(text,add_special_tokens=False)
        token=[101]+token[:Config.MAXLEN-2]+[102]
        pad_len=Config.MAXLEN-len(token)
        mask=[1 for _ in range(len(token))]+[0 for _ in range(pad_len)]
        token=token+[0 for _ in range(pad_len)]
        token_id=[0 for _ in range(Config.MAXLEN)]
        return {
                'label':torch.tensor(label),#,dtype=torch.float32
                'token':torch.tensor(token),
                'mask':torch.tensor(mask),
                'token_id':torch.tensor(token_id)
                }
        
def randomsplit(d,vals=0.1):
    x=[_ for _ in range(len(d))]
    samplei=random.sample(x,int(len(d)*vals))
    i=np.array([0 for i in range(len(d))])
    i[samplei]=1
    inds=np.array(x)
    val=inds[i==1]
    train=inds[i==0]
    dval=d.loc[val]
    #dval.index=[_ for _ in range(len(dval))]
    #print(dval)
    dtrain=d.loc[train]
    #dtrain.index=[_ for _ in range(len(dtrain))]
    return dval,dtrain
def gen_val_train():
    neg=pd.read_excel('estrans1.xlsx',sheet_name='Sheet2')
    pos=pd.read_excel('estrans1.xlsx',sheet_name='Sheet3')
    med=pd.read_excel('estrans1.xlsx',sheet_name='Sheet6')
    v0,t0=randomsplit(neg,vals=0.1)
    v1,t1=randomsplit(med,vals=0.1)
    v2,t2=randomsplit(pos,vals=0.1)
    val_df=pd.concat([v0,v1,v2],axis=0,ignore_index=True)
    train_df=pd.concat([t0,t1,t2],axis=0,ignore_index=True)
    val_df.to_excel(Config.VAL_FILE,encoding='utf_8_sig',index=False)
    train_df.to_excel(Config.TRAIN_FILE,encoding='utf_8_sig',index=False)

def gen_DataLoader():
    val=pd.read_excel(Config.VAL_FILE)
    train=pd.read_excel(Config.TRAIN_FILE)
    train_ds=DataSet(train['text'],train['label'])
    val_ds=DataSet(val['text'],val['label'])
    train_iter=DataLoader(train_ds,batch_size=Config.TRAIN_BS,shuffle=True)
    val_iter=DataLoader(val_ds,batch_size=Config.VALID_BS,shuffle=True)
    return {'train':train_iter,'val':val_iter}
'''
import torch.nn as nn
import torch
a=torch.tensor([0.1,0.2,0.3])
b=torch.tensor([0])
f=nn.CrossEntropyLoss()
'''