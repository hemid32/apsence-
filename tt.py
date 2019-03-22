import sqlite3
file = ("presence.db")

classe = 'A3'
conn = sqlite3.connect(file)
cur = conn.cursor()

cur.execute("SELECT * FROM presence WHERE classe = '%s' " % classe)
car = cur.fetchall()

p = []
#print car
for  i in  car :
    if i[2] not in p :
        p.append(i[2])


print p