import pandas as pd
import numpy as np
from datetime import datetime
from datetime import timedelta
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

"""
collect weather data for 10 days from today
temp, rain, cloud,wind 


"""

def path(src):
    img_path={'https://www.weatheri.co.kr/images/icon_2013_01/01.png':1,
            'https://www.weatheri.co.kr/images/icon_2013_01/02.png':2,
            'https://www.weatheri.co.kr/images/icon_2013_01/18.png':3,
            'https://www.weatheri.co.kr/images/icon_2013_01/21.png':4,
            'https://www.weatheri.co.kr/images/icon_2013_01/03.png':6,
            'https://www.weatheri.co.kr/images/icon_2013_01/13.png':7,
            'https://www.weatheri.co.kr/images/icon_2013_01/07.png':8,
            'https://www.weatheri.co.kr/images/icon_2013_01/04.png':10,
            'https://www.weatheri.co.kr/images/icon_2013_01/16.png':5,
            'https://www.weatheri.co.kr/images/icon_2013_01/11.png':5}
    return img_path[src]
#df = pd.DataFrame(columns=['rain','cloud','max_temp','min_temp']);
def crawling():
    options = Options()
    options.headless = True
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome('./chromedriver',options=options)
    driver.get("http://www.weatheri.co.kr/forecast/forecast01.php?rid=0101010000&k=1&a_name=%EC%84%9C%EC%9A%B8")
    driver.implicitly_wait(5)

    dic = {'day':[],'rain':[],'max_temp':[],'min_temp':[],'wind':[],'cloud':[],'img':[]}
    for k in [2,8]:
        for i in range(1,6):
            day=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table["+str(k)+"]/tbody/tr[1]/td["+str(i)+"]/b")
            rain=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table["+str(k)+"]/tbody/tr[2]/td["+str(i)+"]/table/tbody/tr[4]/td[2]/font")
            cloud=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table["+str(k)+"]/tbody/tr[2]/td["+str(i)+"]/table/tbody/tr[2]/td[1]/img")
            temp_max=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table["+str(k)+"]/tbody/tr[2]/td["+str(i)+"]/table/tbody/tr[2]/td[2]/b/font")
            temp_min=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table["+str(k)+"]/tbody/tr[2]/td["+str(i)+"]/table/tbody/tr[2]/td[2]/b/b/font")
            wind = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table["+str(k)+"]/tbody/tr[2]/td["+str(i)+"]/table/tbody/tr[4]/td[1]/font")
            dic['day'].append(day.text)
            rain_text = rain.text[0:len(rain.text)-3]
            dic['rain'].append(0 if rain_text=='-' else float(rain_text))
            #print(cloud.get_attribute('src'))
            dic['cloud'].append(int(path(cloud.get_attribute('src'))))
            dic['img'].append(cloud.get_attribute('src')[46:])
            dic['max_temp'].append(temp_max.text[0:len(temp_max.text)-2])
            dic['min_temp'].append(temp_min.text[0:len(temp_min.text)-2])
            dic['wind'].append(float(wind.text[0]))
    
    driver.close(); 
    return dic

def naver():
    options = Options()
    options.headless = True
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome('./chromedriver',options=options)    
    url="https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%9A%B8+%EC%A4%91%EA%B5%AC+%EB%82%A0%EC%94%A8+%EC%98%88%EB%B3%B4&oquery=%EC%84%9C%EC%9A%B8+%EA%B2%BD%EB%B3%B5%EA%B6%81+%EB%82%A0%EC%94%A8+%EC%98%88%EB%B3%B4&tqi=UTZOLdprvmZssm86d30ssssssLl-490215"
    driver.get(url)
    driver.implicitly_wait(5) 
                        #/html/body/div[3]/div[2]/div/div[1]/section[2]/div/div[2]/div[2]/div[1]/div[7]/ul[2]
    next_weather = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/section[2]/div/div[2]/div[2]/div[1]/div[7]/ul[2]")

                    
    dic = {'morning':[],'afternoon':[]}
    for k in range(1,3):
        if k==2:
            bttn = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/section[2]/div/div[2]/div[2]/div[1]/div[7]/div[2]/div/a[2]/span")
            bttn.Click()
        for i in range(1,6):
            
            morning=driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/section[1]/div/div[2]/div[2]/div[1]/div[7]/ul["+str(k)+"]/li["+str(i)+"]/span[2]/span[2]/span[2]")
            afternoon=driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/section[1]/div/div[2]/div[2]/div[1]/div[7]/ul["+str(k)+"]/li["+str(i)+"]/span[3]/span[2]/span[2]")
            print(morning.text)
            print(afternoon.text)
            dic['morning'].append(morning.text)
            dic['afternoon'].append(afternoon.text)

    driver.close()
    return dic


#print(naver())
