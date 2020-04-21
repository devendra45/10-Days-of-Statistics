
n=int(input())
list1=list(map(int,input().split()))
#mean
print(sum(list1)/len(list1))

#median
list1.sort()
length=len(list1)

if length%2==0:     #if length is even
    median=(list1[length//2]+list1[(length//2)-1])/2
else: #if length is odd
    median=(list1[length//2])
print(median)

occ={x:list1.count(x) for x in list1}  # occurence of element saved in a dictionary
# k=list(occ.keys())
# v=list(occ.values())
if len(occ)==len(list1):
    print(list1[0])
else:
    print( max(occ.keys(), key=(lambda k: occ[k])))
