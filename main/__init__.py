from flask import Flask,request,render_template
import sys
sys.path.append('/app/main')
from script.predict import castleInfo
from script.logger import logger

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/index4')
def home_seoul():
    return render_template('index4.html')

try:
    value=castleInfo()
except :
    value ={}
    logger.error("fail call fct : predict()")
# 서영
@app.route('/predict_castle')
def castle_predict():
    try:
        return render_template('predict_castle.html',data=value)
    except Exception:
        logger.error(Exception)
        return 'predict_castle.html'

@app.route('/select.html')
def select():
    return render_template('select.html')


