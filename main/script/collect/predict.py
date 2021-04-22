import dateInfo
import weatherInfo
import pandas as pd
import numpy as np
from datetime import datetime
from datetime import timedelta

#collect data for 10 days from today for predict
feature = ['date','holiday','min_temp','max_temp','rain','cloud','nightOpen','culture','img','wind']
df = pd.DataFrame(columns=feature)

#date
df['date']=[datetime.now()+timedelta(days=i) for i in range(10)]
#night Open =0 because of covid19
df['nightOpen']=0

#culture
df['culture']=dateInfo.culture(df['date'])

#print(df)

df['holiday']=dateInfo.holiday(datetime.now())

print(df)

dic = weatherInfo.crawling()
print(dic)

for key in dic.keys():
    df[key]=dic[key]

#collect weather data
print(df)
