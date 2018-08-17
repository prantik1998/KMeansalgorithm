import matplotlib.pyplot as plt 
import math
# k=[2,3,4,10,11,12,20,25,30]
# a=k[0]
# b=k[len(k)-1]
# cluster_a=list()
# cluster_b=list()
# for i in range(len(k)):
# 	if abs(k[i]-a)<abs(k[i]-b):
# 		cluster_a.append(k[i])
# 	else:
# 		cluster_b.append(k[i])
# while sum(cluster_a)/len(cluster_a) !=a and sum(cluster_b)/len(cluster_b)!=b:
# 	a=sum(cluster_a)/len(cluster_a)
# 	b=sum(cluster_b)/len(cluster_b)
# 	cluster_a=list()
# 	cluster_b=list()
# 	for i in range(len(k)):
# 		if abs(k[i]-a)<abs(k[i]-b):
# 			cluster_a.append(k[i])
# 		else:
# 			cluster_b.append(k[i])
# print(a)
# print(b)
# print(cluster_a)
# print(cluster_b)
dataset=[[1,2],[2,2],[2,1],[-1,4],[-2,-1],[-1,-1]]
mean1=dataset[0]
mean2=dataset[len(dataset)-1]
cluster_1=list()
cluster_2=list()

def E_distance(a,b):
	return math.pow(math.pow(a[1]-b[1],2)+math.pow(a[0]-b[0],2),0.5)
for i in dataset:
	if E_distance(i,mean1)<E_distance(i,mean2):
		cluster_1.append(i)
	else:
		cluster_2.append(i)
def average(a):
	centroid=[0,0]
	centroid[0]=sum(a[i][0] for i in range(len(a)))/len(a)
	centroid[1]=sum(a[i][1] for i in range(len(a)))/len(a)
	return centroid
while average(cluster_1)!=mean1 and average(cluster_2)!=mean2:
	mean1=average(cluster_1)
	mean2=average(cluster_2)
	cluster_1=list()
	cluster_2=list()
	for i in dataset:
		if E_distance(i,mean1)<E_distance(i,mean2):
			cluster_1.append(i)
		else:
			cluster_2.append(i)
print(mean1)
print(mean2)
print(cluster_1)
print(cluster_2)





