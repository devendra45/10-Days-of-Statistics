# Pearson Coefficient
n=int(input())
x=list(map(float,input().split()))
y=list(map(float,input().split()))

mx=sum(x)/n #mean x
my=sum(y)/n  #mean Y
varx=sum([(i-mx)**2 for i in x])/n   #variance x
vary=sum([(i-my)**2 for i in y])/n	 #variance y
stdx=varx**0.5   					#std deviation x
stdy=vary**0.5						#std deviation y
#print(mx,stdx,my,stdy)
x=[(i-mx) for i in x]
y=[(i-my) for i in y]  
pxy=0
for i in range(n):
    pxy+=x[i]*y[i]/(n*stdx*stdy)
print(round(pxy,3))
