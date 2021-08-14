import pandas as pd
import numpy as np
import os
import cv2

df = pd.read_csv('A_Z Handwritten Data.csv')

Alphabet = {}
for i in range(26):
    Alphabet[i] = chr(65+i)

folders = list(Alphabet.values())
for i in folders:
    os.mkdir("Fonts/"+i)

for i in range(len(df)):
    img = df.iloc[i].values[1:]
    img = np.resize(img,(28,28))
    alpha = df.iloc[i].values[0]
    cv2.imwrite("fonts/"+Alphabet[alpha]+"/" +str(i)+'.jpg',img)