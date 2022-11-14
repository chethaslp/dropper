from flask import Flask, render_template, request, redirect ,url_for
import firebase_admin
from firebase_admin import credentials, storage, db
import time
import json

app = Flask(__name__)
cred = credentials.Certificate("cred.json")
firebase_admin.initialize_app(cred,{'storageBucket': 'examerapp.appspot.com','databaseURL':'https://examerapp.firebaseio.com'})


@app.route("/drop/upload",methods=["POST"])
def upload():
    f = request.files['file']
    fn = f.filename
    if not fn == '':
        blb = storage.bucket().blob('drops/'+str(int(time.time()))+"_"+fn)
        blb.upload_from_file(f,content_type=f.content_type)
        blb.make_public()
        return blb.public_url
    return "False"

@app.route("/",methods=['GET','POST'])
def root():
    if request.method == 'POST':
        d = db.reference("drops/")
        if request.form['fl'] == "": d.child(str(int(time.time()))).set({'d':request.form['msg'],"ip":request.remote_addr})
        else: d.child(str(int(time.time()))).set({'d':request.form['msg'],'f':request.form['fl'],"ip":request.remote_addr})
        return redirect("/")
    return render_template("index.html")

@app.route("/view/clp",methods=['POST','GET'])
def vvsd():
    if request.method=='POST':
        if request.form['pw'] == "chethas123":
            d = db.reference("drops/").get()
            return render_template("view.html",login=True,d=d)
    return render_template("view.html",login=False)

@app.template_filter('json')
def from_from(st):
    return json.loads(st)

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

import os
if os.environ.get('PORT'):
    app.run(port=os.environ['PORT'],host='0.0.0.0')
else:
    app.debug = True
    app.run()