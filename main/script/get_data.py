"""
It is a script that provide information over the next 10 days to __init__.py.

castleInfo : function that returns the information that provided by the predict_castle.html 
1. Read the updated information from the data Folder.
2. Return the information you need to the dictionary.

"""

def castleInfo():
    import pandas as pd
    import sys
    import logger
    #10days.json을 읽을 수 없는 경우
    try:
        df=pd.read_json('/app/main/script/data/10days.json',orient='table')
    except:
        logger.error("Can't Read 10days.json",sys.exc_info())
        return ""
    #아직  업데이트 되지 않은 경우
    #오늘 날짜부터 10일인지 확인
    # 그렇지 않다면 log를 남긴다.
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
