import numpy as np
import sys

def gauss_elimination(a ,b):
    n = len(b)
    x = np.zeros(n, float)

    for k in range(n - 1):
        if np.fabs(a[k, k]) < 1.0e-12:

            for i in range(k + 1, n):
                if np.fabs(a[i, k]) > np.fabs(a[k, k]):
                    a[[k, i]] = a[[i, k]]
                    b[[k, i]] = b[[i, k]]
                    break

        for i in range(k + 1, n):
            if a[i, k] == 0: continue

            factor = a[k, k] / a[i, k]
            for j in range(k, n):
                a[i, j] = a[k, j] - a[i, j] * factor

            b[i] = b[k] - b[i] * factor
    print(a)
    print(b)

    if a[n - 1, n - 1] == 0 :
        print("DZIELENIE PRZEZ ZERO")
        return

    x[n - 1] = b[n - 1] / a[n - 1, n - 1]
    for i in range(n - 2, -1, -1):
        sum_ax = 0

        for j in range(i + 1, n):
            sum_ax += a[i, j] * x[j]

        x[i] = (b[i] - sum_ax) / a[i, i]

    print("Rozwiązanie: ")
    print(x)

if __name__ == '__main__':
    print("Dla wartości z pliku A: ")
    file = open("gauss1.txt", 'r')

    line = file.readline().split()
    niewiadome = int(line[2])
    line = file.readline().strip().split()
    B = np.zeros([5,1])
    for i in range(niewiadome):
        B[i,0] = line[i]
    print(B)

    line = file.readline().rstrip()
    A = np.loadtxt("gauss1.txt", skiprows=2,  delimiter=' ')
    print(A)


    line = file.readline().split()


    gauss_elimination(A ,B)

    print("##################################")
    print("Dla wartości z pliku B: ")
    file = open("gauss2.txt", 'r')

    line = file.readline().split()
    niewiadome = int(line[2])
    line = file.readline().strip().split()
    B = np.zeros([5, 1])
    for i in range(niewiadome):
        B[i, 0] = line[i]
    print(B)

    line = file.readline().rstrip()
    A = np.loadtxt("gauss2.txt", skiprows=2, delimiter=' ')
    print(A)

    line = file.readline().split()

    gauss_elimination(A, B)

    print("##################################")
    print("Dla wartości z pliku A: ")
    file = open("gauss3.txt", 'r')

    line = file.readline().split()
    niewiadome = int(line[2])
    line = file.readline().strip().split()
    B = np.zeros([5, 1])
    for i in range(niewiadome):
        B[i, 0] = line[i]
    print(B)

    line = file.readline().rstrip()
    A = np.loadtxt("gauss3.txt", skiprows=2, delimiter=' ')
    print(A)

    line = file.readline().split()

    gauss_elimination(A, B)

