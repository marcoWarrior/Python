# -*- coding: utf-8 -*-
"""
Programmi introduzione_python.pdf

@author: M.Warrior
"""

from numpy import *
import threading
import time
def eq2(a,b,c):
    """
    Calcola le radici reali di un'equazione di secondo grado ax^2 + bx + c = 0.
    ---------------------------------
    Sintassi
    --------
      radici=eq2(a,b,c)

    Dati di input
    -------------    
      a,b,c: coefficienti dell'equazione di secondo grado
     
    Dati di output
    -------------- 
      tuple or None: una tupla contenente le radici reali dell'equazione se esistono,
                     altrimenti restituisce None

    Autore: M.Warrior
    """
    # Calcolo del discriminante
    discriminante = b**2 - 4*a*c
    if discriminante >= 0:
        radice_discriminante = sqrt(discriminante)
        x1 = (-b + radice_discriminante)/(2*a)
        x2 = (-b - radice_discriminante)/(2*a)
        return (x1,x2)
    else:
        return None    

def inverti(s):
    """
    Funzione inverti
    ---------------------------------
    Sintassi
    ---------------------------------
      inverti(s)
    ---------------------------------
    Dati di input  
    ---------------------------------
      s: stringa di caratteri
    ---------------------------------
    Dati di output
    ---------------------------------
      r: stringa ottenuta invertendo l'ordine dei caratteri di s

    Autore: M.Warrior
    """
    r = ''
    for i in range(len(s)-1, -1, -1): # range(start, stop, step)
        r += s[i] # r = r + s[i]
    return r
    
def MCD(m,n):
    """
    Funzione MCD
    ---------------------------------
    Sintassi
    ---------------------------------
      MCD(m,n)  
    ---------------------------------
    Dati di input
    ---------------------------------
      m: intero positivo
      n: intero positivo  
    ---------------------------------
    Dati di output
    ---------------------------------
      m: massimo comun divisore tra m e n (intero positivo)) 
    ---------------------------------
    Autore: M.Warrior
    """
    while m != n:
        if m > n:
            m = m - n
        else:
            n = n - m
    return m
    
def somma(lista_num):
    """Somma di una lista di numeri
    """ 
    s = 0
    for i in range(len(lista_num)):
        s += lista_num[i]
    return s
  
def media(lista_num):
    """Media di una lista di numeri
    """ 
    return somma(lista_num)/len(lista_num)

def varianza(lista_num):
  """Varianza di una lista di numeri
  """
  media_lista = media(lista_num)
  n = len(lista_num)
  sum_diff_sq = sum((numero - media_lista) ** 2 for numero in lista_num)
  varianza = sum_diff_sq / n
  return varianza

def ordina(x):
  """Ordina una lista di numeri in ordine decrescente
  """
  for i in range(len(x)):
        for j in range(i+1,len(x)):
            if x[i] > x[j]:
                t = x[i]
                x[i] = x[j]
                x[j] = t
  return x

def congetCollaz(x0):
    """La congettura di Collatz afferma che, a prescindere dal punto iniziale x0,
    l'algoritmo raggiunge sempre il valore 1 dopo un numero finito di passi.
    Restituisce una tupla contenente il valore finale 1 e la sequenza completa di valori x0, x1, ..., xn.
    ---------------------------------
    Sintassi
    ---------------------------------
    congetCollaz(x0)
    ---------------------------------
    Dati di input
    ---------------------------------
    x0: intero positivo
    ---------------------------------
    Dati di output
    ---------------------------------
    tupla: (valore_finale, sequenza_valori)
    ---------------------------------
    Autore: M.Warrior
    """
    x = [x0]  # Lista che contiene l'intera sequenza di valori x0, x1, ..., xn.
    while x0 != 1:
        if x0 % 2 == 0:
            x0 = x0 // 2
            x.append(x0)
        else:
            x0 = x0 * 3 + 1
            x.append(x0)
    return (x[-1], x)

