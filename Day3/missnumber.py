def missnumber(listA, listB):
	listAB = listA + listB # combines listA and listB

	for i in range(0, len(listAB)):

		if ((listAB[i] not in listA) or (listAB[i] not in listB)): #check if an element in the combined listAB is not in either listA or ListB
			c = listAB[i] # returns the missing number
	print c # prints missing number

missnumber([1,2,3,4,5], [1,2,3,4,5,7])