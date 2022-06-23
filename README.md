# 리워드형 크라우드 펀딩 텀블벅 기반으로 펀딩 성공확률 예측 프로젝트

![텀블벅](https://user-images.githubusercontent.com/87019897/175299171-8c4f9ffb-7296-4faa-b0d2-b462e698acdd.png)

## ✔️ 개요

- 리워드형 크라우드 펀딩 프로젝트를 시작하고 싶을 때, 사용자가 준비한 프로젝트로 성공할 수 있을지 몇가지 선택지를 통하여 간단히 확인할 수 있는 서비스
- 데이터 출처  : 웹 크롤러를 제작하여 `텀블벅` 에서 `크라우드 펀딩 성공,실패 데이터` 수집
- 수집한 URL을 하나씩 접속하여 특정 데이터(총 펀딩 금액, 펀딩 금액 퍼센트, 목표 금액, 소개글 글자수, 후원 금액1,2)을 특정하여 관계형 DB(Sqlite3)에 저장

## ✔️ 프로젝트 내용

### 문제 인식

- 리워드형 크라우드펀딩의 경우, 기업이 아닌 **개인이 아이디어를 현실화할 수 있는 시스템**입니다. 그러나 한국에서는 기업에서 이용하는 경우가 대부분이고 개인이 성공시킨 프로젝트는 많지가 않습니다. 이러한 점을 쇄신하고자 개인이 크라우드펀딩 시작의 **편의성을 높혀 개인의 참여를 제고**해야 합니다.

### **데이터 수집 및 분석(EDA)**

- 텀블벅 사이트에서 크라우드펀딩 데이터 수집
- 총 펀딩 금액, 펀딩 금액 퍼센트, 목표 금액, 소개글 글자수, 후원 금액1,2 을 추출하여 METABASE를 사용하여 EDA 실행
![1](https://user-images.githubusercontent.com/87019897/175299535-61a66387-2b83-4bcd-85ed-343f92c81848.png)
![2](https://user-images.githubusercontent.com/87019897/175299693-5bc57d83-e6e8-419f-aac5-6c5e30c5b6cd.png)
![3](https://user-images.githubusercontent.com/87019897/175299704-fc051714-ee01-452b-b7f2-b2417f6a0780.png)
![4](https://user-images.githubusercontent.com/87019897/175299712-0b0e42f0-78e0-4b8a-8a47-2300c5cb400c.png)
![5](https://user-images.githubusercontent.com/87019897/175299719-cf9f6178-8c4f-4f02-aa6a-c5158541c248.png)


## ✔️ 데이터 모델링

![6](https://user-images.githubusercontent.com/87019897/175299883-74b4f4c7-d47f-49e2-979b-a4232843944c.png)

- 간단한 머신러닝(RandomForestClassifier)를 사용하여 수집한 데이터를 가지고 훈련하여 모델을 저장합니다.
- Flask를 사용하여 저장한 모델을 불러와 목표 금액, 소개글 글자수, 후원 금액, 카테고리를 선택하고 클릭 시 다른 페이지에서 성공확률을 표현해주는 웹어플리케이션 구현

## ✔️ 프로젝트 결과

아래 그림에서 확인할 수 있듯이 리워드형 크라우드 펀딩을 시작할 경우 소비자가 확인하게 되는 몇가지 사항을 가지고 펀딩에 대한 대략적인 정보를 얻을 수 있습니다.
크라우드펀딩 기업에서 제공하는 전문적인 시스템 이전에 사용하여 현직자의 업무 강도를 낮추면서 펀딩을 시작하는 사용자에게는 직관적이고 쉬운 접근 방식을 통해 참여를 제고할 수 있다고 생각합니다.

![7](https://user-images.githubusercontent.com/87019897/175299972-68c83b8c-3f0a-4671-aa93-3d26c649dd0f.png)
![8](https://user-images.githubusercontent.com/87019897/175299983-c5f1d704-c6b9-4fd0-bf5e-634ecaccd81e.png)

## ✔️  **느낀 점(인사이트)**

1) DB 활용을 통해 데이터를 손쉽게 저장하고 BI툴을 사용하면 쉽게 데이터 시각화(EDA)를 할 수 있었습니다.
2) 웹에 퍼져있는 데이터를 웹스크래핑을 통해 필요한 데이터만을 추출하여 RDB에 저장하고 ML모델링을 통해 문제 해결에 적절히 활용할 수 있었습니다.