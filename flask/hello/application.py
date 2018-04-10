from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "hello, world!!!"

# export FLASK_APP=application.py
# flask run 
