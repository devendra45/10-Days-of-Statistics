u,std=list(map(float,input().split()))
x0=float(input())
x1,x2=list(map(float,input().split()))
import math
cdf = lambda x: 0.5 * (1 + math.erf((x - u) / (std * (2 ** 0.5))))

# Less than 19.5
print('{:.3f}'.format(cdf(x0)))
# Between 20 and 22
print('{:.3f}'.format(cdf(x2) - cdf(x1)))