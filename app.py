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

model = pickle.load(open('spamclassifier.pkl', 'rb'))
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
  if (request.method=='POST'):
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

    stemmer=PorterStemmer()
    message = re.sub(pattern='[^a-zA-Z]', repl=' ',string=message)
    message = message.lower()
    words = [stemmer.stem(word) for word in message.split() if word not in stopwords.words('english')]
    message=' '.join(words)

    from sklearn.feature_extraction.text import TfidfVectorizer
    tfidf = TfidfVectorizer()
    Vectors=tfidf.fit_transform(list(message)).toarray()

    prediction=model.predict([[wordcount,specialCharPresent,digitPresent,Vectors]])

    output=round(prediction[0],2)

    if(output==1):
      output='Spam'
    else:
      output='Not Spam'

    return render_template('result.html',prediction_text="Your Message is. {}".format(output))

  return render_template("index.html")

if __name__ == '__main__':
	app.run(debug=True)