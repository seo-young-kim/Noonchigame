
def castleInfo():
    import pandas as pd
    import joblib
    model =joblib.load('/app/main/script/data/castle.pkl')
    df=pd.read_json('/app/main/script/data/10days.json',orient='table')
    #print(df)

    df['month']= df['date'].dt.month
    df['weekday']=df['date'].dt.weekday
    df['min_temp']=df['min_temp'].astype(int)
    df['max_temp']=df['max_temp'].astype(int)
   # print(df.info())
    df['temp']=(df['min_temp']+df['max_temp'])/2
    X = df[['month','weekday','holiday','culture','nightOpen','temp','cloud','rain']]
    df['result'] = model.predict(X).astype(int)
    #print(result.astype(int))
    
    #weekdic = {0:'mon',1:'tue',2:'wen',3:'thu',4:'fri',5:'sat',6:'sun'}
    
    column = ['month','weekday','result','day','holiday','min_temp','max_temp','rain_morning','rain_afternoon','weather_img']
    data = pd.DataFrame(columns=column)
    data['month']=df['month']
    data['result']=df['result']
    data['day']=df['date'].dt.day
    data['holiday']=df['holiday']
    data['min_temp']=df['min_temp']
    data['max_temp']=df['max_temp']    
    data['rain_morning']=df['rain']
    data['rain_afternoon']=df['rain']
    data['weather_img']=df['img']
    data['weekday']=df['weekday'].apply(week)
    print(data.to_dict())
    return data.to_dict()

def week(num):
    weekdic = {0:'MON',1:'TUE',2:'WEN',3:'THU',4:'FRI',5:'SAT',6:'SUN'}
    return weekdic[num]
castleInfo()
