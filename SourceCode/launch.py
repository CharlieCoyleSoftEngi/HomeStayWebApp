from flask import Flask, g, render_template, request, session ,url_for, redirect
import sqlite3
import os

from flask import Flask

app = Flask(__name__)
db_location = 'var/sqlite3.db'

def get_db():
  db = getattr(g, 'db', None)
  if db is None:
    db = sqlite3.connect(db_location)
    g.db = db
  return db

@app.teardown_appcontext
def  close_db_connection(exception):
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
		return page

#Profile page
@app.route('/homestay/profile', methods=["POST","GET"])
def  ProfileSlected(name=None):
        try:
                return render_template("profile.html")

         #This is a tempory page until template is made.
        except:
                page ='''
                <html><body>
                <h1 style ="text-align: center"> Temp HomePage</h1>
                <h2 style ="text-align: center">The page you are lookin$
                </body></html> '''
                return page

#Login page
@app.route('/homestay/login', methods=["POST","GET"])
def  LoginSlected(name=None):
        try:
                 return render_template("log_in.html")

 	#This is a tempory page until template is made.
        except:
                page ='''
        	<html><body>
         	<h1 style ="text-align: center"> Temp login</h1>
         	<h2 style ="text-align: center">The page you are looking for dosen't exist yet</h2>
                </body></html> '''
                return page

#create_account page
@app.route('/homestay/createaccount', methods=["POST","GET"])
def  CreateAccountSlected(name=None):
        try:
                 return render_template("create_account.html")

        #This is a tempory page until template is made.
        except:
               	page ='''
        	<html><body>
        	<h1 style ="text-align: center"> Temp createaccount</h1>
         	<h2 style ="text-align: center">The page you are looking for dosen't exist yet</h2>
                </body></html> '''
                return page

#create_listing page
@app.route('/homestay/create_listing', methods=["POST","GET"])
def  ClistingSlected(name=None):
        try:
                 return render_template("create_listing.html")

        #This is a tempory page until template is made.
        except:
               	page ='''
        	<html><body>
         	<h1 style ="text-align: center"> Temp createlisting</h1>
         	<h2 style ="text-align: center">The page you are looking for dosen't exist yet</h2>
                </body></html> '''
                return page

#listing page
@app.route('/homestay/createaccount', methods=["POST","GET"])
def  CAccountSlected(name=None):
        try:
                 return render_template("lising.html")

        #This is a tempory page until template is made.
        except:
               	page ='''
        	<html><body>
         	<h1 style ="text-align: center"> Temp lisiting</h1>
         	<h2 style ="text-align: center">The page you are looking for dosen't exist yet</h2>
                </body></html> '''
                return page


#users profile page
#this will change once sessions are figured out
@app.route('/homestay/profle/user', methods=["POST","GET"])
def  UserSlected(name=None):
        try:
		#assuming that profile.html is the same for use host and admin
                 return render_template("profile.html")

        #This is a tempory page until template is made.
        except:
               	page ='''
        	<html><body>
         	<h1 style ="text-align: center"> Temp user</h1>
         	<h2 style ="text-align: center">The page you are looking for dosen't exist yet</h2>
                </body></html> '''
                return page

#host profile page
#this will change once sessions are figured out
@app.route('/homestay/profle/host', methods=["POST","GET"])
def  HostSlected(name=None):
        try:
                #assuming that profile.html is the same for use host and admin
                 return render_template("profile.html")

        #This is a tempory page until template is made.
        except:
                page ='''
        	<html><body>
         	<h1 style ="text-align: center"> Temp host</h1>
         	<h2 style ="text-align: center">The page you are looking for dosen't exist yet</h2>
                </body></html> '''
                return page

#admin profile page
#this will change once sessions are figured out
@app.route('/homestay/profle/admin', methods=["POST","GET"])
def  AdminSlected(name=None):
        try:
                #assuming that profile.html is the same for use host and admin
                 return render_template("profile.html")

        #This is a tempory page until template is made.
        except:
                page ='''
        	<html><body>
         	<h1 style ="text-align: center"> Temp admin</h1>
         	<h2 style ="text-align: center">The page you are looking for dosen't exist yet</h2>
                </body></html> '''
                return page

#apply  page
@app.route('/homestay/listing/apply', methods=["POST","GET"])
def  ListingSlected(name=None):
        try:
                #assuming that profile.html is the same for use host and admin
                 return render_template("apply.html")

        #This is a tempory page until template is made.
        except:
                page ='''
        	<html><body>
         	<h1 style ="text-align: center"> Temp lisitng</h1>
         	<h2 style ="text-align: center">The page you are looking for dosen't exist yet</h2>
                </body></html> '''
                return page

#404 page
@app.errorhandler(404)
def  page_not_Found(error):
	page ='''
        <html><body>
        <h1 style ="text-align: center"> 404 You seem to have gotten lost fallen out of the site</h1>
        <h2 style ="text-align: center">The page you are looking for dosen't exist<h2>
        </body></html> '''
	return page, 404


if __name__ == "__main":
  app.run(host="0.0.0.0", debug=True)
