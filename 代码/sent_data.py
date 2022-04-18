# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 12:21:51 2022

@author: Joe Yuan
"""

import requests as res
import json
import pymysql
import torch
import pandas as pd
from model import init_model,predict_from_ex,Emotion_FinBERT,gen_t
from load_data import Config
model=Emotion_FinBERT()
model_dict=model.load_state_dict(torch.load(Config.SAVE_PATH))
import numpy as np
from gen_data1 import gen_es,gen_cctv,gen_vote,updown_count,gen_news()
import time

def upload_predict():

    url='http://10.235.142.27:8080/predict'
    params={'text':'hello world'}
    rs=res.post(url,data=params,timeout=10)
    ans=json.loads(rs.text)
def local_predict(text):
    t1=gen_t(text,False)
    with torch.no_grad():
        output=model(t1['token'],t1['mask'],t1['token_id'])
        predict=np.argmax(output.detach().cpu().numpy(),axis=1)
    return predict

class OMySql:
    def __init__(self):
        self.db=pymysql.connect(host='127.0.0.1',user='root',password='13425392359',database='finbert',port=3306)
    def insert(self,t,com,l):
        c=self.db.cursor()
        sql="CALL UPD('{}','{}',{},@res);".format(t,com,int(l))
        try:
            c.execute(sql)
        except:
            print('数据插入失败')
            self.db.rollback()
    def close(self):
        self.db.close()
        print('连接关闭')
    def commit(self):
        print('提交数据')
        self.db.commit()
        
def run_crawber(times=6):
    DB=OMySql()
    temp=[]
    gen_vote()
    gen_news()
    updown_count()
    for i in range(times):
        
        print('正在爬取第{}批数据'.format(i))
        infos=gen_es(p=i+1)
        re=infos['re']
        
        for i in range(len(re)):
            if re[i]['post_id'] not in temp:
                if len(re[i]['post_content'])<256:
                    label=local_predict(re[i]['post_content'])
                    slabel=''
                    if label==0:
                        slabel='消极'
                    elif label==2:
                        slabel='乐观'
                    else:
                        slabel='中立'
                    temp.append(re[i]['post_id'])
                    #插入
                    DB.insert(re[i]['post_publish_time'],re[i]['post_content'],label)
                    print('尝试插入数据:{}'.format(str(re[i]['post_id'])))
                    if len(temp)>=100:
                        temp.pop(0)
        DB.commit()
        time.sleep(5)
    DB.close()
run_crawber(times=10)



'''
url='http://45.83.253.23/web/index.php?act=1'
data={'u':'19023932394','bianhao':'ddsddwd','p':'13242dqqa'}
#d=open('D:/bert_weight_files/roberta/bert_model.ckpt.meta','rb')
#files = {'file': d}
headers={
            'Host': '45.83.253.23',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate, br',
            
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Upgrade-Insecure-Requests': '1',
            'PHPSESSID':'72k576ro4hdsv7l255vbtcq4q4'
            }
#t=res.post(url,data=data,headers=headers,timeout=10)
i=0
while(True):
    print(i)
    t=res.post(url,data=data,headers=headers,timeout=10)
    i+=1
'''