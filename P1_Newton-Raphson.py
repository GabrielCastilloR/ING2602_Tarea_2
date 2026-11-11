# -*- coding: utf-8 -*-

"""
Autor: Gabriel Andres Castillo Rosales

Enunciado:
    Implementar el proceso iterativo de Newton-Raphson y encontrar una aproximación de la raíz de la
    la función f(x) en el intervalo [0, pi/2] con error máximo 10^(-9) y 
        f(x) = exp(-x) - sin(x)
    Imprimir el resultado en pantalla, no es necesario graficar.
"""

# Imports
import numpy as np
import matplotlib.pyplot as plt


# Funciones
def saveFile(fname, data):
    try:
        with open(f"{fname}.csv", "w+") as f:
            f.writelines(data)
            f.close()
        print(f"[saveFile] : Data saved as {fname}.csv")
    except:
        print(f"[saveFile] : Could not save data.")

def plot(x, y, xErr, fname):
    plt.cla()
    plt.title("Valores Obtenidos")
    plt.xlabel("Valor aproximado de la raiz")
    plt.ylabel("Valor correspondiente en la función")
    plt.scatter(x,y,marker='+', c='b', lw=0.75, label="Raíces")
    plt.errorbar(x, y, xerr=xErr, ecolor='g',elinewidth=0.75, ls='none', label="Error Absoluto")
    plt.legend(loc="upper right", bbox_to_anchor=(1, 1), fontsize=10, frameon=True, facecolor="white", edgecolor='gray')
    plt.savefig(f"{fname}.png")

f = lambda x : float(np.e**(-x) - np.sin(x))

# Método Newton-Raphson
def newtonRaphson(xStart, xEnd, tol, hasPlot=False, hasSave=False, fname=f"{__file__}"):
    
    # Condiciones Inciales
    r0 = 0.5*(xEnd - xStart)
    f0 = f(r0)
    counter = 0

    # Errores inciales altos
    ea, es = 10**tol + 1, 10**tol + 1

    x, y, xErr = [],[],[]

    # Proceso iterativo
    while (ea >= 10**tol or es >= 10**tol):
        if not (0 <= r0 <= xEnd):
            print(f"[Newton-Raphson] : x = {r0} no está dentro del intervalo [{xStart}, {xEnd}]. Se detuvo la ejecución")
            break
        phi = (f(r0 + f0) - f0)/f0
        r1 = r0 - f0/phi
        f1 = f(r1)

        #Actualizacion errores
        ea = np.abs(r1 -r0)
        es = np.abs(f1)

        #Guardar valores en listas
        x.append(r1)
        y.append(f1)
        xErr.append(ea)

        #Actualizacion puntos
        r0, f0 = r1, f1
        counter += 1

    # Imprimir en pantalla
    print(f"[Newton-Raphson] : Se completo la iteración con {counter} pasos, la raíz es x = {r1}, con error absoluto {ea}")

    if hasPlot:
        plot(x, y, xErr, fname)
    if hasSave:
        outputData = ["i;x_i;f(x_i);epsilon\n"]
        for i in range(0, len(x)-1):
            outputData.append(f"{i};{x[i]};{y[i]};{xErr[i]}\n")
        outputData.append(f"{len(x)-1};{x[-1]};{y[-1]};{xErr[-1]}")
        saveFile(fname, outputData)

newtonRaphson(0, 0.5*np.pi, -9, hasPlot=True, fname="p1_plot")