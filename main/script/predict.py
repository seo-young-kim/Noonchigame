
def castleInfo():
    import pandas as pd
    import joblib
    model =joblib.load('/app/main/script/data/castle.pkl')
    df=pd.read_json('/app/main/script/data/10days.json',orient='table')
    #print(df)

    df['month']= df['date'].dt.month
    df['weekday']=df['date'].dt.weekday
    df['day']=df['date'].dt.day
    df['min_temp']=df['min_temp'].astype(int)
    df['max_temp']=df['max_temp'].astype(int)
   # print(df.info())
    df['temp']=(df['min_temp']+df['max_temp'])/2

    X = df[['month','weekday','holiday','culture','nightOpen','temp','cloud','rain']]
    df['result'] = model.predict(X).astype(int)
    df.rename({'img':'weather_img'},axis=1,inplace=True)
    df['weekday']=df['weekday'].apply(week)
    #print(result.astype(int))
    
    #weekdic = {0:'mon',1:'tue',2:'wen',3:'thu',4:'fri',5:'sat',6:'sun'}
    
    column = ['month','weekday','result','day','holiday','min_temp','max_temp','rain_morning','rain_afternoon','weather_img']
    
    df['rain_morning']=df['rain']
    df['rain_afternoon']=df['rain']
    
    
   # /* 이제 columns을 key로 갖는 dict 만 생성해서 return
    
    dic = {}
    for col in column:
        dic[col]=df[col].tolist()
    print(dic)
    return dic

def week(num):
    weekdic = {0:'MON',1:'TUE',2:'WEN',3:'THU',4:'FRI',5:'SAT',6:'SUN'}
    return weekdic[num]
castleInfo()
