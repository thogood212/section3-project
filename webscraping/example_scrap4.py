from selenium import webdriver
import sqlite3
import time
from bs4 import BeautifulSoup

##headless_chrome
#options= webdriver.ChromeOptions()
#options.headless = True
#options.add_argument("window-size=1920x1080")
#browser = webdriver.Chrome("/Users/damon/section3_project/chromedriver",options=options)

browser = webdriver.Chrome("/Users/damon/section3_project/chromedriver")

#창 최대화
browser.maximize_window()

#페이지 이동
url = "https://tumblbug.com/discover?sort=publishedAt"
browser.get(url)

time.sleep(2)
# 지정한 위치로 스크롤 내리기
# 모니터(해상도) 높이인 1080 위치로 스크롤 내리기
#browser.execute_script("window.scrollTo(0,1080)")


browser.execute_script("window.scrollTo(0,1080)")

print('스크롤 완료')

soup = BeautifulSoup(browser.page_source, "html.parser")
items = soup.find_all("dt")

url_address=[]

#링크주소 리스트 만들기
for item in items :
    link = item.find("a")['href']
    link = "https://tumblbug.com"+link
    #print(f"링크 :", "https://tumblbug.com"+link)
    url_address.append(link)

print(url_address)
browser.quit()

conn= sqlite3.connect("/Users/damon/section3_project/tumblebug.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS ADDRESS;")

cur.execute("""CREATE TABLE ADDRESS (
    url VARCHAR NOT NULL);""")

for i in url_address :
    cur.execute("INSERT INTO ADDRESS (url) VALUES (?)", [i])
conn.commit()
