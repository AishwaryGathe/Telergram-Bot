from flask import Flask
from threading import Thread

app = Flask("")
@app.route('/')
def home():
  return " I,m Online!"
def run():
  app.run(host='0.0.0.0',port=8080)
def Server():
  basicConfig = Thread(target=run)
  basicConfig.start()