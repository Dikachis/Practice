#!/usr/bin/python3

import cmath
import math


def findRoot(a, b, c):
    dis = (b**2 - (4 * a * c))
    root1 = (- b + (cmath.sqrt(dis)))/(2*a)
    root2 = (- b - (cmath.sqrt(dis)))/(2*a)
    print(root1)
    print(root2)
    
    if dis > 0:
        root1 = (- b + (math.sqrt(dis)))/(2*a)
        root2 = (- b - (math.sqrt(dis)))/(2*a)
        print("Print two Real and Distintive roots: root1 = %.2f and root2 = %.2f" %(root1, root2))
    elif dis == 0:
        root1 = (- b )/(2*a)
        root2 = (- b )/(2*a)
        print("Print two Real and Equal roots: root1 = %.2f and root2 = %.2f" %(root1, root2))
    elif dis < 0:
        # root =   Real part         Imaginary part
        # root1 = (- b )/(2*a) + (math.sqrt(dis))/(2*a)
        # root2 = (- b )/(2*a) + (math.sqrt(dis))/(2*a)
        # for Real part ->
        root1 = root2 = (- b )/(2*a)
        # for Imaginary ->
        imaginary = math.sqrt(-dis)/(2*a)
        print("Print two complex and Distintive roots: root1 = %.2f+%.2f and root2 = %.2f-%.2f" %(root1, imaginary, root2, imaginary))


a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

findRoot(a, b, c)
