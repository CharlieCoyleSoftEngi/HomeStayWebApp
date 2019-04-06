import sqlite3
conn = sqlite3.connect('sqlite3.db')
c = conn.cursor()
c.execute('INSERT INTO Vacancies VALUES(103,1012,"Fountain Bridge","its fountain bridge","10/d","2018/10/12","2012/12/12",1,"12.00.00","ocupants are jewish","ffgsdgs")')
conn.commit()
