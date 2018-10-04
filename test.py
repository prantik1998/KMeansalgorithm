
import math

dataset=[[1,2],[2,2],[2,1],[-1,4],[-2,-1],[-1,-1]] #This is going to be our sample dataset
mean1=dataset[0] #Initializing First Mean/Centroid
mean2=dataset[len(dataset)-1] #Initializing Second Mean/Centroid
cluster_1=list()#First cluster
cluster_2=list()#First cluster

def E_distance(a,b):
	return math.pow(math.pow(a[1]-b[1],2)+math.pow(a[0]-b[0],2),0.5) #Computing the Euclidean Distance between two points
for i in dataset:
	if E_distance(i,mean1)<E_distance(i,mean2):
		cluster_1.append(i)#Clustering the elements
	else:
		cluster_2.append(i)#Clustering the elements
def average(a):    #Used for finding the centroid of all the points belonging to that cluster
	centroid=[0,0]
	centroid[0]=sum(a[i][0] for i in range(len(a)))/len(a)
	centroid[1]=sum(a[i][1] for i in range(len(a)))/len(a)
	return centroid
while average(cluster_1)!=mean1 and average(cluster_2)!=mean2:#Condition for stopping the K-Means Algorithms
	
	mean1=average(cluster_1)#The first new mean/centroid
	mean2=average(cluster_2)#The second new mean/centroid
	cluster_1=list()
	cluster_2=list()
	for i in dataset:
		if E_distance(i,mean1)<E_distance(i,mean2):
			cluster_1.append(i)#Forming the new cluster
		else:
			cluster_2.append(i)#Forming the new cluster
print(mean1)			
print(mean2)
print(cluster_1)
print(cluster_2)





