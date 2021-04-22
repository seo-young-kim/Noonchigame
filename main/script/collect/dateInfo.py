# In dateInfo file, collect holliday info and culture day info
# collects and returns information for 10 days from today.


import numpy as np
from datetime import datetime
from datetime import timedelta
import pandas as pd


#1. culture day
# if day is culture day, return 1
def isCulture(day):
    nextweek = day + timedelta(days=7)
    if day.weekday()==2 and nextweek.month!=day.month:
        return 1
    else :
        return 0

#return series that contains culture info for 10 days from today
def culture(series):
    return series.apply(lambda x: isCulture(x))


#2. holiday
#return array that contains holiday info for 10 days from today
def holiday(today):
    candidate = candidateHoliday(today)
    #today
    holidays = [h['date'] for h in candidate]
    holiday = []
    for i in range(10):
        day = datetime.now()+timedelta(days=i)
        daystr = str(day.year) 
        daystr += str(day.month) if day.month>=10 else '0'+str(day.month)
        daystr += str(day.day) if day.day>=10 else '0'+str(day.day)
        holiday.append(1 if daystr in holidays else 0)
        
    return holiday

def candidateHoliday(today):
    #API
    response = get_request_query(today)
    #
    holidayinfo = xmlTolist(response.text)
    #10
    month = today.month
    monthAfter10days = (today+timedelta(days=10)).month
    if month!=monthAfter10days:
        response = get_request_query(today+timedelta(days=10))
        holidayinfo+=xmlTolist(response.text)
    return holidayinfo

def xmlTolist(xmldata):
    from xml.etree import ElementTree
    root = ElementTree.fromstring(xmldata)
    holiday = []
    for element in root.iter(tag = 'item'):
        hdict = {}
        hdict['name']=element.find('dateName').text
        hdict['date']=element.find('locdate').text
        holiday.append(hdict)

    return holiday

def get_request_query(today):
    import requests
    import urllib.parse as urlparse
    url = 'http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService'
    operation = 'getHoliDeInfo'
    myKey = 'qpSSoqsY2Nv4ybDAUZbVRFyu0%2F8QLNOPvNoPK7UT0z52ZqwaBNWE94zDlQClIH1DDZ8n7crjwWC%2B2tn9n1M6AQ%3D%3D'
            
    month = str(today.month) if today.month>=10 else '0'+str(today.month)
    solYear  = str(today.year)
    solMonth = month
    params = {'solYear':solYear, 'solMonth':solMonth}

    params = urlparse.urlencode(params)
    request_query = url + '/' + operation + '?' + params + '&' + 'serviceKey' + '=' + myKey
    return requests.get(url=request_query)
