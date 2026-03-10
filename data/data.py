import pandas as pd
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()

import json
df=pd.read_excel("churn.xlsx")
##print(df.columns)
y=df["Churn Value"]
y.to_csv("lab.csv",index=False)
##
##fol=df[['Tenure Months','Total Charges']]
##
##df[['Tenure Months','Total Charges']]=df[['Tenure Months','Total Charges']].apply(pd.to_numeric,errors='coerce')
##df[['Tenure Months','Total Charges']]=df[['Tenure Months','Total Charges']].fillna(0)
##
##df[['Tenure Months','Total Charges']]=scaler.fit_transform(df[['Tenure Months','Total Charges']])
##print(df.shape)
##col=['CustomerID','Churn Label','Churn Score','Zip Code',
##     'Count','Churn Reason','Country', 'State', 'City',
##       'Lat Long', 'Latitude', 'Longitude','Churn Value', 'CLTV','Monthly Charges']
##encoding={'No':0, 'Yes':1, 'No internet service':0,'Male':1 ,'Female':0,
##          'No phone service':0}
##colsi=['Gender','Senior Citizen','Partner',
##       'Dependents','Phone Service','Multiple Lines',
##       'Online Security','Online Backup','Device Protection',
##       'Tech Support','Streaming TV',
##       'Streaming Movies','Paperless Billing']
##df[colsi]=df[colsi].replace(encoding)
##df=pd.get_dummies(df,columns=['Internet Service','Contract','Payment Method'],drop_first=True,dtype=int)
##
##
##gf=df.drop(columns=col)
##print(gf.shape,gf.columns)
##for col in gf.columns:
##    print(f"{col}: {df[col].unique()}")
##gf.to_csv("p1.csv",index=False)
