<p align="center" width="100%">
  <img src="https://raw.githubusercontent.com/chethaslp/dropper/master/screenshots/title.png" alt="title" width="100%"/> <br>
  Your personal dropbox.
</p>

### Usage

Remember when you are uncomfortable to login into a guest PC just to share some files from it. You would either had to login into whatsapp/telegram apps to share even just a link (now solved with QR codes). Thats where dropper comes in, its online and personal. So you and your close circle probably have access to it. You can use it to share any text or files through it to yourself. **Please duly note that this app is developed for personal use for a user and the security concerns are ignored for simplicity.**

### DEMO site
 Access Demo site at <a href="https://dropper-de4ro476z-chethaslp.vercel.app" target="_blank">dropper-de4ro476z-chethaslp.vercel.app (Preview)</a><br>
 Admin URL: <a href="https://dropper-de4ro476z-chethaslp.vercel.app/view/admin" target="_blank">dropper-de4ro476z-chethaslp.vercel.app/view/admin</a> <br>
 Admin password: demo

**Be sure that you are not uploading any sensitive contents.**
 In Demo mode, only the newest 5 drops are kept. Rest are deleted automatically.
 
### Implementation

* Home: [/], default
<p align="center" width="100%">
    <img src="https://raw.githubusercontent.com/chethaslp/dropper/master/screenshots/1.png" alt="Screenshot" width="500"/> 
</p>

* Home: [/], while Uploading a file
<p align="center" width="100%">
    <img src="https://raw.githubusercontent.com/chethaslp/dropper/master/screenshots/2.png" alt="Screenshot" width="500"/> 
</p>

* Viewpanel: [/view/admin], viewing all drops made so far
<p align="center" width="100%">
    <img src="https://raw.githubusercontent.com/chethaslp/dropper/master/screenshots/3.png" alt="Screenshot" width="500"/> 
</p>

* Home: [/view/admin], when settings dialog is open
<p align="center" width="100%">
    <img src="https://raw.githubusercontent.com/chethaslp/dropper/master/screenshots/4.png" alt="Screenshot" width="500"/> 
</p>

### Prerequisites
* Configure your [firebase account](https://console.firebase.google.com/) and create a project. 
* Get your 'credentials.json' from firebase.
        Most PaaS supports environment variables and secret files to be added.

* Set the following environment variables (prefered). Or, if you are using it locally, add it directly in 'config.py' file:
    
        PASSWORD : your password
  
        CRED : set the contents of 'credentials.json' to this variable.
                        OR
        CRED_FILE : set the path for 'credentials.json'. You could upload it as a 'secret file' in your PaaS.
  
        STRG_BKT : your firebase storage bucket URL
        STRG_DB : your firebase database URL

        VIEW URL: your login url (change it accordingly)
        SECRET_KEY: used for session storage (any random strong password could be added) [trivial]

    Go to [ipdata.co](https://ipdata.co) and create an account
        
        IP_API : enter the api key from ipdata.co here
          (This is required for capturing user IP and IP Location)
    
    Demo mode: Do not set this variable while in production. This is specifically set for the demo page in github.
        
        DEMO : True/False [default:False]

###

### Deployment

* To run locally for development, directly run web.py (Debug mode enabled).

* For production, use gunicorn:

        web: gunicorn --bind :8000 --workers 3 --threads 2 web:app

### Dependencies
```
Python:
    flask
    firebase_admin
    gunicorn
    python-dotenv
```
```
Javascript:
    Dropzone
    FilePond
    jQuery
    Bootstrap
    Fontawesome
```
<hr>

```
MIT License

Copyright (c) 2023 Chethas L Pramod

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
