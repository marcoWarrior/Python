class Veicolo:
    def __init__(self, marca, modello, colore):
        self.marca = marca
        self.modello = modello
        self.colore = colore
        self.stato = False

    def accendi(self):
        print(f"L'auto {self.marca}, modello: {self.modello}, colore: {self.colore} è stata accesa.\n")
        self.stato = True

    def ferma(self):
        print(f"L'auto {self.marca}, modello: {self.modello}, colore: {self.colore} è stata spenta.\n")
        self.stato = False

    def statoAuto(self):
        print(f"L'auto {self.marca}, modello: {self.modello}, colore: {self.colore} è {'' if self.stato else 'non '}accesa.\n")

    def __str__(self):
        return f"Veicolo: {self.marca} {self.modello}, Colore: {self.colore}, Stato: {'Accesa' if self.stato else 'Spenta'}"
