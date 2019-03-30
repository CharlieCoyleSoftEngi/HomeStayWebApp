import sqlite3
conn = sqlite3.connect('sqlite3.db')
c = conn.cursor()
c.execute('INSERT INTO Vacancies VALUES(101,1011,"32 test Av","du du","31/h","2012/12/12","2012/12/12",1,"12.00.00","dfdasf","ffgsdgs")')
conn.commit()
