

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
        