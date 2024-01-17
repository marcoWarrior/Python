import random

def crea_campo_minato():
    campo_minato = [[' ' for _ in range(5)] for _ in range(5)]
    num_mine = random.randint(5, 10)

    for _ in range(num_mine):
        while True:
            riga, colonna = random.randint(0, 4), random.randint(0, 4)
            if campo_minato[riga][colonna] != 'X':
                campo_minato[riga][colonna] = 'X'
                break

    return campo_minato

def stampa_campo(campo):
    print("  0 1 2 3 4")
    for i in range(5):
        print(i, end=' ')
        for j in range(5):
            print(campo[i][j], end=' ')
        print()

def gioca():
    campo = crea_campo_minato()
    mine_trovate = 0

    while mine_trovate < 5:
        stampa_campo(campo)

        try:
            riga = int(input("Inserisci la riga: "))
            colonna = int(input("Inserisci la colonna: "))
        except ValueError:
            print("Inserisci coordinate valide.")
            continue

        if 0 <= riga < 5 and 0 <= colonna < 5:
            if campo[riga][colonna] == 'X':
                print("Hai colpito una mina! Game over.")
                break
            elif campo[riga][colonna] == ' ':
                print("Hai trovato una cella senza mina!")
                mine_trovate += 1
                campo[riga][colonna] = 'O'
            else:
                print("Hai già controllato questa cella.")
        else:
            print("Coordinate non valide. Inserisci coordinate tra 0 e 4.")

    if mine_trovate == 5:
        print("Congratulazioni! Hai trovato tutte le celle senza mine.")

# if __name__ == "__main__":
gioca()
