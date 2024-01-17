# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 09:17:45 2021
@author: marcoWarrior
"""
from numpy import *

def bisezioni_sceltaErrore(f, a, b, tol=1e-10, itmax=100):
    """
    Metodo delle successive bisezioni con criterio di arresto relativo
    ----------------------------------------------------------------
    Sintassi
    --------
    alpha, iterazioni = bisezioni_sceltaErrore(f, a, b, tol=1e-10, itmax=100)

    Dati di input
    -------------
    f: funzione di cui calcolare uno zero
       
    [a, b]: intervallo di lavoro
     
    rel_tol: precisione relativa richiesta
      
    itmax: numero massimo di iterate consentite
     
    Dati di output
    -------------- 
    c: approssimazione di uno zero di f(x) 
     
    it: numero di iterate eseguite

    Autore: MarcoWarrior
    """
    fa = f(a) 
    print("fa = ", fa)
    fb = f(b) 
    print("fb = ", fb)
    if fa * fb > 0:  
        print("La funzione non cambia segno agli estremi dell'intervallo")
        return

    scelta = ""  # Inizializzazione della variabile scelta
    while (scelta != "1" and scelta != "2" and scelta != "3"):
        print("Scegli il criterio di arresto:\n'1' Per Assoluto\n'2' Per Relativo\n'3' Per Misto\n")
        scelta = input()
    arresto = False 
    it = 0 
    while not(arresto) and it < itmax:
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
            arresto = abs(b - a) < tol  # "Errore assoluto" arresto==True se b-a<tol
        elif scelta == "2":
            try:
                arresto = (b - a) / min(abs(a), abs(b)) < tol  # "Errore relativo"
            except ZeroDivisionError:               
                print("Attenzione: divisione per zero nel criterio di arresto relativo")
                arresto = False  # Gestisci il caso di divisione per zero
        else:
            arresto = (b - a) / (1 + min(abs(a), abs(b))) < tol  # "Errore misto"
    if not(arresto):  # arresto == False
        print("Attenzione: precisione non raggiunta")
        
    print("Approssimazione di alpha:", c)
    print("Iterate eseguite:", it)
    return c, it

def f(x, ord=0): 
    if ord == 0:
        y = x - cos(x)
    elif ord == 1:
        y = 1 + sin(x)
    else:
        print("ordine di derivazione non definito")
        return
    return y

def g(x, ord=0):
    if ord == 0:
        y = x - exp(-x) 
    elif ord == 1:
        y = 1 + exp(-x)
    else:
        print("ordine di derivazione non definito")
        return
    return y

def main():
    # Chiamata alla funzione bisezioni
    print("\nSintassi funzione:\nalpha, iterazioni = bisezioni_sceltaErrore(f, a, b, tol=1e-10, itmax=100)\nValori consigliati per 'a' e 'b': [0, 1]")
    a = float(input("Inserisci il valore di 'a': "))
    b = float(input("Inserisci il valore di 'b': "))
    alpha, iterazioni = bisezioni_sceltaErrore(f, a, b)

    # Chiamata alla funzione newton
    """
    x0 = 0.5
    alpha_newton, iterazioni_newton = newton(g, x0)
    print("Risultato newton:")
    print("Approssimazione di alpha:", alpha_newton)
    print("Iterazioni eseguite:", iterazioni_newton)
    """

# Chiamata alla funzione main per eseguire il programma
main()


"""
Esempio utilizzo senza main:

>>> import bisezioni_alternative as bs
>>> alpha, iterazioni = bs.bisezioni_sceltaErrore(bs.f, 0, 1)   

"""
