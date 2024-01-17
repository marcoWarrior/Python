class Pila:
    def __init__(self):
        self.items = []

    def aggiungi(self, valore):
        self.items.append(valore)

def leggi(stk, in_pos):
    if in_pos < 0 or in_pos >= len(stk.items):
        return "Posizione non valida"
    return stk.items[in_pos]

def main():
    stk = Pila()

    stk.aggiungi(10)
    stk.aggiungi(20)
    stk.aggiungi(30)
    stk.aggiungi(40)

    print("Inserisci la posizione da ricercare")
    posizione_da_ricercare = int(input())

    risultato = leggi(stk, posizione_da_ricercare)
    print("Valore trovato:", risultato)
    print("Pila:", stk.items)

if __name__ == "__main__":
    main()
