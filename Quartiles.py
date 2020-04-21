n=int(input())
item=list(map(int,input().split()))
item.sort()
if n%2==0:
    q2=(item[n//2]+item[(n-1)//2])/2
else:
    q2=item[n//2]
l1=[x for x in item if x<q2]
l2=[x for x in item if x>q2]
n1=len(l1)
n2=len(l2)
# if length if item is even
if n1%2==0:
    q1=(l1[n1//2]+l1[(n1-1)//2])/2
    q3=(l2[n2//2]+l2[(n2-1)//2])/2
# if length if item is odd
else:
    q1=l1[n1//2]
    q3=l2[n2//2]
print(int(q1))   #quartile 1 -->median of sublist 1
print(int(q2))   #quartile 2 -->median of list
print(int(q3))   #quartile 3 -->median of sublist 2
