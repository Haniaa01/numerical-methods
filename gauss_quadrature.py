import numpy as np
import math

def f_sinus(x):
    return (x**2) * (np.sin(x)**3)
def f_exp(x):
    return (np.exp(x**2)) * (1-x)

def kwadraturagl(waga, f, a, b):
    fun = 0
    licz = 2
    if(waga == 3):
        licz = 4
    if(waga == 4):
        licz = 7

    for i in range(waga):
        fun += tablicaWi[licz-2+i] * f((b-a)/2 * tablicaXi[licz-2+i] + (b+a)/2)
    fun *= (b - a)/2

    print(fun)



tablicaXi = [0.57735, -0.577350,
             0, 0.774597, -0.774597,
             0.339981, -0.339981, 0.861136, -0.861136]

tablicaWi = [1, 1,
             0.888889, 0.555556, 0.555556,
             0.652145, 0.6521450, 0.347855, 0.347855]

if __name__ == '__main__':

    print("Obliczenie calek za pomoca kwadratury 2 - wezlowej: ")
    print("f(x): x^2 * sin^3(x): ", end=' ')
    kwadraturagl(2, f_sinus, 1, 4.8)
    print("f(x): exp(x^2)*(1-x): ", end=' ')
    kwadraturagl(2, f_exp, abs(-1.5), 3.2)
    print('\n')

    print("Obliczenie calek za pomoca kwadratury 3 - wezlowej: ")
    print("f(x): x^2 * sin^3(x): ", end=' ')
    kwadraturagl(3, f_sinus, 1, 4.8)
    print("f(x): exp(x^2)*(1-x): ", end=' ')
    kwadraturagl(3, f_exp, abs(-1.5), 3.2)
    print('\n')

    print("Obliczenie calek za pomoca kwadratury 4 - wezlowej: ")
    print("f(x): x^2 * sin^3(x): ", end=' ')
    kwadraturagl(4, f_sinus, 1, 4.8)
    print("f(x): exp(x^2)*(1-x): ", end=' ')
    kwadraturagl(4, f_exp, abs(-1.5), 3.2)