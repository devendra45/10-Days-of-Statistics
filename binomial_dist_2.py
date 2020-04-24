import math
p,n=list(map(float,input().split()))
p=p/100
q=1-p  # failure prob
x=2    # atleat three are boys
prob_x=0
for i in range(x+1):
    prob_x+=(math.factorial(n)*(p**i)*(q**(n-i)))/(math.factorial(n-i)*math.factorial(i))

atleast_2=1-prob_x+(math.factorial(n)*(p**2)*(q**(n-2)))/(math.factorial(n-2)*2)
print(round(prob_x,3))  # 1- atmost(3)
print(round(atleast_2,3))
