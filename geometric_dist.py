import math
num,den=list(map(int,input().split()))
n=int(input())
x=5
p=num/den  #probabiity of success
q=1-p		#probabiity of failure
geom_dist=0
for i in range(1,x+1):
    geom_dist+=q**(n-i)*p

print(round(geom_dist,3))
