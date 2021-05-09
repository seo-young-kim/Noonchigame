import dateInfo as dateInfo
import weatherInfo as weatherInfo
import pandas as pd
import numpy as np
import joblib
from datetime import datetime
from datetime import timedelta

import sys
sys.path.append("..")
from logger import makelog
"""
Create DataFrame for 10 days from today

feature = ['date','holiday','min_temp','max_temp','rain','cloud','nightOpen','culture','img','wind']
"""
logger = makelog("seoykim")
import time
time0=time.time()
print(time0)
from flask import Flask,request,render_template
df = pd.DataFrame()

"""
date
"""
df['date']=[datetime.now()+timedelta(days=i) for i in range(10)]
df['month']= df['date'].dt.month
df['weekday']=df['date'].dt.weekday

"""
night Open =0 because of covid19
"""

df['nightOpen']=0

"""
culture&holiday
"""
df['culture']=dateInfo.culture(df['date'])
df['holiday']=dateInfo.holiday(datetime.now())

#print(df)
"""
weather
"""
weather = weatherInfo.crawling()
for key in weather.keys():
    df[key]=weather[key]

"""
engineering feature
"""
df['min_temp']=df['min_temp'].astype(int)
df['max_temp']=df['max_temp'].astype(int)
df['temp']=(df['min_temp']+df['max_temp'])/2
df['day']=df['date'].dt.day
#print(df)

"""
predict by castle.pkl
"""
model =joblib.load('/app/main/script/data/castle.pkl')
X = df[['month','weekday','holiday','culture','nightOpen','temp','cloud','rain']]
df['result'] = model.predict(X).astype(int)
print(df)


#store
df.to_json('/app/main/script/data/10days.json',orient='table')

print(time.time())
print(time.time()-time0)
logger.info(time.time()-time0)

