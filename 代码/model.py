# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 15:13:55 2022

@author: Joe Yuan
"""
from load_data import gen_DataLoader,Config
import torch
import torch.nn as nn
import transformers
from transformers import get_linear_schedule_with_warmup,BertTokenizer, BertForSequenceClassification,  BertConfig
from tqdm import tqdm
from torch import optim
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#
class Emotion_FinBERT(nn.Module):
    def __init__(self):
        super(Emotion_FinBERT,self).__init__()
        self.bert=transformers.BertForSequenceClassification.from_pretrained(Config.BERT_PATH,num_labels=3)
        #self.drop=nn.Dropout(0.3)
        #self.dense=nn.Linear(768,Config.EMO_CLASS)
        #Config.TOKENIZER.encode()
        #self.soft=nn.Softmax()
    
    def forward(self,tokens,mask,ids):
        output=self.bert(tokens,attention_mask=mask,token_type_ids=ids)
        #output=self.drop(output)
        #output=self.soft(self.dense(output))
        
        return output['logits']


def init_model(a):
    model=Emotion_FinBERT()
    
    model.to(Config.DEVICE)
    m_params=list(model.named_parameters())
    lock_params=[]#['bias','LayerNorm.bias','LayerNorm.weight']
    set_decay=[
            {
                    'params':[p for n,p in m_params if not any(nd in n for nd in lock_params)],
                    "weight_decay": 0.001,
    
                    },
            {
                    'params':[p for n,p in m_params if any(nd in n for nd in lock_params)],
                    "weight_decay": 0,
                    }    
                ]
    train_step=int(len(a['train'])/Config.TRAIN_BS*Config.EPOCHS)
    
    optimizer=optim.Adam(set_decay)
    scheduler=get_linear_schedule_with_warmup(optimizer,num_warmup_steps=1,num_training_steps=train_step)
    #scheduler=[]
    return model, optimizer,scheduler

a=gen_DataLoader()
model, optimizer,scheduler=init_model(a)

model_dict=model.load_state_dict(torch.load(Config.SAVE_PATH))
''' 
bestloss=np.inf
f=nn.CrossEntropyLoss()

loss_list=[]

model.train()
for epo in range(Config.EPOCHS):
    
    print('{:*^30}'.format('Epochs:'+str(epo)))
    total_loss=0
    k=0
    for info in tqdm(a['train']):
        
        
        output=model(info['token'].to(Config.DEVICE),mask=info['mask'].to(Config.DEVICE),ids=info['token_id'].to(Config.DEVICE))
        print(output)
        loss=f(output,info['label'].to(Config.DEVICE))
        total_loss+=loss.item()
        loss_list.append(loss.item())
        loss.backward()
        optimizer.step()
        #scheduler.step()
        model.zero_grad()
        optimizer.zero_grad()
        k+=1
        if(k==10):
            break
      

    if total_loss<bestloss:
        torch.save(model.state_dict(), Config.SAVE_PATH)
        bestloss=total_loss
plt.plot(loss_list)
'''

def gen_t(text,to_cuda=False):
    token=Config.TOKENIZER.encode(text,add_special_tokens=False)
    token=[101]+token[:Config.MAXLEN-2]+[102]
    pad_len=Config.MAXLEN-len(token)
    mask=[1 for _ in range(len(token))]+[0 for _ in range(pad_len)]
    token=token+[0 for _ in range(pad_len)]
    token_id=[0 for _ in range(Config.MAXLEN)]
    if not to_cuda:
        return {
                
                'token':torch.tensor([token]),
                'mask':torch.tensor([mask]),
                'token_id':torch.tensor([token_id])
                }
    return {
                
                'token':torch.tensor([token]).to(Config.DEVICE),
                'mask':torch.tensor([mask]).to(Config.DEVICE),
                'token_id':torch.tensor([token_id]).to(Config.DEVICE)
                }
def predict_from_ex(x,use_cuda=False):
    t1=gen_t(x,to_cuda=False)
    
    with torch.no_grad():
        output=model(t1['token'],t1['mask'],t1['token_id'])
    
        predict=np.argmax(output.detach().cpu().numpy(),axis=1)
    return int(predict)
'''
dfs=pd.read_excel('cc41.xlsx')
dfs['label']=dfs['text'].apply(predict_from_ex)
dfs.to_excel('cctvt.xlsx',encoding='utf_8_sig',index=False)
'''
#model_dict=model.load_state_dict(torch.load(Config.SAVE_PATH))

'''
k=0
#model.eval()
with torch.no_grad():
    model.zero_grad()
    optimizer.zero_grad()
    l=[]
    vtotal_loss=0
    total_val=len(a['val'])
    cor_num=0
    for info in tqdm(a['val']):
        
        output=model(info['token'].to(Config.DEVICE),mask=info['mask'].to(Config.DEVICE),ids=info['token_id'].to(Config.DEVICE))
        #vloss=f(output,info['label'].to(Config.DEVICE))
        #vtotal_loss+=vloss.item()
        predict=np.argmax(output.detach().cpu().numpy(),axis=1)
        l.append(predict)
        print(output)
        #print(predict,info['label'].numpy())
        #print(info['token'])
        #print(predict)
        #print(' ')
        #print(info['label'])
        cor_num+=len(predict[predict==info['label'].numpy()])
        
        k+=1
        if(k==10):
            break
    
    precision=cor_num/total_val
'''
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score
def val(model,a):
    k=0
    act=[]
    pre=[]
    with torch.no_grad():
        
        vtotal_loss=0
        total_val=len(a['val'])
        cor_num=0
        for info in tqdm(a['val']):
            #model.zero_grad()
            output=model(info['token'].to(Config.DEVICE),mask=info['mask'].to(Config.DEVICE),ids=info['token_id'].to(Config.DEVICE))
            #vloss=f(output,info['label'].to(Config.DEVICE))
            #vtotal_loss+=vloss.item()
            predict=np.argmax(output.detach().cpu().numpy(),axis=1)
            #print(predict,info['label'].numpy())
            #print(info['token'])
            
            #print(' ')
            #print(info['label'])
            cor_num+=len(predict[predict==info['label'].numpy()])
            act.append(int(info['label'].numpy()[0]))
            pre.append(int(predict[0]))
            '''
            k+=1
            if(k==10):
                break
                '''

    ac=accuracy_score(act,pre)
    pr=precision_score(act,pre,average='weighted')
    re=recall_score(act,pre,average='weighted')
    f1=f1_score(act,pre,average='weighted')
    print('ac:{} pr:{} re:{} f1:{}'.format(ac,pr,re,f1))


'''
ac:0.856203007518797 pr:0.8574562244151016 re:0.856203007518797 f1:0.8564087051809383
'''

'''
t1=gen_t('哈哈哈今天赚了好多',True)
t0=gen_t('呜呜呜我想死',True)
model(t0['token'],t0['mask'],t0['token_id'])
model(t1['token'],t1['mask'],t1['token_id'])
m_params=list(model.named_parameters())
lock_params=['LayerNorm.weight']
s=[[n,p] for n,p in m_params if  any(nd in n for nd in lock_params)]
for i in range(len(s)):
    #print(i,s[i][0])
    print(s[i][1][1:10])
'''