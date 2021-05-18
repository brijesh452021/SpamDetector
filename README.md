**Spam Detector**

Its a Machine Learning based project that detects if a message is a spam or not. **Bagging(Random Forest Classifier) and Boosting (XGBoost)** Technique is used to detect the spam. Below are some analysis done based on different feature engg.

1. wordcount

![wordcount](https://user-images.githubusercontent.com/81951806/118611781-d341f200-b7da-11eb-87b9-6c17786554f9.png)

For the messages which are not spam, most of the word count lies in 6-13 whereas for spam messages its lies between 22-30

2. special characters in message

![specialcharacters](https://user-images.githubusercontent.com/81951806/118611868-e3f26800-b7da-11eb-83b4-1ef747054675.png)

Special Characters are present in most of the spam messages

3. Numbers in message

![Digitspresent](https://user-images.githubusercontent.com/81951806/118611932-f076c080-b7da-11eb-89d7-ae61f87ceb7c.png)

Numbers are present in most of the spam messages

4. Distribution of word count

![wordcount2](https://user-images.githubusercontent.com/81951806/118612092-0e442580-b7db-11eb-85c8-50094537f98f.png)

50 percentile lies around word count 10 in ham messages whereas it lies around 25 in spam messages. Some part of Distribution are overlapping when word count is low

5. Words like Call, Guaranteed, Service,Customer are more frequest in Spam Messages.

![spamwordcloud](https://user-images.githubusercontent.com/81951806/118686662-d3b1ab80-b821-11eb-810b-cfaf18ae791e.png)


**TFIDFVectorizer** is used to convert the words to vectors and then PCA is applied to reduce the dimension and to get the important features.

Confusion Matrix for Random Forest Classifier

![randomforestconfusionmatrix](https://user-images.githubusercontent.com/81951806/118612263-392e7980-b7db-11eb-9d48-6c4739405044.png)

Accuracy for Random Forest Classifier: F1Score-0.97

Confusion Matrix for XGBoost

![xgboostconfusionmatrix](https://user-images.githubusercontent.com/81951806/118632696-4c971000-b7ee-11eb-80ac-cd309aad9967.png)

Accuracy for XGBoost: 0.96


