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
from lightgbm import LGBMRegressor



@st.cache_data()
def load_and_preprocess_data():
  url='https://drive.google.com/uc?export=download&id=130cth9oH1Q4ErTvz5SJ-bDjTidi_6Rqa'
  df=pd.read_csv(url)

  for i in ['PostalCode','Brand','Model','VehicleType','Gearbox']:
      df[i]=df[i].astype("category")
  for i in ['LastSeen','DateCrawled','DateCreated']:
      df[i]=pd.to_datetime(df[i],format='%Y-%m-%d %H:%M:%S')

  df=df.loc[(df['RegistrationYear']<2016) & (df['RegistrationYear']>1910) ]
  df=df.loc[df['Price']>10]
  df=df.loc[df['Power']>1]

  def missing(data,features,target):# Функция замены пропусков
      
      columns = [i for i in features]
      
      
      new_data = data.loc[(-data[target].isna())&(-data[columns[0]].isna())&(-data[columns[1]].isna())&
                    (-data[columns[2]].isna())&(-data[columns[3]].isna()),features+[target]]

      predict = data.loc[(data[target].isna())&(-data[columns[0]].isna())&(-data[columns[1]].isna())&
                    (-data[columns[2]].isna())&(-data[columns[3]].isna()),features]
      
      
      
      features=new_data.drop(target,axis=1)
      
      target=new_data[target]
      
      label=LabelEncoder()
      
      targets=label.fit_transform(target)
      
      
      encoder=OrdinalEncoder()
      
      new_transform=encoder.fit_transform(np.concatenate((features,predict),axis=0))
      
      features=new_transform[:new_data.shape[0]]
      
      predict=new_transform[new_data.shape[0]:]
      
      param={'max_depth':range(4,20,2)}
      
      
      
      
      grid=RandomizedSearchCV(DecisionTreeClassifier(),param,cv=3)
      grid.fit(features,targets)
      predict=grid.predict(predict)
      return label.inverse_transform(np.round(predict))

  df.loc[(df['Repaired'].isna())&(-df['Gearbox'].isna())&(-df['RegistrationYear'].isna())&
                    (-df['Brand'].isna())&(-df['Kilometer'].isna()),'Repaired']=missing(df,['Gearbox','Brand','Kilometer','RegistrationYear'],'Repaired')

  df.loc[(df['Model'].isna())&(-df['Gearbox'].isna())&(-df['RegistrationYear'].isna())&
                    (-df['Brand'].isna())&(-df['VehicleType'].isna()),'Model']=missing(df,['Gearbox','Brand','VehicleType','RegistrationYear'],'Model')

  df.loc[(df['Gearbox'].isna())&(-df['Model'].isna())&(-df['RegistrationYear'].isna())&
                    (-df['Brand'].isna())&(-df['VehicleType'].isna()),'Gearbox']=missing(df,['Model','Brand','VehicleType','RegistrationYear'],'Gearbox')

  df.loc[(df['VehicleType'].isna())&(-df['Gearbox'].isna())&(-df['RegistrationYear'].isna())&
                    (-df['Brand'].isna())&(-df['Model'].isna()),'VehicleType']=missing(df,['Gearbox','Brand','Model','RegistrationYear'],'VehicleType')

  df.loc[(df['FuelType'].isna())&(-df['Gearbox'].isna())&(-df['RegistrationYear'].isna())&
                    (-df['Brand'].isna())&(-df['Model'].isna()),'FuelType']=missing(df,['Gearbox','Brand','Model','RegistrationYear'],'FuelType')


  df['FuelType']=df.groupby(['Brand','RegistrationYear','Model'])['FuelType'].apply(lambda x: x.ffill().bfill())
  df['VehicleType']=df.groupby(['Brand','Model','RegistrationYear'])['VehicleType'].apply(lambda x: x.ffill().bfill())
  df['Gearbox']=df.groupby(['Brand','Model','RegistrationYear'])['Gearbox'].apply(lambda x: x.ffill().bfill())

  df=df.dropna()
  df=df.drop_duplicates()

  df['how_long']=(df['LastSeen']-df['DateCreated']).astype('timedelta64[D]')

  df['year_created']=(pd.DatetimeIndex(df['DateCreated']).year).astype("category")

  df['month_created']=pd.DatetimeIndex(df['DateCreated']).month.astype("category")

  df['Repaired']=np.where(df['Repaired']=='yes',1,0)
  for i in ['RegistrationYear','FuelType','Repaired']:
      df[i]=df[i].astype("category")


  df=df.drop(['DateCrawled','RegistrationMonth','DateCreated','LastSeen','NumberOfPictures'],axis=1)
  df=df.drop_duplicates()

  for column in df.columns:
      counts = df[column].value_counts()  
      categories_to_keep = counts[counts > 10].index  
      df = df[df[column].isin(categories_to_keep)] 


  features=df.drop(['Price','how_long','year_created', 'month_created'],axis=1)
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

  light=(study(features_train,target_train,{'selection__k': [3, 6, 10],'model__learning_rate': [0.01, 0.1, 1],'model__num_leaves': [32, 64, 128],'model__max_depth': [4, 6, 8]},LGBMRegressor()))
  return features,light


features_df, trained_model = load_and_preprocess_data()

st.write('Модель загруженна')




language = ['RUS', 'ENG']
selected_variation = st.selectbox('Выберите язык/Choose language', language)

# Depending on the selected language, show different UI text
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

# Initialize a new DataFrame for storing user's selections
user_df = pd.DataFrame(columns=all_columns)

for i, column in enumerate(all_columns):
    if features_df[column].dtypes=='category':
        unique_values = features_df[column].unique().tolist()
        
        # Create a selectbox for each column
        selected_value = st.selectbox(f'{input_label} {column}', unique_values, key=column)
        
        # Filter the DataFrame based on the selected value for the next selectboxes
        features_df = features_df[features_df[column] == selected_value]

        # Store the selected value
        selected_values[column] = selected_value
        
    elif pd.api.types.is_numeric_dtype(features_df[column]):
        numeric_value = st.text_input(f"{input_label} {column}", key=column)
        if numeric_value:
            try:
                numeric_value = float(numeric_value)
                selected_values[column] = numeric_value
            except ValueError:
                st.error(f"{error_message} {column}")

    # Adding the case for 'PostalCode'
    elif column == 'PostalCode':
        postal_code = st.text_input(f"{input_label} PostalCode", key='PostalCode')
        selected_values[column] = str(postal_code)

# Add a confirmation checkbox
if st.checkbox(confirmation_text):
    # Add the user's selections to the new DataFrame
    user_df = user_df.append(selected_values, ignore_index=True)

    # Show the user's selections DataFrame
    st.dataframe(user_df)
    st.write(f'Стоимость вашей машины : {np.round(*trained_model.predict(user_df),2)} EUR')

