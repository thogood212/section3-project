from selenium import webdriver
import requests
import time
from bs4 import BeautifulSoup

browser = webdriver.Chrome("/Users/damon/section3_project/chromedriver")
#창 최대화
browser.maximize_window()

#페이지 이동
url = "https://tumblbug.com/discover?sort=publishedAt"
browser.get(url)

time.sleep(2)

browser.execute_script("window.scrollTo(0,1080)")
soup = BeautifulSoup(browser.page_source, "html.parser")



#items = soup.find_all("div", attrs={"class":"InfinityList__ProjectCardWrapper-sc-19jay7c-4 jfWeNA"})
#items = soup.find_all("div", attrs={"class":"InfinityList__ListWrapper-sc-19jay7c-3 fZWVhg"})
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

for object in url_address :
    item_url=object
    page = requests.get(item_url)
    soup = BeautifulSoup(page.content, "html.parser")
    category = soup.find("span", attrs={"class":"ProjectIntroduction__ProjectCategory-sc-1o2ojgb-4 jXHjuM"}).text
    curr_pirce = soup.find("div", attrs= {"class":"ProjectIntroduction__StatusValue-sc-1o2ojgb-16 irdmAh"})
    target_value = soup.find("span", attrs={"class":"ProjectIntroduction__FundingRate-sc-1o2ojgb-17 YubsY"})
    
    browser.get(item_url)
    browser.execute_script("window.scrollTo(0,1080)")   
    time.sleep(1)
    soup= BeautifulSoup(browser.page_source,"html.parser")

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

    print(f"현재 모인 금액 : {curr_pirce}")
    print(f"목표 충족 퍼센트 : {target_value}")
    print(f"카테고리 : {category}")
    print(f"후원금액1 : {reward_price1}")
    print(f"후원금액2 : {reward_price2}")
    print(f"제품 소개 글자수 : {text_length}")
    print("-"*100)

browser.quit()