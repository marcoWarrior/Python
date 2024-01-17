class Forma:
    def calcola_area(self):
        pass

class Quadrato(Forma):
    def __init__(self, lato):
        self.lato = lato

    def calcola_area(self):
        return self.lato ** 2

class Cerchio(Forma):
    def __init__(self, raggio):
        self.raggio = raggio

    def calcola_area(self):
        return 3.14 * self.raggio ** 2

# Funzione polimorfica che calcola l'area di una forma
def area_forma(forma):
    return forma.calcola_area()

# Polimorfismo di inclusione
# La funzione area_forma è polimorfica di inclusione, in quanto può accettare oggetti di qualsiasi classe derivata da Forma.

quadrato = Quadrato(5)
cerchio = Cerchio(3)

print(area_forma(quadrato))  # Stampa 25 (area del quadrato)
print(area_forma(cerchio))   # Stampa circa 28.26 (area del cerchio)

# Polimorfismo di sovraccarico
# la classe Calcolatore, che fornisce due implementazioni del metodo somma con un numero diverso di argomenti.
# L'utilizzo del metodo somma mostra il polimorfismo di sovraccarico,
# poiché il metodo può essere chiamato con un diverso numero di argomenti, e la scelta di quale implementazione utilizzare avviene a tempo di chiamata.
class Calcolatore:
    def somma(self, a, b):
        return a + b

    def somma(self, a, b, c):
        return a + b + c

# Creazione di un oggetto Calcolatore
calcolatore = Calcolatore()

# Polimorfismo di sovraccarico nella chiamata a 'somma'
risultato1 = calcolatore.somma(2, 3)
risultato2 = calcolatore.somma(2, 3, 4)

print(risultato1)  # Stampa 5
print(risultato2)  # Stampa 9
