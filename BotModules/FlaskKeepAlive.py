# To keep bot running, run this app in parallel to your code.

from flask import Flask
from threading import Thread

def FlaskApp(seconds):
    app=Flask("")

    @app.route("/")
    def index():
      return """<!DOCTYPE html>


<html lang="en"  content="text/html; charset=UTF-8" >
<link rel="icon" type="image/png" sizes="32x32" href="https://raw.githubusercontent.com/bondeabhijeet/TorrentSearcherBot/main/ats.png">
<body style="background-color:#1d1f1f;">
<a href="https://www.bondeabhijeet.co/" style="text-decoration:none">
<font style="color:#f4f6f7 ">
<h2><pre>				b͟o͟n͟d͟e͟a͟b͟h͟i͟j͟e͟e͟t͟</pre></h2></font>
</a>

<h1 style="text-align:center;" > <font style="color:#f4f6f7 "> Hi, I'm Torrent Search Bot </font> <br> <font style="color:#6495ED"> & I'm Running </font> </h1>
<p style="text-align:center;" > <font style='color:#c39bd3'>____________________________________________________________________________________________________________ </font></pre>
<p style="text-align:center;" > <font style="color:#2ECC71 ">  I'm a simple telegram bot written in python to search torrents </font> </p>


<p>

<center style="background-color:#1d1f1f;">
<a  style="color:white" align="center" href="https://github.com/bondeabhijeet/TorrentSearcherBot">Source Code</a> &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a  style="color:white" align="center" href="https://t.me/AbhijeetsClan">Telegram Channel</a>


</center>
</p>
    
<a href="https://www.bondeabhijeet.co/" style="text-decoration:none" align="center">
         <pre> <img alt="bondeabhijeet" align="center" src="https://raw.githubusercontent.com/bondeabhijeet/TorrentSearcherBot/main/Bondeabhijeet1.png"
         width=700" height="233.33"> </pre>
      </a>

</body>




</html>"""
    Thread(target=app.run,args=("0.0.0.0",8080)).start()