# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 09:17:45 2021

@author: felix
"""
from numpy import *
       
def bisezioni(f,a,b,tol=1e-10,itmax=100):
    """
    Metodo delle successive bisezioni
    ---------------------------------
    Sintassi
    --------
      alpha=bisezioni(f,a,b,tol)

    Dati di input
    -------------    
      f: funzione di cui calcolare uno zero
       
      [a,b]: intervallo di lavoro
     
      tol: precisione richiesta
      
      itmax: numero massimo di iterate consentite
     
    Dati di output
    -------------- 
       c: approssimazione di uno zero di f(x) 
     
      it: numero di iterate eseguite

    ..
    """
    fa=f(a) 
    fb=f(b) 
    if fa*fb>0:
        print('La funzione non cambia segno agli estremi dell''intervallo')
        return
    arresto=False 
    it=0 # contatore di iterate
    while not(arresto) and it<itmax:
        it=it+1
        c=(a+b)/2
        fc=f(c)
        if fc==0:
            return c,it
        elif fa*fc<0:
            b=c
        else:
            a=c
            fa=fc
        arresto=b-a<tol # arresto==True se b-a<tol
    if not(arresto): # arresto==False
        print('Attenzione: precisione non raggiunta')
    return c,it
    
    
    
def f(x,ord=0): 
    if ord==0:
        y=x-cos(x)
    elif ord==1:
        y=1+sin(x)
    else:
        print('ordine di derivazione non definito')
        return
    return y

def g(x,ord=0):
    if ord==0:
        y=x-exp(-x)
    elif ord==1:
        y=1+exp(-x)
    else:
        print('ordine di derivazione non definito')
        return
    return y


def newton(f,x0,tol=1e-10,itmax=100):
    """
    Metodo delle successive bisezioni
    ---------------------------------
    Sintassi
    --------
      alpha=newton(f,x0,tol,itmax)

    Dati di input
    -------------    
      f: funzione di cui calcolare uno zero
       
      x0: stima iniziale dello zero di f
     
      tol: precisione richiesta
      
      itmax: numero assimo di iterate consentite
     
    Dati di output
    -------------- 
      x1: approssimazione di uno zero di f(x) 
     
      it: numero di iterate eseguite

    Autore: F. Iavernaro
    """
    arresto=False
    it=0 # contatore di iterate
    while not(arresto) and it<itmax:
        it=it+1
        x1=x0-f(x0)/f(x0,1)
        arresto=abs(x1-x0)<tol
        x0=x1
    if not(arresto):
        print('Attenzione: precisione non raggiunta')
    return x1,it