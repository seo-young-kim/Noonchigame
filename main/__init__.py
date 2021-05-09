from flask import Flask,request,render_template
import sys
sys.path.append('/app/main')
from script import get_data
from script.logger import makelog
import time

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


logger = makelog("seoykim")

try:
    time0 = time.time()
    value=get_data.castleInfo()
    logger.info("Successful! Loading Time:{}".format(time.time()-time0))
except :
    logger.exception()

@app.route('/predict_castle')
def castle_predict():
    try:
        return render_template('predict_castle.html',data=value)
    except :
        logger.exception()
        return value

@app.route('/select.html')
def select():
    return render_template('select.html')


