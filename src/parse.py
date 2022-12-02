# import libraries
import os
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import cv2
import seaborn as sns
from scipy.linalg import eigh

class Parser: 

    def __init__(self,coil_20_path,netflix_path,mnist_path):
       
        self.data_path_coil20 =coil_20_path
        self.data_path_mnist = netflix_path
        self.data_path_netflix = mnist_path
    
        
    def parse_image_label_coil(self, filename):
        f = filename.split('_')[0]
        f = f.replace('obj', '')
        return int(f)


    def handle_non_numerical_data(self,df):
        columns = df.columns.values
        for column in columns:
            text_digit_vals = {}
            def convert_to_int(val):
                return text_digit_vals[val]
            if df[column].dtype != np.int64 and df[column].dtype != np.float64:
                column_contents = df[column].values.tolist()
                unique_elements = set(column_contents)
                x = 0
                for unique in unique_elements:
                    if unique not in text_digit_vals:
                        text_digit_vals[unique] = x
                        x+=1
                df[column] = list(map(convert_to_int, df[column]))

        return df
    def netflix(self):
        df = pd.read_csv(self.data_path_netflix)
        df = self.handle_non_numerical_data(df)
        X = df.drop('show_id', axis=1)
        X = X.drop('title', axis=1)
        X = X.drop('type', axis=1)
        y = df['type']
        scaler = StandardScaler()
        scaler.fit(X)
        X = scaler.transform(X)
        return X,y,df
        # print(f"Dataset shape: {df.shape}")
        # df.head()

    def mnist(self):
        # df = pd.read_csv('./data/mnist/mnist_train.csv', nrows = 20000)
        # print("the shape of data is :", df.shape)
        # df.head()
        pass

    def coil20(self):

        images = []
        labels = []
        print("This is : ",self.data_path_coil20)
        for filepath in os.listdir(self.data_path_coil20):
            f = os.path.join(self.data_path_coil20, filepath)
            img = cv2.imread(f)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            images.append(img)
            labels.append(self.parse_image_label_coil(filepath))

        images = np.array(images)
        labels = np.array(labels)
        return images, labels


