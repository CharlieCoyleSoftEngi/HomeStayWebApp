Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
from flask import Flask, session

app = Flask(__name_)
app.secret_key = ’A0Zr98j /3 yX R~XHH!jmN]LWX / ,? RT ’


@app.route('/')
def index():
    return "Root route for sessions example"

@app.route('/sessions/write/<name>/')
def write (name=None):
    session['name'] = name
    return "Wrote %s into 'name' key of session" % name

@app.route('/session/read/')
def.read():
    try:
      if(session['name']):
          return str (session['name'])
    except KeyError:
      pass
    return "No session variable set for 'name' key"

@app.route ('/session/remove/')
def remove():
    session.pop('name' , None)
    return "Removed key 'name' from session"

if __name__ == "__main__"
  app.run(host='0.0.0.0' , debug=True)

