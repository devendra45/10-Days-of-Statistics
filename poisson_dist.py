import math
l=float(input())
k=float(input())
e=2.71828
poisson=(l**k)*(e**(-l))/math.factorial(k)
print(poisson)
