import streamlit as st
import pickle
from sklearn.preprocessing import StandardScaler
import pandas as pd
import time
from sklearn.datasets import fetch_california_housing
st.title('🏠House Price prediction using ML')
st.image('https://mir-s3-cdn-cf.behance.net/project_modules/1400/09a56674244811.5c27fd8c99e0c.gif')

df = pd.read_csv('house_data.csv')
X = df.iloc[:,;-3]
y = df.iloc[:,;-1]

st.sidebar.title('🏡Select House Features')
st.sidebar.image('https://mir-s3-cdn-cf.behance.net/project_modules/1400/09a56674244811.5c27fd8c99e0c.gif')
all_value = []
for i in X:
  ans = st.sidebar.slider(f'Select {i} value')
  all_value.append(ans)
st.write(all_value)

  



