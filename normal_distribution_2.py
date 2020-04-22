u,std=list(map(float,input().split())) # mean,std dev
x80=float(input())
x60=float(input())
import math
# cdf of normal distribution
cdf = lambda x: 0.5 * (1 + math.erf((x - u) / (std * (2 ** 0.5)))) 
cdf80=(1-cdf(x80))*100
cdf_g60=(1-cdf(x60))*100
cdf_l60=cdf(x60)*100
# higher than 80
print('{:.2f}'.format(cdf80))
# greater equal to 60
print('{:.2f}'.format(cdf_g60))
# less than 60
print('{:.2f}'.format(cdf_l60))
