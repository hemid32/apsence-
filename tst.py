# -*- coding : utf-8 -*-
import sys
from PyQt4.QtGui import *
import sqlite3
a = 'hemidi benameur'
b = 'hakmi mohamed'
c = 'hocine benziadi'
d = 'kjfvnjlkfvn '

liste = [a,b,c,d]


file = ("C:\Users\hemidi benameur\Desktop\project_\data.db")
conn = sqlite3.connect(file)
cur = conn.cursor()

file2 = ("presence.db")
conn2 = sqlite3.connect(file2)
cur2 = conn2.cursor()



cur.execute("SELECT * FROM etidient ")
l  = cur.fetchall()

cur2.execute("SELECT * FROM presence " )
m = cur2.fetchall()
print  m

