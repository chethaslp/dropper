from flask import Flask, render_template, request, redirect, session, send_file
import firebase_admin
from firebase_admin import credentials, storage, db
import time
import json
from config import *

"""
DROPPER
 ~CLP - 2023

 Dropper is a flask app that allows users to upload files and share messages within one's private environment.
 Dropper is intented for personal use.

 Prereqs:
   * Create a Firebase project and download your credentials as json.
   * IN config.py ADD YOUR CREDENTIALS AND PASSWORD.
   * To host on web, you should have a hosting service with python support.
"""

app = Flask(__name__)
cred = credentials.Certificate(CRED_FILE)
firebase_admin.initialize_app(cred,STORAGE_URL)
app.secret_key = SECRET_KEY
pw = PASSWORD

def init():
    global pw
    pw = db.reference("dropper/pw").get(shallow=True) or PASSWORD

@app.route("/drop/upload",methods=["POST",'DELETE'])
def upload():
    """ Upload endpoint.
            * Uploads files to firebase storage.
    """
    if request.method == 'POST':
        f = request.files['file']
        fn = f.filename
        if not fn == '':
            blb = storage.bucket().blob('dropper/'+str(int(time.time()))+"_"+fn)
            blb.upload_from_file(f,content_type=f.content_type)
            blb.make_public()
            return [blb.name,blb.public_url]
    else:
        blb = storage.bucket().blob(json.loads(request.data)[0])
        blb.delete()
        return [True]
    

@app.route("/drop/chng_pw",methods=["POST"])
def chng_pw():
    """ Change Password endpoint.
    """
    if request.form['crt_pw'] == pw:
        if request.form['new_pw'] == request.form['new_pwc']:
            db.reference("dropper/pw").set(request.form['new_pw'])
            init()
            return "True"
    return "False"

@app.route("/drop/clr_drp",methods=["POST"])
def clr_drp():
     if request.form['pw'] == pw:
         db.reference("dropper/drops").delete()
         return "True"
     return "False"

@app.route("/",methods=['GET','POST'])
def root():
    """ Root
            * Renders the home page.
    """
    if request.method == 'POST':
        d = db.reference("dropper/drops/")

        fl = json.loads(request.form['fl'])

        if fl[1] == []:
            d.child(str(int(time.time()))).set({'d':request.form['msg'],"ip":fl[0]})
        else: 
            d.child(str(int(time.time()))).set({'d':request.form['msg'],'f':fl[1],"ip":fl[0]})
        return redirect("/")
    return render_template("index.html",ip_api=IP_API)

@app.route(VIEW_URL,methods=['POST','GET'])
def vvsd():
    """ View 
            * Allows user to access the shared datas."""
    init()
    if session.get("pw") and session.get("pw") == pw:
        d = db.reference("dropper/drops/").get()
        return render_template("view.html",login=True,d=d)
    if request.method=='POST' and request.form['pw'] == pw: 
        session.permanent = False
        session["pw"] = pw
        return redirect(VIEW_URL)
    return render_template("view.html",login=False)

@app.route("/favicon.ico")
def favicon():
    return send_file("templates/favicon.ico")

@app.template_filter('json')
def from_from(st):
    return json.loads(st)

@app.template_filter('fn')
def getfn(st):
    return st.replace("dropper/","").split("_",1)[1]

@app.template_filter('dt')
def dt(time=False):
    """
    Get a datetime object or a int() Epoch timestamp and return a
    pretty string like 'an hour ago', 'Yesterday', '3 months ago',
    'just now', etc
    """
    from datetime import datetime
    now = datetime.now()
    diff = now - datetime.fromtimestamp(int(time))
    second_diff = diff.seconds
    day_diff = diff.days

    if day_diff < 0:
        return ''

    if day_diff == 0:
        if second_diff < 10:
            return "just now"
        if second_diff < 60:
            return str(second_diff) + " seconds ago"
        if second_diff < 120:
            return "a minute ago"
        if second_diff < 3600:
            return str(second_diff // 60) + " minutes ago"
        if second_diff < 7200:
            return "an hour ago"
        if second_diff < 86400:
            return str(second_diff // 3600) + " hours ago"
    if day_diff == 1:
        return "Yesterday"
    if day_diff < 7:
        return str(day_diff) + " days ago"
    if day_diff < 31:
        return str(day_diff // 7) + " weeks ago"
    if day_diff < 365:
        return str(day_diff // 30) + " months ago"
    return str(day_diff // 365) + " years ago"


if __name__ == "__main__":
    app.debug = True
    app.run()