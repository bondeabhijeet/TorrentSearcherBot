# To keep bot running, run this app in parallel to your code.

from flask import Flask
from threading import Thread

def FlaskApp(seconds):
    app=Flask("")

    @app.route("/")
    def index():
      return "<h1>Bot is running</h1>"

    Thread(target=app.run,args=("0.0.0.0",8080)).start()