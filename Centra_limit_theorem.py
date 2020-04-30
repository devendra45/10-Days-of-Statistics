x=int(input())
n=int(input())
u=float(input())
std=float(input())
import math
mu=n*u
sigma=std*(n**0.5)

def cdf(x, mu, sigma):
    Z = (x - mu)/sigma
    return 0.5*(1 + math.erf(Z/(math.sqrt(2))))
print(round(cdf(x, mu, sigma),4))
