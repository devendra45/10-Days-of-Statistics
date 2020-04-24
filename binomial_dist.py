import math
boy_ratio,girl_ratio=list(map(float,input().split()))
p=boy_ratio/(boy_ratio+girl_ratio)  #succes prob
q=1-p  # failure prob
n=6    # number of trials
x=3    # atleat three are boys
prob_x=0
for i in range(x):
    prob_x+=(math.factorial(n)*(p**i)*(q**(n-i)))/(math.factorial(n-i)*math.factorial(i))
print(round(1-prob_x,3))   # 1- atmost(3)
