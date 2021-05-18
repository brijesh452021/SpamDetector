# -*- coding: utf-8 -*-
"""app

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pdRz_WRlJkN1YbFzAypbiSxQeV15oY5W
"""

from flask import Flask,render_template,request
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
nltk.download('stopwords')

spamModel = pickle.load(open('spamclassifier_1.pkl', 'rb'))
tfidfModel= pickle.load(open('tfidf_transform.pkl', 'rb'))
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
  if request.method=='POST':
    message=request.form['message']
    wordcount=len(message.split())

    special_characters=['~','!','@','#','$','%','^','&','*','(',')','+','£','€','¥']
    specialCharPresent=0
    for item in special_characters:
      if item in message:
        specialCharPresent=1
    
    digitPresent=0
    words=[word for word in message]
    for character in words:
      if character.isdigit():
        digitPresent=1
    data=[message]
    tfidfVectors = tfidfModel.transform(data).toarray()
    tfidfList=tfidfVectors.tolist()[0]
    #print("tfidfList=",tfidfList)
    temp_List=[wordcount,specialCharPresent,digitPresent]
    temp_List.extend(tfidfList)
    #print("temp_List",temp_List)

    prediction=spamModel.predict([temp_List])


    print(prediction)

    if prediction==1:
      output='Spam'
    else:
      output='Not Spam'

    return render_template('result.html',prediction_text="Your Message is. {}".format(output))

  return render_template("index.html")

if __name__ == '__main__':
	app.run()
