from time import time
import numpy as np


def _poly_newton_coefficient(x, y):

    m = len(x)

    x = np.copy(x)
    a = np.copy(y)
    for k in range(1, m):
        a[k:m] = (a[k:m] - a[k - 1])/(x[k:m] - x[k - 1])

    return a

def newton_polynomial(x_data, y_data, x):

    a = _poly_newton_coefficient(x_data, y_data)
    n = len(x_data) - 1
    p = a[n]

    for k in range(1, n + 1):
        p = a[n - k] + (x - x_data[n - k])*p

    return p

def horner(ai, x):
    ai = np.flip(ai)
    n = len(ai)
    result = ai[0]
    for i in range(1, n):
        result = result * x + ai[i]
    return result

def postac_nat(a, x):
    w=0
    for i in range(len(a)):
        w += a[i] * (x**i)
    return w

if __name__ == '__main__':

###########################################
   file = open("horner.txt", 'r')
   line = file.readline().split()
   wspolczynniki = []
   for i in line:
      wspolczynniki.append(float(i[3:]))
   X = file.readline().split()
   X_float = []
   for x in X:
       X_float.append(float(x))

   print("Postac Hornera - czas")
   t1 = time()
   for i in X_float:
      horner(wspolczynniki, i)
   t2 = time()
   horner_czas = t2 - t1
   print(horner(wspolczynniki, i))
   print(horner_czas)


   print("Postac naturalna - czas")
   t1 = time()
   for i in X_float:
      postac_nat(wspolczynniki, i)
   t2 = time()
   nat_czas = t2 - t1
   print(postac_nat(wspolczynniki, i))
   print(nat_czas)

   file.close()
   print("###########################")
###########################################

   plik = open("newton.txt", 'r')
   line = plik.readline().split()

   iksy_float = []
   igrek_float = []
   for x in line:
      iksy_float.append(float(x))


   line = plik.readline().split()
   for y in line:
      igrek_float.append(float(y))

   punkt = float(input("Podaj wartość xp: "))
   print(_poly_newton_coefficient(iksy_float, igrek_float))
   print(newton_polynomial(iksy_float,igrek_float, punkt))

