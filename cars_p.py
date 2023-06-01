# -*- coding: utf-8 -*-
"""cars_projects.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LFCgBgz0kH8GL-2yZ5OqIQ6no48s_ZIW
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import time
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor,DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder,OrdinalEncoder,StandardScaler
from sklearn.model_selection import train_test_split,GridSearchCV,RandomizedSearchCV
from sklearn.pipeline import Pipeline
from sklearn.compose import make_column_transformer,ColumnTransformer
from sklearn.metrics import mean_squared_error
from sklearn.feature_selection import SelectKBest, f_regression,f_classif
from catboost import CatBoostRegressor

@st.cache_data()
def load_and_preprocess_data():
  url = 'https://raw.githubusercontent.com/Zeroflip64/Study_projects/main/cars.csv'
  df = pd.read_csv(url)
    
  features=df.drop(['Price'],axis=1)
  target=df['Price']

  features_train,fetures_test,target_train,target_test=train_test_split(features,target,test_size=0.25,random_state=345,shuffle=target)

  pre=make_column_transformer((OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1),[i for i in features.columns  if features[i].dtype !='int']),
                              (StandardScaler(),[i for i in features.columns  if features[i].dtype =='int' and i!='Price']))
  def study(features,target,param,model):
    feature_selection = SelectKBest(score_func=f_regression)
    pipeline = Pipeline([('preprocesing',pre),
      ('selection',feature_selection),('model',model)])
    grid = RandomizedSearchCV(pipeline, param, cv=5,scoring='neg_root_mean_squared_error')
    grid.fit(features, target)
    return grid

  light=study(features_train,target_train,{'selection__k': [3, 6, 10],'model__learning_rate':[0.01,0.1,1],'model__l2_leaf_reg': [0.1, 1, 10],'model__n_estimators': [100, 500, 100],'model__depth':[4,6,8]},CatBoostRegressor(verbose=False))
  return features,light

features_df, trained_model = load_and_preprocess_data()

st.write('Модель загруженна')

language = ['RUS', 'ENG']
selected_variation = st.selectbox('Выберите язык/Choose language', language)

if selected_variation == 'RUS':
    input_label = 'Введите значение для'
    error_message = 'Недопустимый числовой ввод для'
    confirmation_text = 'Подтвердите ваши данные'
elif selected_variation == 'ENG':
    input_label = 'Enter a value for'
    error_message = 'Invalid numeric input for'
    confirmation_text = 'Confirm your data'

selected_values = {}
all_columns = features_df.columns.tolist()

user_df = pd.DataFrame(columns=all_columns)
temp_df = features_df.copy()  # Create a temporary copy of the DataFrame

for i, column in enumerate(all_columns):
    if temp_df[column].dtypes=='object':
        unique_values = temp_df[column].unique().tolist()


        selected_value = st.selectbox(f'{input_label} {column}', unique_values, key=column)


        temp_df = temp_df[temp_df[column] == selected_value]

        selected_values[column] = selected_value
        
    elif pd.api.types.is_numeric_dtype(features_df[column]):
        numeric_value = st.text_input(f"{input_label} {column}", key=column)
        if numeric_value:
            try:
                numeric_value = float(numeric_value)
                selected_values[column] = numeric_value
            except ValueError:
                st.error(f"{error_message} {column}")

    elif column == 'PostalCode':
        postal_code = st.text_input(f"{input_label} PostalCode", key='PostalCode')
        selected_values[column] = str(postal_code)
st.write(pd.DataFrame(selected_values,ignore_index=True))
if st.checkbox(confirmation_text):

    user_df = user_df.append(selected_values, ignore_index=True)

    st.dataframe(user_df)
    st.write(f'Стоимость вашей машины : {np.round(*trained_model.predict(user_df),2)} EUR')
