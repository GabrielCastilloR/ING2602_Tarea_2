# -*- coding:utf-8 -*-
"""
Autor: Gabriel Castillo Rosales

Objetivo: Resolver el sistema
    x + y = 20
    (x + sqrt(x))*(y + sqrt(y)) = 155.55
"""
import numpy as np
import matplotlib.pyplot as plt

# Definicion funciones del sistema
f = lambda x,y : x + y - 20
g = lambda x,y : (x + np.sqrt(x))*(y + np.sqrt(y)) - 155.55

# Definicion Jacobiana y computo del vector de cambio (dx, dy)
J = lambda x,y : np.array([[1 , 1],[((np.sqrt(x) + 2*x)/(2*x))*(y+np.sqrt(y)), ((np.sqrt(y) +2*y)/(2*y))*(x+np.sqrt(x))]])
b = lambda x,y : -1*np.array([f(x,y), g(x,y)])

def newtonRaphson(p0, tol):
    p0 = p0
    jacobiana = J(p0[0],p0[1])
    vectorB = b(p0[0],p0[1])
    vectorDelta = np.linalg.solve(jacobiana, vectorB)
    p1 = p0 + vectorDelta
    error = np.max(np.abs(vectorDelta))
    counter = 1
    print("="*75)
    print(f"n = {counter}\n    p = {p1}\n    error = {error}")
    while (error >= 10**tol):
        p0 = p1
        jacobiana = J(p0[0],p0[1])
        vectorB = b(p0[0],p0[1])
        vectorDelta = np.linalg.solve(jacobiana, vectorB)
        p1 = p0 + vectorDelta
        error = np.max(np.abs(vectorDelta))
        counter += 1
        print("="*75)
        print(f"n = {counter}\n    p = {p1}\n    error = {error}")


newtonRaphson(np.array([11.0,9.0]), -4)