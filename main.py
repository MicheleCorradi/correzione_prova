

class Immobile():
    
    def __init__(self,riferimento,proprietario, indirizzo, prezzo):
        self.riferimento = riferimento
        self.proprietario = proprietario
        self.indirizzo = indirizzo
        self.prezzo = prezzo 

    def modifica_prezzo(self,prezzo):
        self.prezzo = prezzo

    def stampa_immobile(self):
        print(f"L'immobile con riferimento {self.riferimento} con proprietario {self.proprietario} all'indirizzo {self.indirizzo} costa {self.prezzo}")


class Catalogo():

    def __init__(self,nome):
        self.nome = nome
        self.immobili = list()
        self.database = self.nome + ".p"

    def aggiungi_immobile(self,immobile):
        self.immobili.append(immobile)
        print("L'immobile é stato aggiunto con successo!")

    def cancella(self,immobile):
        if immobile in self.immobili:
            self.delete.immobili
            print("L'immobile é stato cancellato con successo!")
        else:
            print("L'immobile non é presente!")

    def cerca_immobile(self,indirizzo):
        for immobile in self.immobili:
            if immobile.indirizzo == indirizzo:
                immobile.stampa_immobile()
            else:
                print("L'indirizzo non é corretto!")

    def stampa_catalogo(self):
        for immobile in self.immobili:
            immobile.stampa.immobile()

        



        