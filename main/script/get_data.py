"""
It is a script that provide information over the next 10 days to __init__.py.

castleInfo : function that returns the information that provided by the predict_castle.html 
1. Read the updated information from the data Folder.
2. Return the information you need to the dictionary.

"""

def castleInfo():
    import pandas as pd
    df=pd.read_json('/app/main/script/data/10days.json',orient='table')

    # rename & encoding
    df.rename({'img':'weather_img'},axis=1,inplace=True)
    df['weekday']=df['weekday'].apply(week)
    
    #provide information
    column = ['month','weekday','result','day','holiday','min_temp','max_temp','rain_morning','rain_afternoon','weather_img']
    df['rain_morning']=df['rain']
    df['rain_afternoon']=df['rain']
    
    #columns을 key로 갖는 dic return
    dic = {}
    for col in column:
        dic[col]=df[col].tolist()
    print(dic)
    return dic

def week(num):
    weekdic = {0:'MON',1:'TUE',2:'WEN',3:'THU',4:'FRI',5:'SAT',6:'SUN'}
    return weekdic[num]

castleInfo()
