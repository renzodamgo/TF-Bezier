import numpy as np
from matplotlib import pyplot as plt
# Funcion factorial
def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

# Funcion combinacional
def comb(n, r):
    return fact(n)/(fact(n-r)*fact(r))

def getPoints():
    #Inicializamos los puntos X y Y
    px=[]
    py=[]
    
    n = int(input("Ingresa numero de puntos[3,8]: "))
    for i in range(n):
        print(f'Prunto {i+1}:')
        px.append(int(input("x = ")))
        py.append(int(input("y = ")))
    return px,py,n-1
    
#Bezier en consola
def bezier(px,py,n):
    bx=[]
    by=[]
    for t in np.arange(0,1,0.001):
        sum_x = 0
        sum_y = 0
        for i in range(n+1):
            #x = x+(comb(n, i) * pow((1-t), (n-i)) * pow(t, i) * px[i]);
            sum_x= sum_x+ (comb(n,i)*pow((1-t),(n-i))*pow(t,i)*px[i])
            sum_y= sum_y+ (comb(n,i)*pow((1-t),(n-i))*pow(t,i)*py[i])
        bx.append(sum_x)
        by.append(sum_y)
    return bx,by
    
def cl_bezier():
    px ,py,n = getPoints()
    bx,by = bezier(px,py,n)
    plt.plot(px,py,bx,by)
    plt.show()

cl_bezier()