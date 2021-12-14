from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def dict():
    return {"data": "Hello Flask!"}

@app.route('/current_datetime', methods=['GET'])
def current_datetime_dict():
    message = ''
    current_datetime = datetime.now()
    if current_datetime.strftime("%p") == 'am':
        message = 'Bom dia!'
    elif current_datetime.strftime("%H") >= '12' and current_datetime.strftime("%H") < '18':
        print(current_datetime.strftime("%H"))
        message = 'Boa tarde!'
    else:
       message = 'Boa noite!'
    return {"current_datetime": current_datetime.strftime("%d/%m/%Y %H:%M:%S %p"), "message": message}
