m1,s1=list(map(int,input().split()))
m2,s2=list(map(int,input().split()))
m3,s3=list(map(int,input().split()))
m4,s4=list(map(int,input().split()))
m5,s5=list(map(int,input().split()))

x=[m1,m2,m3,m4,m5]
y=[s1,s2,s3,s4,s5]
n=len(x)
mean_x=sum(x)/n
mean_y=sum(y)/n

sum_xy=sum([x[i]*y[i] for i in range(n)])
sum_of_sq_x=sum([i**2 for i in x])
sq_of_sum_x=(sum(x))**2

m=(n*sum_xy-(sum(x)*sum(y)))/(n*sum_of_sq_x-sq_of_sum_x)
c=mean_y-m*mean_x
y_80=m*80+c
print(round(y_80,3))
