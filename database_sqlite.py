import sqlite3


conn = sqlite3.connect('immobili.db')
curs = conn.cursor()
try:
    curs.execute("DROP table immobile")
    curs.execute("DROP table catalogo")
except:
    
    pass
curs.execute("CREATE table immobile (riferimento char(30), proprietario char(30),indirizzo char(30), citta char(30), prezzo int, catalogo char(30))")