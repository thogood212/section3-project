from selenium import webdriver

browser = webdriver.Chrome("/Users/damon/section3_project/chromedriver")

browser.get("http://naver.com")

#페이지에서 클릭하기
#elem = browser.find_element_by_class_name("") #링크 변수 만들기
#elem
#elem.click() # 클릭해서 들어가기
#browser.back() #뒤로가기
#browser.forward() #엎으로 가기
#browser.refresh() #새로고침

#페이지에 값 입력하기
#elem = browser.find_element_by_id("")
#elem
#from selenium.webdriver.common.keys import keys #keys.ENTER를 위한 임포트
#elem.send_keys("")
#elem.send_keys(keys.ENTER) #엔터치고 들어가기
#그외의 방법
#elem = browser.find_element_by_xpath("검색버튼 path copy해서 붙여넣기")
#elem.click() 하면 검색결과로 넘어감

#elem= browser.find_elements_by_id("") # 여러가지 요소 가져오기 
#for e in elem :
#    e.get_attribute("찾는값")

#결과 출력
#elem = browser.find_element_by_xpath("")
#print(elem.text)

#로딩 
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import webDriverWait
#from selenium.webdriver.support import expected_conditions as EC

#10초동안 element가 불러와질때까지 기다려보고 그전에 불러와지면 바로 실행한다.
#try :
#elem - webDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,"xpath주소")))
#print(elem.text)
#finaaly:
# browser.quit()