def contaVocali(stringa):
	"""Funzione che conta le vocali presenti in una stringa.
	Sono incluse le ripetizioni e la funzione è case-insensitive.
	---------------------------------
	Sintassi
	---------------------------------
	conta_vocali(stringa)
	---------------------------------
	Dati Input
	---------------------------------
	stringa: stringa di caratteri
	---------------------------------
	Dati di output
	---------------------------------
	num_vocali: intero che rappresenta il numero di vocali in stringa
	"""
	num_vocali = 0
	vocali = "aAeEiIoOuU"
	sv = set(vocali)
	for i in range (len(stringa)):
		if stringa[i] in sv:
			num_vocali+=1
	return num_vocali


def contaCarattere():
    '''
    Scrivi una funzione in Python che prenda come input una stringa e restituisca un dizionario contenente la conta di ciascun carattere presente nella stringa.
    Ad esempio, se la stringa è "hello", il dizionario risultante dovrebbe essere {'h': 1, 'e': 1, 'l': 2, 'o': 1}.
    Assicurati di considerare la gestione degli errori e fornisce un esempio di utilizzo della tua funzione.
    '''
    try:
        stringa = input("Inserire una stringa: ")
        
        # Trasforma tutti i caratteri in minuscolo per contare le occorrenze senza distinzione tra maiuscole e minuscole
        stringa = stringa.lower()

        occorrenze = {} # Dizionario
        for carattere in stringa:
            # Se il carattere è presente nel dizionario, incrementiamo il contatore
            if carattere in occorrenze:
                occorrenze[carattere] += 1
            else:
                # Il carattere non è presente nel dizionario, quindi viene aggiunto con contatore 1
                occorrenze[carattere] = 1

        for carattere, conteggio in occorrenze.items():
            print(f"Carattere: {carattere}, Occorrenze: {conteggio}")

    except Exception as e:
        print(f"Errore: {e}")
# contaCarattare()


def listaPari():
    """Funzione che 
	  ---------------------------------
	  Sintassi
	  ---------------------------------
	
	  ---------------------------------
	  Dati Input
	  ---------------------------------
	
	  ---------------------------------
	  Dati di output
	  ---------------------------------
	
	  """
    try:
        input_utente = input("Inserire una lista di numeri separati da una virgola\n")
        numeri_str = input_utente.split(',')
        lista = [int(numero) for numero in numeri_str]
        lista_pari = [num for num in lista if num % 2 == 0] # list comprehension
        print(f"Nuova lista: {lista_pari}")
    except ValueError:
        print("Assicurati di inserire solo numeri separati da una virgola")
    except Exception as e:
        print(f"Errore imprevisto {e}")


def trova_primi_n_primi(n):
    '''Funzione che 
	  ---------------------------------
	  Sintassi
	  ---------------------------------
	
	  ---------------------------------
	  Dati Input
	  ---------------------------------
	
	  ---------------------------------
	  Dati di output
	  ---------------------------------
    '''
    lista_n_primi = []
    i = 2
    while len(lista_n_primi) < n:
        if f_primo(i, lista_n_primi):
            lista_n_primi.append(i)
        i += 1
    return lista_n_primi

def f_primo(numero, lista):
    if not lista:
        return True
    for n in lista:
        if numero % n == 0:
            return False
    return True
# Test:
'''
try:
    input_utente = input("Inserire un intero positivo:\n")
    n = int(input_utente)
    if n <= 0:
        print("Numero inserito negativo o 0")
    elif n == 1:
        print("1 non è un numero primo")
    else:
        lista = trova_primi_n_primi(n)
        print(f"Lista numeri primi:\n {lista}")
except ValueError as e:
    print(f"Valore non valido\n {e}")
'''



# import threading
# import time

def stampa_numero(numero):
    '''Esempio di Thread
	---------------------------------
	Sintassi
	---------------------------------
	
	---------------------------------
	Dati Input
	---------------------------------
	
	---------------------------------
	Dati di output
	---------------------------------
'''
    time.sleep(2)
    print(f"Numero: {numero}")

# Creazione di due thread che eseguono la funzione stampa_numero simultaneamente
thread1 = threading.Thread(target=stampa_numero, args=(1,))
thread2 = threading.Thread(target=stampa_numero, args=(2,))
# Test
'''
thread1.start()
thread2.start()

thread1.join()
thread2.join()
'''

