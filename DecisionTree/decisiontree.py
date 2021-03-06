# -*- coding: utf-8 -*-
"""DecisionTree.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w-Yrf9En8ij4exPSx3w6eNP90hmJ4BaT

**DecisionTree**

---

Karar Ağaçları, sınıflandırma ve regression çözümüne uyarlanabilirler.
Bir karar ağacı, çok sayıda kayıt içeren veri kümesini bir dizi karar kuralları uygulayarak daha küçük parçalara bölmek için kullanılan bir yöntemdir.

 **Avantajları:**
*  Anlama ve yorumlarama olarak kolaydır.Kullanılan ağaç yapıları görselleştirilebilir.

* Az oranda bir veri hazırlanmasına ihtiyaç duyar.Kayp değerleri desteklememektedir.
* Kullanılan ağacın maliyeti, ağacı eğitmek için kullanılan veri noktalarının sayısıyla logaritmiktir.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data=pd.read_csv("data.csv")
data.drop(["id", "Unnamed: 32"], axis=1, inplace=True)

M=data[data.diagnosis=="M"]
B=data[data.diagnosis=="B"]

plt.scatter(M.radius_mean, M.texture_mean, color="red",label="kotu", alpha=0.3)
plt.scatter(B.radius_mean, B.texture_mean, color="green",label="iyi",alpha=0.3)
plt.xlabel("radius_mean")
plt.ylabel("texture_mean")
plt.legend()
plt.show()

data.diagnosis=[1 if each =="M" else 0 for each in data.diagnosis]
y=data.diagnosis.values
x_data=data.drop(["diagnosis"],axis=1)

x =(x_data - np.min(x_data))/(np.max(x_data)-np.min(x_data))

from sklearn.model_selection import train_test_split
x_train, x_test,y_train, y_test = train_test_split(x,y,test_size = 0.15,random_state = 42)

from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier()
dt.fit(x_train,y_train)

print("score: ", dt.score(x_test,y_test))

y_pred = dt.predict(x_test)  
y_pred

from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, y_pred)