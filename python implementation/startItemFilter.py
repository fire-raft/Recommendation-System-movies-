#acessing already availiable data
from critics import *
from recommendationsUserCF import *
from recommendationItemFilter import *

print(" Item based collaborative filtering  ")

#present user to be substituted for which recommendations are to be suggested
critics['228054']	
{'Fortune': 6.0}

#calculating euclidian distance and pearson correlation for the user
sim_distance(critics,'98556', '180727')			#euclidian distance
sim_pearson(critics,'180727', '177432')		#pearson correlation


#finding top matches of similar users for given user
topMatches(critics,'98556',10,sim_distance)
topMatches(critics,'180727', 3)


#getting the recommendations
u1=getRecommendations(critics,'228054',similarity=sim_distance)[0:10]
u2=getRecommendations(critics,'180727',similarity=sim_distance)[0:4]
#getRecommendedItems(critcs, itemMatch, '228054')
print(u1)
print(u2)
