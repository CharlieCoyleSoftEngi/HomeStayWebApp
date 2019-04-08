from flask import Flask, g, render_template, request, session ,url_for, redirect
import sqlite3
import os
import os.path
import bcrypt
from flask import Flask

app = Flask(__name__)
db_location = 'var/sqlite3.db'
app.secret_key = "zxdcfgyhujiolp;'[/.,mnbvcdrtyui"

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
    with app.open_resource('schema.sql', mode='r') as f:
      db.cursor().executescript(f.read())
    db.commit()

def check_auth_H(username, password):
        db = get_db()
        data = db.cursor().execute("SELECT email,hPassword FROM Host")
        data = data.fetchall()
        password = password.encode('utf-8')
        for item in (data):
                        if(username == item[0] and item[1].encode('utf-8') == bcrypt.hashpw(password,item[1].encode('utf-8'))):
                                print("ITS ALIVE!!! HOST")
                                return True
        return False

def check_auth_A(username, password):
        db = get_db()
        data = db.cursor().execute("SELECT email,aPassword FROM Applicants")
        data = data.fetchall()
        password = password.encode('utf-8')
        for item in (data):
                        if(username == item[0] and item[1].encode('utf-8') == bcrypt.hashpw(password,item[1].encode('utf-8'))):
                                print("ITS ALIVE!!! Applicant")
                                return True
        return False


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

#Home page
@app.route('/homestay', methods=["POST","GET"])
def  HomePageSlected(name=None):
		try:
			print (session['Type'])
			if session['Type'] == 'Host':
                        	UserType = 'Host'
			else:
                        	UserType = 'Applicant'
		except:
			print ("Not A HOST")
			UserType = "Visitor"
		db= get_db()
		data = db.cursor().execute("SELECT * FROM Vacancies")
		data = list(data.fetchall())
		urlHelper = "homestay/listing/"
		return render_template("index.html",data=data,urlHelper=urlHelper,ut=UserType)

	 #This is a tempory page until template is made.


#Profile page
@app.route('/homestay/profile', methods=["POST","GET"])
def  ProfileSlected(name=None):

                if session['Type'] == 'Host':
			db = get_db()
			userContent =  query_db('SELECT * FROM Host WHERE email = ?', [session['Current_User']], one=True)
			negStar = 10 - int(userContent[6])
			negStar1 = range(negStar)
			posStar1 = range(int(userContent[6]))
			userListings = db.cursor().execute('SELECT * FROM Vacancies WHERE hostID = ?', [userContent[0]])
			userListings = list(userListings.fetchall())
			urlHelper = "../homestay/listing/"
			return render_template("host.html", userContent=userContent, userListings=userListings, negStar1=negStar1, posStar1=posStar1, urlHelper=urlHelper )
		elif session['Type'] == 'Applicant':
			db = get_db()
			userContent = query_db('SELECT * FROM Applicants WHERE email = ?', [session['Current_User']], one=True)
                        negStar = 10 - int(userContent[7])
                        negStar1 = range(negStar)
                        posStar1 = range(int(userContent[7]))
			urlHelper = "../homestay/listing/"
			userAplications = db.cursor().execute('SELECT * FROM Applications WHERE applicantID = ?', [userContent[0]])
			userListings = list(userAplications.fetchall())
			return render_template("student.html", userContent=userContent, userAplications=userAplications, negStar1=negStar1, posStar1=posStar1, urlHelper=urlHelper )
		else:
			return render_template("listingtemp.html")
         #This is a tempory page until template is made.


#Login page
@app.route('/homestay/login', methods=["POST","GET"])
def  LoginSlected(name=None):
        db = get_db()
        if request.method == 'POST':
                  username = request.form['email']
                  password = request.form['address']

                  if check_auth_H(username,password):
                         session['Current_User'] =  username
			 session['Type'] = 'Host'
                         print("Working!")
                         return redirect(url_for(".HomePageSlected"))

                  if check_auth_A(username,password):
                         session['Current_User'] =  username
			 session['Type'] = 'Applicant'
                         print("Working!")
                         return redirect(url_for(".HomePageSlected"))

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
@app.route('/homestay/user_create_account', methods=["POST","GET"])
def  CreateAccountSlected(name=None):
        db = get_db()
        if request.method == 'POST':
                user = request.form['email']
                pword = request.form['password']
		firstName = request.form['firstname']
		lastName = request.form['lastname']
		diet = request.form['diet']
		dob = request.form['date']
		university = request.form['university']
		nationality = request.form['nationality']
		confirm = request.form['cPassword']
		telNo = request.form['telNo']
		if pword == confirm :
                	pword = pword.encode('utf-8')
                	hashedpw = bcrypt.hashpw(pword, bcrypt.gensalt())
               		if (hashedpw is not None and user is not None):
                        		db.cursor().execute("INSERT INTO Applicants(email,aPassword,firstName,lastName,dietaryRequirements,dob,university,nationality,phoneNumber) VALUES (?,?,?,?,?,?,?,?,?)",(user,hashedpw,firstName,lastName,diet,dob,university,nationality,telNo))
                        		db.commit()
                        return redirect(url_for('.LoginSlected'))
		else :
			return render_template("create_account.html")

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

