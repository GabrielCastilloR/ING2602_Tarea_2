# -*- coding:utf-8 -*-
"""
Autor: Gabriel Andrés Castillo Rosales
Objetivo: Solución ejercicio 3, implementacion de la regla del punto medio con interpolacion y splines cubicos
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Datos telemetricos
t = [0,2,5,7,12,18,25]
a = [0.0,4.2,14.8,19.1,11.3,3.5,0.2]

def printFuncs(spline):
    # 2. Extract attributes
    coef = spline.c  # Array of shape (4, number_of_intervals)
    nodos = spline.x         # Array of shape (number_of_intervals + 1)

    # 3. Iterate through intervals to print each function
    n = len(nodos) - 1

    for i in range(n):
        # Extract coefficients for the current interval (highest degree to lowest)
        d = coef[0, i]  # Cubic coefficient
        c = coef[1, i]  # Quadratic coefficient
        b = coef[2, i]  # Linear coefficient
        a = coef[3, i]  # Constant coefficient
        
        x_i = nodos[i]          # Starting point of the interval
        x_next = nodos[i+1]     # Ending point of the interval
        
        print(f"Intervalo [{x_i} <= x <= {x_next}]:")
        print(f"S_{i}(x) = {d:.4f}(x - {x_i})^3 + {c:.4f}(x - {x_i})^2 + {b:.4f}(x - {x_i}) + {a:.4f}\n")
    
def deltaV(t,a, bc_type=None):
    # Crear el spline usando scipy
    if not bc_type:
        spline = CubicSpline(t, a)
    else:
        spline = CubicSpline(t, a, bc_type=bc_type)

    # Imprimir el spline ajustado
    printFuncs(spline)

    # Configuracion regla punto medio con malla uniforme
    n = 100
    t0, tf = t[0], t[-1]
    h = (tf-t0)/n # Ancho del subintervalo uniforme

    i = np.arange(n)
    m = t0 + (i + 0.5) * h # Puntos medios

    # Calculo delta v
    return h * np.sum(spline(m))

v = deltaV(np.array(t), np.array(a))
vNat = deltaV(np.array(t), np.array(a), bc_type="natural")
print(f"El valor aproximado de deltaV con comportamiento 'not-a-knot' es : {v:.4f} m/s")
print(f"El valor aproximado de deltaV con comportamiento 'natural' es : {vNat:.4f} m/s")