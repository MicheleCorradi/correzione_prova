import sqlite3


conn = sqlite3.connect('immobili.db')
curs = conn.cursor()

try:
    curs.execute("DROP table immobile")
    curs.execute("DROP table catalogo")
except:
    pass

curs.execute("CREATE table immobile (riferimento char(30), proprietario char(30),indirizzo char(30), citta char(30), prezzo int, catalogo char(30))")


class Immobile():
    
    def __init__(self,riferimento,proprietario, indirizzo, prezzo,citta):
        self.riferimento = riferimento
        self.proprietario = proprietario
        self.indirizzo = indirizzo
        self.prezzo = prezzo 
        self.citta = citta

    def modifica_prezzo(self,prezzo):
        self.prezzo = prezzo

    def stampa_immobile(self):
        print(f"L'immobile con riferimento {self.riferimento} con proprietario {self.proprietario} all'indirizzo {self.indirizzo} costa {self.prezzo}")


class Catalogo():
    def __init__(self, nome, cursore):
        self.nome = nome
        self.immobili = list()
        self.cursore = cursore

    def aggiungi_immobile(self, immobile):
        self.immobili.append(immobile)
        row = (immobile.riferimento, immobile.proprietario, immobile.indirizzo,immobile.prezzo, immobile.citta, self.nome)
        self.cursore.execute("INSERT INTO immobile values(?, ?, ?, ?, ?, ?)",row)
        print("L'immobile é stato aggiunto con successo!")
        conn.commit()#per scriverle all'interno del database

    def cancella_immobile(self, immobile):
        if immobile in self.immobili:
            self.immobili.delete(immobile)
            self.cursore.execute("DELETE FROM immobile WHERE riferimento = ?",(immobile.riferimento,))
            print("L'immobile é stato cancellato con successo!")
        else:
            print("L'immobile non é presente!")

    def cerca_immobile(self,indirizzo):
        for immobile in self.immobili:
            if immobile.indirizzo == indirizzo:
                print("Immobili trovati:")
                immobile.stampa_immobile()
        print("dal database:")

        self.cursore.execute("SELECT * FROM immobile WHERE indirizzo = ?",(immobile.indirizzo, ))
        for row in self.cursore.fetchall():
            print(row)


    def stampa_catalogo(self):
        for immobile in self.immobili:
            immobile.stampa_immobile()
        print("dal database:")
        self.cursore.execute("SELECT * FROM immobile")
        for row in self.cursore.fetchall():
            print(row)


generale = Catalogo("generale", curs)

casa1 = Immobile("1a","Lelio Campanile","Via Roma",200000,"Aversa")
casa2 = Immobile("2a", "Caio", "Via dei Gracchi", 700000, "Roma")

generale.aggiungi_immobile(casa1)
generale.aggiungi_immobile(casa2)

generale.stampa_catalogo()

generale.cerca_immobile("Via Roma")