@app.route('/homestay/host_create_account', methods=["POST","GET"])
def  CreateHostAccountSlected(name=None):
        db = get_db()
        if request.method == 'POST':
                user = request.form['email']
                pword = request.form['password']
		confirm = request.form['cPassword']
                firstName = request.form['firstname']
                lastName = request.form['lastname']
                telNo = request.form['telNo']
                if pword == confirm :
                        pword = pword.encode('utf-8')
                        hashedpw = bcrypt.hashpw(pword, bcrypt.gensalt())
                        if (hashedpw is not None and user is not None):
                                        db.cursor().execute("INSERT INTO Host(email,hPassword,firstName,lastName,phoneNumber) VALUES (?,?,?,?,?)",(user,hashedpw,firstName,lastName,telNo))
                                        db.commit()
                        #return redirect(url_for('.login'))
                else :
                        return render_template("create_host.html")

        try:

                 return render_template("create_host.html")

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
   if request.method == 'POST':
                location = request.form['location']
                Description = request.form['description']
                Rate = request.form['rate']
                StartDate = request.form['start_date']
                EndDate = request.form['end_date']
                curfew = request.form['curfew']
                extra_info = request.form['extra_info']
                        #Get the host id for foreigen key
                Host = session["Current_User"]
                db = get_db()
                print("we got here")
                hostid = query_db('SELECT hostID FROM Host WHERE email = ?', [Host], one=True)
		Hostid = int(hostid[0])
		f = request.files['property']
		print (f)
		imageName = str(Hostid) + location.replace(" ","_") + ".PNG"
		num = 0
		while os.path.isfile('static/uploads/' + imageName):
			imageName = imageName + str(num)
			num = num + 1
		imagePath = ('static/uploads/' + imageName)
		f.save(imagePath)
		print(hostid)
                db.cursor().execute('INSERT INTO Vacancies(hostID,location,description,rate,startDate,endDate,available,curfew,extraInfo,images)Values(?,?,?,?,?,?,?,?,?,?)',(Hostid,location,Description,Rate,StartDate,EndDate,"1",curfew,extra_info,imageName))
                db.commit()
                print("we also got here")
   try:
   	if session['Type'] == 'Host':
	   	return render_template("createlistings.html")
   	else:
		return render_template("listingtemp.html")
   except:
	return render_template("listingtemp.html")
        #This is a tempory page until template is made.
       #listing page

@app.route('/homestay/listing', methods=["POST","GET"])
@app.route('/homestay/listing/<id>', methods=["POST","GET"])
def  CAccountSlected(name=None,id=None):
	db = get_db()
	id = int(id)
	result = query_db('SELECT * FROM Vacancies WHERE vacancyID = ?', [id], one=True)
	result[2]
	GMLink = "https://www.google.com/maps/search/" + result[2]
	GMLink = GMLink.replace(" ","+")
	result[1]
	HPLink = "../profile/host/" + str(result[1])
	print(HPLink)
	return render_template("listings.html",result=result,GMLink=GMLink,HPLink=HPLink)

        #This is a tempory page until template is made.


#host profile page
#this will change once sessions are figured out
@app.route('/homestay/profile/host/<host>', methods=["POST","GET"])
def  HostSlected(name=None, host=None):
		db = get_db()
		Host = query_db('SELECT * FROM Host WHERE hostID = ?', [host], one=True)
		negStar = 10 - int(Host[6])
		negStar1 = range(negStar)
		posStar1 = range(int(Host[6]))
		userListings = db.cursor().execute('SELECT * FROM Vacancies WHERE hostID = ?', [Host[0]])
		userListings = list(userListings.fetchall())
		urlHelper = "../../../homestay/listing/"
		return render_template("host.html", userContent=Host, userListings=userListings, negStar1=negStar1, posStar1=posStar1, urlHelper=urlHelper )

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

@app.route('/homestay/app', methods=["POST","GET"])
def  AppSlected(name=None):
        try:
                #assuming that profile.html is the same for use host and admin
                 return render_template("application.html")

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


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
