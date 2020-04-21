N=int(input()) 
element=list(map(int,input().split())) #element list
freq=list(map(int,input().split()))    # no of times an element repeats
item=[]
for i in range(N):
    for j in range(freq[i]):
        item.append(element[i])
n=len(item)
item.sort()
# median of list if len is even
if n%2==0:
    l1=item[:n//2]
    l2=item[n//2:]
    n1=len(l1)
    q1=(l1[n1//2]+l1[(n1-1)//2])/2
    q3=(l2[n1//2]+l2[(n1-1)//2])/2
# median of list if len is odd
else:
    l1=item[:(n//2)]
    l2=item[(n//2)+1:]
    n1=len(l1)
    n2=len(l2)
    # median of sublist if len is odd

    if n1%2!=0:
        q1=l1[n1//2]
        q3=l2[n2//2]
    
        # median of sublist if len is even
    else:
        q1=(l1[n1//2]+l1[(n1-1)//2])/2
        q3=(l2[n1//2]+l2[(n1-1)//2])/2

#interquartile range =q3-q1
print(float(q3-q1))  

