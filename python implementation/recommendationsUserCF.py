from math import sqrt
import scipy as spy
import pandas as pd
import numpy as np

#calculates a distance-base score for user1 and user2

def sim_distance(prefrences, user1, user2):	#prefrences = the data file "critics.py" used as database
	#Get the list of shared_items
	si = {}
	for item in prefrences[user1]:
		if item in prefrences[user2]:
			si[item] = 1

	#if they have no rating in common, return 0
	if len(si) == 0: 
		return 0

	#Add up the squares of all differences
	sum_of_squares = sum([pow(prefrences[user1][item]-prefrences[user2][item],2) for item in prefrences[user1] if item in prefrences[user2]])

	return 1 / (1 + sum_of_squares)


#Returns the Pearson correlation coefficient for p1 and p2 
def sim_pearson(prefrences,p1,p2):
	#Get the list of mutually rated items
	si = {}
	for item in prefrences[p1]:
		if item in prefrences[p2]: 
			si[item] = 1

	#if they are no rating in common, return 0
	if len(si) == 0:
		return 0

	#sum calculations
	n = len(si)

	#sum of all preferences
	sum1 = sum([prefrences[p1][it] for it in si])
	sum2 = sum([prefrences[p2][it] for it in si])

	#Sum of the squares
	sum1Sq = sum([pow(prefrences[p1][it],2) for it in si])
	sum2Sq = sum([pow(prefrences[p2][it],2) for it in si])

	#Sum of the products
	pSum = sum([prefrences[p1][it] * prefrences[p2][it] for it in si])

	#Calculate r (Pearson score)
	num = pSum - (sum1 * sum2/n)
	den = sqrt((sum1Sq - pow(sum1,2)/n) * (sum2Sq - pow(sum2,2)/n))
	if den == 0:
		return 0

	r = num/den

	return r

#Returns the best matches for person from the prefrences dataset results and similiraty function being optional.
def topMatches(prefrences,person,n=5,similarity=sim_pearson):
	scores = [(similarity(prefrences,person,other),other)
				for other in prefrences if other != person]
	scores.sort()
	scores.reverse()
	return scores[0:n]


#Gets recommendations for a person by using a weighted average

def getRecommendations(prefrences,person,similarity=sim_pearson):
	totals = {}
	simSums = {}

	for other in prefrences:
		#don't compare me to myself
		if other == person:
			continue
		sim = similarity(prefrences,person,other)

		#ignore scores of zero or lower
		if sim <= 0: 
			continue
		for item in prefrences[other]:
			#only score items i haven't seen yet
			if item not in prefrences[person] or prefrences[person][item] == 0:
				#Similarity * score
				totals.setdefault(item,0)
				totals[item] += prefrences[other][item] * sim
				#Sum of similarities
				simSums.setdefault(item,0)
				simSums[item] += sim

	#Create the normalized list
	rankings = [(total/simSums[item],item) for item,total in totals.items()]

	#Return the sorted list
	rankings.sort()
	rankings.reverse()
	return rankings


#Function to transform Person, item - > Item, person
def transformprefrences(prefrences):
	results = {}
	for person in prefrences:
		for item in prefrences[person]:
			results.setdefault(item,{})

			#Flip item and person
			results[item][person] = prefrences[person][item]
	return results
