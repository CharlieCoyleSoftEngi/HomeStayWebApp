import sqlite3
import bcrypt
db_location = 'var/sqlite3.db'
secret_key = "zxdcfgyhujiolp;'[/.,mnbvcdrtyui"
conn = sqlite3.connect('sqlite3.db')
c = conn.cursor()
pword = "bb1572"
pword = pword.encode('utf-8')
hashedpw = bcrypt.hashpw(pword, bcrypt.gensalt())
c.execute('INSERT INTO Admin(username,password) VALUES(?,?)',("Admin",hashedpw))
conn.commit()
