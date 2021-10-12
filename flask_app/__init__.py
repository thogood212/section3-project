from flask import Flask
from flask import Flask, render_template
from flask import request
import pandas as pd
import joblib

app = Flask(__name__)
model = joblib.load('/Users/damon/section3_project/judge_model.pkl')

#y_pred = loaded_model.predict(X_val)
#y_pred_proba = pipe.predict_proba(X_val)[:, 1]

@app.route('/',methods = ['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        #data = request.form
        target_price = int(request.form['target_price'])
        category = request.form['category']
        text_length = int(request.form['text_length'])
        reward_price1 = float(request.form['reward_price1'])
        reward_price2 = float(request.form['reward_price2'])
        
        df = pd.DataFrame({'target_price':[target_price], 'category':[category], 'text_length':[text_length], 'reward_price1':[reward_price1], 'reward_price2':[reward_price2]})

        y_pred = model.predict(df)
        y_pred_proba = model.predict_proba(df)[:, 1]

    return render_template('result.html',data=y_pred_proba)

    #    target_price = request.form['target_price']
    #    category = request.form['category']
    #    text_length = request.form['text_length']
    #    reward_price1 = request.form['reward_price1']
    #    reward_price2 = request.form['reward_price2']
    #    return target_price


if __name__ == '__main__':
    app.run(debug=True)