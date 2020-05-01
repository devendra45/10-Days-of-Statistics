
n=int(input())
x=list(map(float,input().split()))
y=list(map(float,input().split()))

x_sort=sorted(x)
y_sort=sorted(y)

#rank of each element in x
x_rank=[x_sort.index(i)+1 for i in x_sort]  

#rank of each element in y 
y_rank=[y_sort.index(i)+1 for i in y_sort]

x_dict=dict(zip(x_sort,x_rank))
y_dict=dict(zip(y_sort,y_rank))
# square of difference between ranks of x and y
d_sq=[(x_dict[x[i]]-y_dict[y[i]])**2 for i in range(n)]
# spearman_coeff
rxy=1-((6*sum(d_sq))/(n*((n**2)-1)))
print(round(rxy,3))
