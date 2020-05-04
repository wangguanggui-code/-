# -刚开始学习python
import math

def quadratic(a, b, c):
    if a == 0:
        raise TypeError('0can not be fenmu')
    x1 = (-b + math.sqrt(b**2-4*a*c))/(2*a)
    x2 = (-b - math.sqrt(b**2-4*a*c))/(2*a)
    return x1, x2
