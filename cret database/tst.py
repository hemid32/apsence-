import sqlite3
import  os
f = os.getcwd()
d1 = 'data.db'
d2 = 'presence.db'

file = os.listdir(f)

if  d1 not in  file :
    s = open( d1, "w")

if d2 not in file :

    s2 =  open(d2 , 'w')


conn = sqlite3.connect(d1)
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS etidient (age TEXT , nome TEXT , prenom TEXT , numbre TEXT , classe TEXT)")

conn2 = sqlite3.connect(d2)
c2 = conn2.cursor()
c2.execute("CREATE TABLE IF NOT EXISTS presence (name_prenome TEXT , classe TEXT , data TEXT , presence TEXT )")