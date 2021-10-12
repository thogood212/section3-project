from selenium import webdriver
import requests
import time
from bs4 import BeautifulSoup

#browser = webdriver.Chrome("/Users/damon/section3_project/chromedriver")
#창 최대화

browser = webdriver.Chrome("/Users/damon/section3_project/chromedriver")
browser.maximize_window()
#페이지 이동
url_address = 'https://tumblbug.com/thecornerofaroom?ref=discover'
#url_address = ['https://tumblbug.com/badworkers?ref=discover', 'https://tumblbug.com/newmoonproject?ref=discover', 'https://tumblbug.com/chogwa?ref=discover', 'https://tumblbug.com/betheflowring?ref=discover', 'https://tumblbug.com/filmcase?ref=discover', 'https://tumblbug.com/thecornerofaroom?ref=discover', 'https://tumblbug.com/icewinenectarine?ref=discover', 'https://tumblbug.com/yoyo?ref=discover']


browser.get(url_address)
browser.execute_script("window.scrollTo(0,1080)")

time.sleep(2)

soup= BeautifulSoup(browser.page_source,"html.parser")
category = soup.find("span", attrs={"class":"ProjectIntroduction__ProjectCategory-sc-1o2ojgb-4 jXHjuM"}).text
curr_pirce = soup.find("div", attrs= {"class":"ProjectIntroduction__StatusValue-sc-1o2ojgb-16 irdmAh"}).get_text().split('원')[0]
target_value = soup.find("span", attrs={"class":"ProjectIntroduction__FundingRate-sc-1o2ojgb-17 YubsY"}).get_text()
target_value = int(target_value.replace('%',''))
            #글자수 세기
p = soup.find_all("p")
lens =[]
for s in p:
    text = len(s.get_text())
    lens.append(text)
text_length = sum(lens)

            #후원금 값 찾기
price = soup.find_all("div",attrs={"class":"RewardCard__RewardMinimumPledgeAmount-sc-11jni8b-11 hcaxjL"})
price_list=[]
for i in price:
    price_list.append(i.get_text().split('원')[0])
reward_price1 = int(price_list[1].replace(',',''))
reward_price2 = int(price_list[2].replace(',',''))
            
            #target 값 설정
if target_value >= 100 :
    target = '1'
else :
    target = '0'
            
print(f"현재 모인 금액 : {curr_pirce}")
print(f"목표 충족 퍼센트 : {target_value}")
print(f"카테고리 : {category}")
print(f"후원금액1 : {reward_price1}")
print(f"후원금액2 : {reward_price2}")
print(f"제품 소개 글자수 : {text_length}")
print(f"목표 달성 여부 : {target}")
print("-"*100)
            
browser.quit()

