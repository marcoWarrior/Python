# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 10:02:16 2019

@author: Docente
"""

from numpy import *
def potenze(A,y0,tol=1e-10,kmax=500):
    """
    Metodo delle potenze 
    con tecnica di normalizzazione (norma 2)
    A: matrice quadrata che ammette autovalore dominante
    y0: vettore iniziale dell'iterazione
    tol: precisione richiesta
    kmax: numero max di iterazioni consentite
    """
    [m,n]=shape(A)
    arresto=False
    k=0
    z0=y0/linalg.norm(y0)
    sigma0=0
    while not(arresto) and k<=kmax:
        k=k+1
        t1=dot(A,z0)
        z1=t1/linalg.norm(t1)
        sigma1=sum(t1*z0)
        Er=abs(sigma1-sigma0)/abs(sigma1)
        arresto=Er<tol
        z0=z1
        sigma0=sigma1 
    if not(arresto):
        print("successione non convergente")
    return sigma1, z1
        
        
    
    
    
    
    
    
    
    
    
    
    