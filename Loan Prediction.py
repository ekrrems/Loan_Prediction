
# Importing packages 
import math
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score


data = pd.read_csv('C:\\Users\\ekrem\\OneDrive\\Masaüstü\\Machine learning DATAS\\loan_prediction_dataset.csv')
df = data.copy()
df.head()

df.info()

def change_objects():
    df['Gender']=df['Gender'].replace(['Male','Female'],[int(1),int(0)])
    df['Married']=df['Married'].replace(['Yes','No'],[int(1),int(0)])
    df['Education']=df['Education'].replace(['Graduate','Not Graduate'],[int(1),int(0)])
    df['Self_Employed']=df['Self_Employed'].replace(['Yes','No'],[int(1),int(0)])
    df['Loan_Status']=df['Loan_Status'].replace(['Y','N'],[int(1),int(0)])
    df['Property_Area']=df['Property_Area'].replace(['Semiurban','Urban','Rural'],[int(0),int(1),int(2)])


change_objects()

df.drop(['Loan_ID','Dependents'],axis=1,inplace=True)
df.dropna(inplace=True)

# Visualizing Data

df['Loan_Status'].value_counts().plot.bar()

sns.barplot(x='Gender',y='LoanAmount',hue='Married',data=df)

sns.scatterplot(x='ApplicantIncome',y='LoanAmount',hue='Property_Area',data=df)

sns.lmplot(x='ApplicantIncome',y='LoanAmount',data=df)

sns.distplot(df['CoapplicantIncome'])

df.groupby('Loan_Status')['ApplicantIncome'].mean().plot.bar()

sns.heatmap(df.corr(),annot=True)
# Modeling

X = df.drop('LoanAmount',axis=1)
y = df['LoanAmount']

X_train ,X_test ,y_train,y_test = train_test_split(X,y,test_size=0.2,
                                                   random_state=42)

#LinearRegression,Lasso
#DecisionTreeRegressor
#SVR
#RandomForestRegressor

models = []

def models_append():
    models.append(('LR',LinearRegression()))
    models.append(('DTR',DecisionTreeRegressor()))
    models.append(('Lasso',Lasso()))
    models.append(('SVR',SVR()))
    models.append(('RFR',RandomForestRegressor()))

models_append()



    
for name,model in models:
    print('***********************')
    model.fit(X_train,y_train)
    prediction = model.predict(X_test)
    print("{}'s MSE:{}".format(name,mean_squared_error(y_test,prediction)))
    print("{}'s RMSE:{}".format(name,math.sqrt(mean_squared_error(y_test,prediction))))
    print("{}'s MAE:{}".format(name,mean_absolute_error(y_test,prediction)))
    print("{}'s R2 Score:{}".format(name,r2_score(y_test,prediction)))
    print('***********************')
    

    
    
    
    











