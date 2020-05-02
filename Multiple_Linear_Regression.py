import numpy as np
m,n = [int(i) for i in input().strip().split(' ')]
x=[]
y=[]
for i in range(n):
        data=list(map(float,input().split()))
        x.append(data[:m])
        y.append(data[m:])
q=int(input().strip())
x_new=[]
for i in range(q):
    data_new=list(map(float,input().split()))
    x_new.append(data_new)
features=[i.insert(0,1) for i in x]
features_new=[i.insert(0,1) for i in x_new]
X=np.array(x,float)
Y=np.array(y,float)
X_new=np.array(x_new,float)
beta=np.dot(np.linalg.inv(np.dot(X.T,X)),np.dot(X.T,Y))

Y_new=np.dot(X_new,beta)
predict_y=Y_new.flatten()
for i in predict_y:
    print(round(i,2))


