from selenium import webdriver
import requests
import time
from bs4 import BeautifulSoup
import sqlite3

#sqlite 데이터베이스에서 url 정보 불러오기
conn= sqlite3.connect("/Users/damon/section3_project/tumblbug.db")
cur = conn.cursor()

#curr_price : 모인 금액
#target_per : 모인 금액 퍼센트
#target_price : 목표 금액
#category : 프로젝트 분야
#text_length : 소개글 글자 수
#reward_price1 : 후원 요청 금액
#reward_price2 : 후원 요청 금액
#target : 펀딩 성공여부 (0:실패, 1:성공)


#cur.execute("DROP TABLE IF EXISTS tumblbug;")

#데이터 저장할 테이블 생성
#cur.execute("""CREATE TABLE tumblbug (
#    curr_price INTEGER,
#    curr_per INTEGER ,
#    target_price INTEGER,
#    category TEXT,
#    text_length INTEGER,
#    reward_price1 INTEGER,
#    reward_price2 INTEGER,
#    target INTEGER);""")

url_list = cur.execute("""SELECT * FROM ADDRESS ORDER BY random() LIMIT 3000""")
url_address = url_list.fetchall()

#headless_chrome
options= webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
#browser = webdriver.Chrome("/Users/damon/section3_project/chromedriver",options=options)


#url정보 하나씩 접속해서 데이터 모으기
for item_url in url_address :
    browser = webdriver.Chrome("/Users/damon/section3_project/chromedriver",options=options)
    browser.maximize_window()
    browser.get(item_url[0])
    browser.execute_script("window.scrollTo(0, 1080)")

    time.sleep(3)

    print(item_url[0])

    soup= BeautifulSoup(browser.page_source,"html.parser")
    try :
        category = soup.find("span", attrs={"class":"ProjectIntroduction__ProjectCategory-sc-1o2ojgb-4 jXHjuM"}).text
        curr_price = soup.find("div", attrs= {"class":"ProjectIntroduction__StatusValue-sc-1o2ojgb-16 irdmAh"}).get_text().split('원')[0]
        curr_per = soup.find("span", attrs={"class":"ProjectIntroduction__FundingRate-sc-1o2ojgb-17 YubsY"}).get_text()
        #target_per = int(target_value.replace('%',''))
        curr_price = int(curr_price.replace(',',''))
        curr_per = int(curr_per.replace('%',''))

        #글자수 세기
        p = soup.find_all("p")
        lens =[]
        for s in p:
            text = len(s.get_text())
            lens.append(text)
        text_length = sum(lens)

        #target 값 설정
        if curr_per >= 100 :
            target = '1'
        else :
            target = '0'
        
        target_price = int(curr_price/curr_per*100)

        #후원금 값 찾기
        try :
            price = soup.find_all("div",attrs={"class":"RewardCard__RewardMinimumPledgeAmount-sc-11jni8b-11 hcaxjL"})
            price_list=[]
            for i in price:
                price_list.append(i.get_text().split('원')[0])
            reward_price1 = int(price_list[1].replace(',',''))
            reward_price2 = int(price_list[2].replace(',',''))
        except :
            reward_price1 = None
            reward_price2 = None
        

        #print(f"현재 모인 금액 : {curr_price}")
        #print(f"목표 충족 퍼센트 : {curr_per}")
        #print(f"목표 금액 : {target_price}")
        #print(f"카테고리 : {category}")
        #print(f"후원금액1 : {reward_price1}")
        #print(f"후원금액2 : {reward_price2}")
        #print(f"제품 소개 글자수 : {text_length}")
        #print(f"목표 달성 여부 : {target}")
        #print("-"*100)
        
        browser.quit()
        
        cur.execute("""INSERT INTO tumblbug (curr_price,curr_per,target_price,category,text_length,reward_price1,reward_price2,target)
            VALUES (?,?,?,?,?,?,?,?)""", (curr_price,curr_per,target_price,category,text_length,reward_price1,reward_price2,target))
        conn.commit()

    except :
        print("오류발생")
        browser.quit()