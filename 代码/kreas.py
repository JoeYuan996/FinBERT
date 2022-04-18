# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 16:37:42 2022

@author: Joe Yuan
"""

import keras
from keras.models import Model
import keras.backend as K
from keras.callbacks import Callback
from keras.optimizers import Adam
from keras.regularizers import l2
from bert4keras.models import build_transformer_model
#from utils import seq_gather, extract_items, metric
from tqdm import tqdm
import numpy as np

bert_layers = 12

def FinBertModel(bert_config_path):
    bert_model = build_transformer_model(
            config_path=bert_config_path,
            #checkpoint_path=bert_checkpoint_path,
            return_keras_model=True,
        )
    tokens_feature = bert_model.get_layer('Transformer-2-FeedForward-Norm').output
    pred = keras.layers.Dense(3, activation='sigmoid')(tokens_feature)
    FinBert_model = Model(bert_model.input, pred) 
    return FinBert_model
a=FinBertModel(r'D:/bert_weight_files/roberta/bert_config_rbt3.json')
keras.utils.plot_model(a, "finbert.png", show_shapes=True)
