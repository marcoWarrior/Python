from veicolo import Veicolo  # Importa la classe Veicolo dal file veicolo.py

class AutoElettrica(Veicolo):
    def __init__(self, marca, modello, colore, autonomia):
        super().__init__(marca, modello, colore)
        self.autonomia = autonomia

    def mostraAutonomia(self):
        print(f"Autonomia dell'auto elettrica: {self.autonomia} km.\n")
