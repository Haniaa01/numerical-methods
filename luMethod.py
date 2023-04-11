import numpy as np

def multiply_matrix(A,B, niewiadome,kolumny):
  if  A.shape[1] == B.shape[0]:
    C = np.zeros((A.shape[0],B.shape[1]),dtype = int)
    for row in range(niewiadome):
        for col in range(kolumny):
            for elt in range(len(B)):
              C[row, col] += A[row, elt] * B[elt, col]
    return C
  else:
    return "Nie można pomnozyc tych dwoch macierzy :(."

def rozwiazanie(a, b, l, u, niewiadome):
    z = np.zeros_like(b)
    n = niewiadome

    for x in range(n):
        z[x] = b[x]
        for y in range(x):
            z[x] -= l[x, y] * z[y]
        z[x] /= l[x, x]

    x = np.zeros_like(b)
    for i in range(n - 1, -1, -1):
        x[i] = z[i]
        for j in range(i + 1, n):
            x[i] -= u[i, j] * x[j]
        x[i] /= u[i, i]

    return x

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

    return x


def plu(A):
    # Get the number of rows
    n = A.shape[0]

    # Tworzenie permutacji, lower i upper
    U = A.copy()
    L = np.eye(n, dtype=np.double)
    P = np.eye(n, dtype=np.double)

    for i in range(n):

        # Permute rows if needed
        for k in range(i, n):
            if ~np.isclose(U[i, i], 0.0):
                break
            U[[k, k + 1]] = U[[k + 1, k]]
            P[[k, k + 1]] = P[[k + 1, k]]

        factor = U[i + 1:, i] / U[i, i]
        L[i + 1:, i] = factor
        U[i + 1:] -= factor[:, np.newaxis] * U[i]

    return L, U

if __name__ == '__main__':
    file = open("luMethod.txt", 'r')

    line = file.readline().split()
    niewiadome = int(line[2])
    line = file.readline().strip().split()
    B = np.zeros([5, 1])
    for i in range(niewiadome):
        B[i, 0] = line[i]
    print(B)

    line = file.readline().rstrip()
    A = np.loadtxt("luMethod.txt", skiprows=2, delimiter=' ')
    print(A)

    line = file.readline().split()
    lower, upper = plu(A)
    print("Lower: ")
    print(lower)
    print("Upper: ")
    print(upper)
    print("Rozwiazanie")
    rozw = rozwiazanie(A,B, lower, upper, niewiadome)
    print(rozw)

    print("Sprawdzenie poprawności algorytmu")
    print("Ax = b używając napisanej funkcji do mnozenia macierzy")
    print(multiply_matrix(A, rozw, niewiadome, 1))
    print("Ax = b używając napisanej funkcji wbudowanej z NumPy")
    print(np.dot(A, rozw))

