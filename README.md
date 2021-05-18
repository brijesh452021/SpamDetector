**Spam Detector**

Its a Machine Learning based project that detects if a message is a spam or not. **Bagging(Random Forest Classifier) and Boosting (XGBoost)** Technique is used to detect the spam. Below are some analysis done based on different feature engg.

1. wordcount

![wordcount](https://user-images.githubusercontent.com/81951806/118611781-d341f200-b7da-11eb-87b9-6c17786554f9.png)

2. special characters in message

![specialcharacters](https://user-images.githubusercontent.com/81951806/118611868-e3f26800-b7da-11eb-83b4-1ef747054675.png)

3. Numbers in message

![Digitspresent](https://user-images.githubusercontent.com/81951806/118611932-f076c080-b7da-11eb-89d7-ae61f87ceb7c.png)

4. Distribution of word count

![wordcount2](https://user-images.githubusercontent.com/81951806/118612092-0e442580-b7db-11eb-85c8-50094537f98f.png)

**TFIDFVectorizer** is used to convert the words to vectors.

Confusion Matrix for Random Forest Classifier

![randomforestconfusionmatrix](https://user-images.githubusercontent.com/81951806/118612263-392e7980-b7db-11eb-9d48-6c4739405044.png)

Accuracy for Random Forest Classifier: F1Score-0.97

Confusion Matrix for XGBoost


Accuracy for XGBoost: ROC-AUC-


