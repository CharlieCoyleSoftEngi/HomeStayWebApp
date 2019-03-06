from flask import Flask, g
import sqlite3

from flask import Flask
app = Flask(__name__)
db_location = 'var/sqlite3.db'

def get_db():
  db = getattr(g, 'db', None)
  if db is None:
    db = sqlite3.connect(db_location)
    g.db = db
  return db

@app.teardown.appcontext
def close_db_connection(exception):
  db = getattr(g, 'db' , None)
  if db is not None:
    db.close()

def init_db():
  with app.app_context():
    db = get_db()
    with app.open_resource('schema.sql', more='r') as f:
      db.cursor().executescript(f.read())
      db.commit()

#Home page
@app.route('/homestay', methods=["POST","GET"])
def  HomePageSlected(name=None):
	try:
		 return render_template("home.html")

	 #This is a tempory page until template is made.
	except:
		page ='''
        <html><body>
         <h1 style ="text-align: center"> Temp HomePage</h1>
         <h2 style ="text-align: center">The page you are looking for dosen't exist yet</h2>
        </body></html> '''
	return page, 404

#Profile page
@app.route('/homestay/profile', methods=["POST","GET"])
def  HomePageSlected(name=None):
        try:
                 return render_template("profile.html")

	#This is a tempory page until template is made.
	except:
                page ='''
        <html><body>
         <h1 style ="text-align: center"> Temp HomePage</h1>
         <h2 style ="text-align: center">The page you are looking for dosen't exist yet</h2>
        </body></html> '''
        return page, 404

#Login page
@app.route('/homestay/login', methods=["POST","GET"])
def  HomePageSlected(name=None):
        try:
                 return render_template("log_in.html")

 	#This is a tempory page until template is made.
        except:
                page ='''
        <html><body>
         <h1 style ="text-align: center"> Temp HomePage</h1>
         <h2 style ="text-align: center">The page you are looking for dosen't exist yet</h2>
        </body></html> '''
        return page, 404

#create_account page
@app.route('/homestay/createaccount', methods=["POST","GET"])
def  HomePageSlected(name=None):
        try:
                 return render_template("create_account.html")

        #This is a tempory page until template is made.
        except:
                page ='''
        <html><body>
         <h1 style ="text-align: center"> Temp HomePage</h1>
         <h2 style ="text-align: center">The page you are looking for dosen't exist yet</h2>
        </body></html> '''
        return page, 404

#create_listing page
@app.route('/homestay/create_listing', methods=["POST","GET"])
def  HomePageSlected(name=None):
        try:
                 return render_template("create_listing.html")

        #This is a tempory page until template is made.
        except:
                page ='''
        <html><body>
         <h1 style ="text-align: center"> Temp HomePage</h1>
         <h2 style ="text-align: center">The page you are looking for dosen't exist yet</h2>
        </body></html> '''
        return page, 404


#listing page
@app.route('/homestay/createaccount', methods=["POST","GET"])
def  HomePageSlected(name=None):
        try:
                 return render_template("lising.html")

        #This is a tempory page until template is made.
        except:
                page ='''
        <html><body>
         <h1 style ="text-align: center"> Temp HomePage</h1>
         <h2 style ="text-align: center">The page you are looking for dosen't exist yet</h2>
        </body></html> '''
        return page, 404


#users profile page
#this will change once sessions are figured out
@app.route('/homestay/profle/user', methods=["POST","GET"])
def  HomePageSlected(name=None):
        try:
		#assuming that profile.html is the same for use host and admin
                 return render_template("profile.html")

        #This is a tempory page until template is made.
        except:
                page ='''
        <html><body>
         <h1 style ="text-align: center"> Temp HomePage</h1>
         <h2 style ="text-align: center">The page you are looking for dosen't exist yet</h2>
        </body></html> '''
        return page, 404


#host profile page
#this will change once sessions are figured out
@app.route('/homestay/profle/host', methods=["POST","GET"])
def  HomePageSlected(name=None):
        try:
                #assuming that profile.html is the same for use host and admin
                 return render_template("profile.html")

        #This is a tempory page until template is made.
        except:
                page ='''
        <html><body>
         <h1 style ="text-align: center"> Temp HomePage</h1>
         <h2 style ="text-align: center">The page you are looking for dosen't exist yet</h2>
        </body></html> '''
        return page, 404

#admin profile page
#this will change once sessions are figured out
@app.route('/homestay/profle/admin', methods=["POST","GET"])
def  HomePageSlected(name=None):
        try:
                #assuming that profile.html is the same for use host and admin
                 return render_template("profile.html")

        #This is a tempory page until template is made.
        except:
                page ='''
        <html><body>
         <h1 style ="text-align: center"> Temp HomePage</h1>
         <h2 style ="text-align: center">The page you are looking for dosen't exist yet</h2>
        </body></html> '''
        return page, 404

#apply  page
@app.route('/homestay/listing/apply', methods=["POST","GET"])
def  HomePageSlected(name=None):
        try:
                #assuming that profile.html is the same for use host and admin
                 return render_template("apply.html")

        #This is a tempory page until template is made.
        except:
                page ='''
        <html><body>
         <h1 style ="text-align: center"> Temp HomePage</h1>
         <h2 style ="text-align: center">The page you are looking for dosen't exist yet</h2>
        </body></html> '''
        return page, 404




if __name__ == "__main":
  app.run(host="0.0.0.0", debug=True)
