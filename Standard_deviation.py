n=int(input())
item=list(map(int,input().split()))
#mean
mu=sum(item)/n   #mean
dis=[(x-mu)**2 for x in item]  # squared distance from mean
var=sum(dis)/n					# variance 
std_dev=var**0.5
print(round(std_dev,1))
