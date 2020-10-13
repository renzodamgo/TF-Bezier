# Funcion factorial
def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

# Funcion combinacional
def comb(n, r):
    return fact(n)/(fact(n-r)*fact(r))


def bezier():
    print("Ingresa numero de puntos:[3,8]")
    n = int(input())
    print(n+5)


bezier()
