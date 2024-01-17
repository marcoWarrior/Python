# -*- coding: utf-8 -*-
"""
Created on Mon Oct 4 09:17:45 2021
@author: marcoWarrior
"""
from numpy import *
import matplotlib.pyplot as plt

def bisezioni_sceltaErrore(f, a, b, tol=1e-10, itmax=100, scelta=""):
    """
    Metodo delle successive bisezioni con criterio di arresto relativo
    ...
    """
    fa = f(a)    
    fb = f(b)    
    if fa * fb > 0:  
        print("La funzione non cambia segno agli estremi dell'intervallo")
        return
    arresto = False 
    it = 0 

    # Lista per salvare l'approssimazione di alpha ad ogni passo
    alpha_list = []
    # Lista per salvare il numero di iterate eseguite ad ogni passo
    iterate_list = []

    while not arresto and it < itmax:
        it += 1
        c = (a + b) / 2 
        fc = f(c)
        if fc == 0: 
            return c, it
        elif fa * fc < 0:
            b = c
        else:
            a = c
            fa = fc
        if scelta == "1":
            arresto = (b - a) < tol  # "Errore assoluto" arresto==True se b-a < tol
        elif scelta == "2": 
            arresto = (b - a) / min(abs(a), abs(b)) < tol  # "Errore relativo"
        else:
            arresto = (b - a) / (1 + min(abs(a), abs(b))) < tol  # "Errore misto"
        
        # Salviamo l'approssimazione di alpha e il numero di iterate nella lista
        alpha_list.append(c)
        iterate_list.append(it)

    if not arresto:  # arresto == False
        print("Attenzione: precisione non raggiunta")
        
    print("Approssimazione di alpha:", c)
    print("Iterate eseguite:", it)
    return c, it, alpha_list, iterate_list

def f(x, ord=0): 
    if ord == 0:
        y = x - cos(x)
    elif ord == 1:
        y = 1 + sin(x)
    else:
        print("ordine di derivazione non definito")
        return
    return y


def main():
    # Chiamata alla funzione bisezioni
    print("\nSintassi funzione:\nalpha, iterazioni = bisezioni_sceltaErrore(f, a, b, tol=1e-10, itmax=100)\nEsempio per 'a' e 'b': [0.5, 2]")
    a = float(input("Inserisci il valore di 'a': "))
    b = float(input("Inserisci il valore di 'b': "))
    scelta = ""  # Inizializzazione della variabile scelta
    while scelta not in ["1", "2", "3"]:
        print("Scegli il criterio di arresto:\n'1' Per Assoluto\n'2' Per Relativo\n'3' Per Misto\n")
        scelta = input()
    if scelta == "1":
        t = 1e-10
        errore_scelto = "Errore Assoluto"
    elif scelta == "2":
        t = 1e-8
        errore_scelto = "Errore Relativo"
    else:
        t = 1e-6
        errore_scelto = "Errore Misto"
        
    alpha, iterazioni, alpha_list, iterate_list = bisezioni_sceltaErrore(f, a, b, tol=t, itmax=100, scelta=scelta)

    # Creazione del grafico
    plt.plot(iterate_list, alpha_list, marker='o', linestyle='-')
    plt.xlabel('Iterate eseguite')
    plt.ylabel('Approssimazione di alpha')
    plt.title(f'Metodo delle bisezioni: {errore_scelto}')
    plt.grid(True)
    plt.show()

# Chiamata alla funzione main per eseguire il programma
main()
