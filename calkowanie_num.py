import numpy as np



def trap(l, u, dx,wsp):
    x = np.arange(l,u,dx)
    wsp = np.flip(wsp)

    y = horner(wsp, x)
    return 0.5*dx*(y[0] + y[-1] + 2 * np.sum(y[1:-1]))

def trapcos(l, u, dx, n):
    h = (u - l) / (n - 1)
    x = np.linspace(l, u, n)
    f = x*x*np.cos(x)*np.cos(x)*np.cos(x)

    return (h / 2) * (f[0] + 2 * sum(f[1:n - 1]) + f[n - 1])



def simpson(a, b, n, wsp):
    if n % 2:
        raise ValueError("n must be even (received n=%d)" % n)
    wsp = np.flip(wsp)

    h = (b - a) / n
    s = horner(wsp, a) + horner(wsp, b)

    for i in range(1, n+1, 2):
        s += 4 * horner(wsp, a + i*h)
    for i in range(2, n-1, 2):
        s += 2 * horner(wsp, a + i*h)

    return s * h / 3


def horner(ai, x):
    n = len(ai)
    result = ai[0]
    for i in range(1, n):
        result = result * x + ai[i]
    return result



if __name__ == '__main__':
    file = open("kwadratury_gr_3.txt", 'r')

    line = file.readline().split()
    stopien = int(line[2])

    gr = []
    line = file.readline().strip().split()
    line = file.readline().strip().split()
    ai = np.zeros([5, 1])
    for i in range(stopien+1):
        ai[i, 0] = line[i]

    line = file.readline().split()
    line = file.readline().split()
    for i in line:
        gr.append(int(i))

    print("Metoda trapezu: ")
    print(trap(gr[0], gr[1], 0.0001, ai))


    print("Metoda Simpsona: ")
    print(simpson(gr[0], gr[1], 10000, ai))



    print("Calka: ")
    print(trapcos(2,6, 0.0001, 100))



    print(" Porownanie: ")
    print("Podaj i: ")
    i = int(input())
    for x in range(i,10000):
        print("trapez")
        print(trap(gr[0], gr[1], i, ai))
        print("Simpson")
        print(simpson(gr[0], gr[1], i, ai))
        i ** 10


