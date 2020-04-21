n=int(input())
x=list(map(int,input().split()))   # list of element
w=list(map(int,input().split()))   # weight of an element
sumw=sum(w)							# sum of weights
wx=0
for i in range(n):
    wx+=x[i]*w[i]
print(round(wx/sumw,1))
