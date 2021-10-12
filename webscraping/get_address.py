from selenium import webdriver
import requests
import time
from bs4 import BeautifulSoup
import sqlite3
import time

#headless_chrome
#options= webdriver.ChromeOptions()
#options.headless = True
#options.add_argument("window-size=1920x1080")
#browser = webdriver.Chrome("/Users/damon/section3_project/chromedriver",options=options)

browser = webdriver.Chrome("/Users/damon/section3_project/chromedriver")

#창 최대화
#browser.maximize_window()

#페이지 이동(분야별로 지정)#게임,연극,디자인,만화,예술,공예,사진,영화비디오,푸드,음악,테크,저널리즘,출판,
#url = "https://tumblbug.com/discover?sort=publishedAt"
url = "https://tumblbug.com/discover?category=fashion&sort=publishedAt"
browser.get(url)

# 지정한 위치로 스크롤 내리기
# 모니터(해상도) 높이인 1080 위치로 스크롤 내리기
#browser.execute_script("window.scrollTo(0,1080)")

# 화면 가장 아래로 스크롤 내리기
#browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")


interval = 2 # 2초에 한번씩 스크롤 내림

#현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

#반복 수행
while True :
    #스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, -100)")
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    #페이지 로딩 대기
    time.sleep(interval)

    #현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")

    if prev_height == curr_height:
        browser.execute_script("window.scrollTo(0, -100)")
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        #browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        #time.sleep(interval)
        #browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        if prev_height == curr_height:
            browser.execute_script("window.scrollTo(0, -100)")
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            if prev_height == curr_height:
                break
            prev_height = curr_height
        prev_height = curr_height
    prev_height = curr_height

print('스크롤 완료')

time.sleep(3)

#주소 저장하기
soup = BeautifulSoup(browser.page_source, "html.parser")
items = soup.find_all("dt")

url_address=[]

#링크주소 리스트 만들기
for item in items :
    link = item.find("a")['href']
    link = "https://tumblbug.com"+link
    #print(f"링크 :", "https://tumblbug.com"+link)
    url_address.append(link)

browser.quit()

conn= sqlite3.connect("/Users/damon/section3_project/tumblbug.db")
cur = conn.cursor()

#cur.execute("DROP TABLE IF EXISTS ADDRESS;")

#cur.execute("""CREATE TABLE ADDRESS (
#    url VARCHAR NOT NULL PRIMARY KEY);""")

for i in url_address :
    cur.execute("INSERT INTO ADDRESS (url) VALUES (?)", [i])
conn.commit()
