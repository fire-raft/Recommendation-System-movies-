#acessing already availiable data
from critics import *
from recommendationsUserCF import *

print(" User based collaborative filtering  ")

#present user to be substituted for which recommendations are to be suggested
critics['228054']	#pass user id 
{'Fortune': 6.0}	#pass a subsequent rating by the target user

#calculating euclidian distance and pearson correlation for the user
sim_distance(critics,'228054', '180727')	#euclidian distance
sim_pearson(critics,'228054', '177432')		#pearson correlation


#finding top matches of similar users for given user
topMatches(critics,'228054',10)
topMatches(critics,'228054', 3)

#the above code can be shifted to source scripts. Written here only for refrence

#getting the recommendations
u1=getRecommendations(critics,'228054',similarity=sim_distance)[0:10]
u2=getRecommendations(critics,'13359',similarity=sim_distance)[0:4]
print(u1)
print(u2)
