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

def plot(spline, pMedios, datosCrudos, fname="p3_plot.png", hasSave=False):
    x = np.linspace(0, 25, num=100)
    plt.cla()
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Aceleración de la Cápsula (m/s^2)")
    plt.title("Datos Telemetricos Capsula de reentrada")

    plt.fill_between(datosCrudos[0], datosCrudos[1], color='gray', alpha=0.3, edgecolor='black', lw=1.0, label="Aproximaciones trapezoidales")
    plt.vlines(x=datosCrudos[0], ymin=0, ymax=datosCrudos[1], color='black', ls=":", alpha=0.3, lw=0.8)
    plt.scatter(datosCrudos[0], datosCrudos[1], marker='+', c='b', lw=1.2, label="Datos Telemetricos", zorder=5)
    plt.plot(x, spline(x), c='green', lw=1, ls='-', label="Spline Cúbico Ajustado")

    plt.legend(loc="upper right", fontsize="small")

    if hasSave:
        plt.savefig(fname, dpi=300, bbox_inches="tight")
    plt.show()

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
        
        print(f"Intervalo [{x_i} <= x < {x_next}]:")
        print(f"S_{i}(x) = {d:.4f}(x - {x_i})^3 + {c:.4f}(x - {x_i})^2 + {b:.4f}(x - {x_i}) + {a:.4f}\n")
    
def deltaV(t, a, n=100, bc_type=None, showFuncs=False, hasPlot=False):
    # Crear el spline usando scipy
    if not bc_type:
        bc_type = 'not-a-knot' # Para el print al final de la función
        spline = CubicSpline(t, a)
    else:
        spline = CubicSpline(t, a, bc_type=bc_type)

    # Imprimir el spline ajustado
    if showFuncs:
        printFuncs(spline)

    # Configuracion regla punto medio con malla uniforme
    t0, tf = t[0], t[-1]
    h = (tf-t0)/n # Ancho del subintervalo uniforme

    i = np.arange(n)
    m = t0 + (i + 0.5) * h # Puntos medios

    # Calculo delta v
    dV = h * np.sum(spline(m))

    if hasPlot:
        datosCrudos = [t, a]
        plot(spline, m, datosCrudos, fname="p3_plot.png", hasSave=True)
    
    print(f"El valor aproximado de deltaV con spline cubico({bc_type}) es : {dV:.4f} m/s")

deltaV(np.array(t), np.array(a), bc_type='natural') # Para mostrar gráfico agregar el argumento hasPlot=True. Para mostrar el ajust agregar showFuncs=True