from flask import Flask,request,render_template
import sys
sys.path.append('/app/main')
from script.get_data import castleInfo
from script.logger import logger

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

try:
    value=castleInfo()
except :
    logger.error("Failed to get data : castleInfo()")
# 서영
@app.route('/predict_castle')
def castle_predict():
    try:
        return render_template('predict_castle.html',data=value)
    except Exception:
        logger.error(Exception)
        return value


@app.route('/select.html')
def select():
    return render_template('select.html')


