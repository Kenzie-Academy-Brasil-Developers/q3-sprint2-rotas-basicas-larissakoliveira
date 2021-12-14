from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def dict():
    return {"data": "Hello Flask"}

@app.route('/current_datetime', methods=['GET'])
def current_datetime_dict():
    current_datetime = datetime.now()
    if current_datetime.strftime("%p") == 'am':
        return f' {current_datetime} + <h1>Bom dia!</h1>'
    elif current_datetime.strftime("%H") >= '12' and current_datetime.strftime("%H") < '18':
        print(current_datetime.strftime("%H"))
        return f'{current_datetime}  <h1>Boa tarde!</h1>'
    else:
        return f'{current_datetime}  <h1>Boa noite!</h1>'

