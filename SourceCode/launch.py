from flask import Flask, g
import sqlite3

from flask import Flask
app = Flask(__name__)
db_location = 'var/data.db'

def get_db():
  db = getattr(g, 'db', none)
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
    with app.open_resource('HomeStay.sql', more='r') as f:
      db.cursor().executescript(f.read())
      db.commit()

if __name__ == "__main":
  app.run(host="0.0.0.0", debug=True)
