# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 11:48:13 2022

@author: Joe Yuan
"""
from model import init_model,predict_from_ex,Emotion_FinBERT,gen_t
from load_data import Config
import flask
import torch
import numpy as np
app=flask.Flask(__name__)
model=Emotion_FinBERT()
model_dict=model.load_state_dict(torch.load(Config.SAVE_PATH))

@app.route("/predict",methods=['post'])
def predict():
    data={'success':False}
    if flask.request.method == 'POST':
        if flask.request.form['text']:
            t1=gen_t(flask.request.form['text'],False)
            with torch.no_grad():
                output=model(t1['token'],t1['mask'],t1['token_id'])
                predict=np.argmax(output.detach().cpu().numpy(),axis=1)
                data['predict']=int(predict)
                data['success']=True
    return flask.jsonify(data)
app.run(host='0.0.0.0',port=8080, debug=False)


