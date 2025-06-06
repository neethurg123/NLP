# -*- coding: utf-8 -*-
"""Tweet Emotion Recognition

**Tweet Emotion Recognition**

**1. Install all libraries required**
"""

!pip install -U datasets

"""**2. Importing libraries**"""

import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
from datasets import load_dataset
from tensorflow import keras

"""**3. Importing Data**"""

data_set = load_dataset('emotion')

data_set.shape

train=data_set['train']
test=data_set['test']
validate=data_set['validation']
train

def get_text(data):
  tweet=data['text']
  label=data['label']
  return tweet,label

tweet_train, label_train =get_text(train)
tweet_train[9],label_train[9]

tweet_val, label_val =get_text(validate)
tweet_val[9],label_val[9]

"""**4. Tokenizing**"""

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
token=Tokenizer(num_words=10000,oov_token='<OOV>')
token.fit_on_texts(tweet_train)

def val(token,data):
  value=token.texts_to_sequences(data)
  value_pad=pad_sequences(value,maxlen=50,padding='post',truncating='post')
  return value_pad

value_pad_train=np.array(val(token,tweet_train))
value_pad_val=np.array(val(token,tweet_val))
label_train=np.array(label_train)
label_val=np.array(label_val)

"""**5. Building & Training the model**"""

model=tf.keras.Sequential([
    tf.keras.Input(shape=(50,)),
    tf.keras.layers.Embedding(10000,16),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(20,return_sequences=True)),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(20)),
    tf.keras.layers.Dense(6,activation='softmax')
])
model.compile(loss='sparse_categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
model.summary()

model.fit(value_pad_train,label_train,epochs=10,validation_data=(value_pad_val,label_val))

model.history.history.keys()

"""**6. Loss & Accuracy Curves**"""

plt.figure(figsize=(12,9))
plt.subplot(1,2,1)
plt.plot(model.history.history['loss'],label='Training Loss')
plt.plot(model.history.history['val_loss'],label='Validation Loss')
plt.legend()
plt.title('Loss Curves')
plt.subplot(1,2,2)
plt.plot(model.history.history['accuracy'],label='Training Accuracy')
plt.plot(model.history.history['val_accuracy'],label='Validation Accuracy')
plt.legend()
plt.title('Accuracy Curves')
plt.show()

"""**7. Evaluation**"""

tweet_test, label_test =get_text(test)
value_pad_test=np.array(val(token,tweet_test))
label_test=np.array(label_test)
value_pad_test=np.array(value_pad_test)
eval= model.evaluate(value_pad_test,label_test)

"""**8. Prediction**"""

pred=model.predict(value_pad_test)
pred_class=np.argmax(pred,axis=1)

for i in range(10):
  print('Tweet:', tweet_test[i])
  print('Actual Emotion:', label_test[i])
  print('Predicted Emotion:', pred_class[i])
  print('----------------------------------------------')

"""**9. Confusion Matrix & Heatmaps**"""

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(label_test,pred_class)
heatmap=sns.heatmap(cm,annot=True,fmt='g')
heatmap.set_title('Confusion Matrix')
heatmap.set_xlabel('Predicted Class')
heatmap.set_ylabel('Actual Class')
