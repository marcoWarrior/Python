# strutture_dati.py

# Stringhe
miostringa = "Ciao mondo"

# Metodi comuni per le stringhe:
# Lunghezza della stringa
lunghezza = len(miostringa)

# Convertire in maiuscolo
maiuscolo = miostringa.upper()

# Convertire in minuscolo
minuscolo = miostringa.lower()

# Sostituire una sottostringa
nuova_stringa = miostringa.replace('Ciao', 'Salve')

#Invertire una stringa
stringa_inversa = miostringa[::-1]
###################################################################
# Liste
mialista = [1, 2, 3, 'quattro']

# Funzioni/Metodi comuni per le liste:
# Aggiunta di un elemento alla fine
mialista.append(5)

# Rimozione di un elemento specifico
mialista.remove(2)

# Indice di un elemento
indice = mialista.index('quattro')

# Conteggio delle occorrenze di un elemento
conteggio = mialista.count(3)

# Ordinamento della lista
mialista.sort()
###################################################################
# Tuple
mitupla = (1, 2, 3, 'quattro')
###################################################################
# Insiemi
mioset = {1, 2, 3, 3, 3}

# Metodi comuni per gli insiemi:
# Aggiunta di un elemento
mioset.add(4)

# Rimozione di un elemento specifico
mioset.remove(2)

# Unione di due insiemi
altroset = {3, 4, 5}
unione = mioset.union(altroset)
###################################################################
# Dizionari
miodizionario = {'chiave1': 'valore1', 'chiave2': 'valore2'}

# Metodi comuni per i dizionari:
# Ottenere un valore tramite chiave
valore = miodizionario['chiave1']

# Aggiunta di una nuova coppia chiave-valore
miodizionario['chiave3'] = 'valore3'

# Rimozione di una coppia chiave-valore
del miodizionario['chiave2']

# Controllo se una chiave è presente
presente = 'chiave1' in miodizionario
###################################################################
# Liste concatenate (deque)
from collections import deque
miadeque = deque([1, 2, 3])

# Metodi comuni per le deque:
# Aggiunta di un elemento alla fine
miadeque.append(4)

# Rimozione di un elemento dalla fine
ultimo_elemento = miadeque.pop()
###################################################################
# Array
from array import array
mioarray = array('i', [1, 2, 3])

# Metodi comuni per gli array:
# Aggiunta di un elemento alla fine
mioarray.append(4)

# Rimozione di un elemento specifico
mioarray.remove(2)

# Matrici (numpy.array)
import numpy as np
miomatrice = np.array([[1, 2, 3], [4, 5, 6]])
###################################################################
# Code (Queue)
from queue import Queue
miafila = Queue()

# Metodi comuni per le code:
# Inserimento di un elemento
miafila.put(1)

# Rimozione di un elemento
elemento_rimosso = miafila.get()

###################################################################
# Pile (LifoQueue)
from queue import LifoQueue
miapila = LifoQueue()

# Metodi comuni per le pile:
# Inserimento di un elemento
miapila.put(1)

# Rimozione di un elemento
elemento_rimosso_pila = miapila.get()
