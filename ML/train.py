import pandas as pd
from sklearn.metrics import f1_score,accuracy_score
from sklearn.metrics import classification_report
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from category_encoders import OrdinalEncoder
from sklearn.model_selection import train_test_split
import sqlite3
import joblib
import pickle

#인코더 설치 안되어 있으면 설치하기
#pip install category_encoders

#데이터베이스에서 정보 불러오기
conn= sqlite3.connect("/Users/damon/section3_project/tumblbug.db")
cur = conn.cursor()
query = cur.execute("SELECT * FROM tumblbug")
cols = [column[0] for column in query.description]
df = pd.DataFrame.from_records(data=query.fetchall(),columns=cols)
#데이터베이스 닫기
conn.close()

#데이터프레임 전처리
df = df.fillna(df.mean()['reward_price1':'reward_price2'])

#데이터 나누기
features = ['target_price', 'category', 'text_length','reward_price1', 'reward_price2']
target = 'target'

X = df[features]
y = df[target]

#메소드 사용하여 훈련데이터, 테스트데이터 나누기 (훈련 80%, 테스트 20%)
X_train, X_val, y_train, y_val = train_test_split(X, y,train_size=0.8, test_size=0.20, random_state=2)
X_val, X_test, y_val, y_test = train_test_split(X_val, y_val,train_size=0.8, test_size=0.20, random_state=2)

##base 모델 설정
#major = y_train.mode()[0]
#y_pred = [major] * len(y_train)
#print('훈련 정확도 :' , classification_report(y_train, y_pred))
#y_pred = [major]* len(y_val)
#print('검증 정확도 :' , classification_report(y_val, y_pred))

pipe = Pipeline([
    ('preprocessing', make_pipeline(OrdinalEncoder())),
    ('rf', RandomForestClassifier(n_estimators=100, random_state=2, n_jobs=-1))])

pipe.fit(X_train, y_train)

y_pred = pipe.predict(X_val)
#print(classification_report(y_val, y_pred))

#성공확률
y_pred_proba = pipe.predict_proba(X_val)[:, 1]
#print(y_pred_proba)

# 학습시킨 모델을 현재 경로에 judge_model.pkl 파일로 저장합니다.
joblib.dump(pipe, '/Users/damon/section3_project/judge_model.pkl')

#성능확인 및 저장확인
loaded_model = joblib.load('/Users/damon/section3_project/judge_model.pkl')

y_pred = loaded_model.predict(X_val)
print(classification_report(y_val, y_pred))