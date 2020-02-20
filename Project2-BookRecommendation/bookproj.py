

# Read the book data into a list of (author,title) tuples. Do this at the module/file level.
books = [] 
fileReader = open('booklist.txt', 'r')
for line in fileReader:
    books.append(tuple(line.strip().split(',')))
fileReader.close()


# Read the ratings data into a dictionary keyed by each name (converted to lower case). 
# The value for each key is a list of the ratings for that reader, preserving the original order. 
# Do this also at the module level so the data is available when the functions mentioned below are called. 
ratings = {}
fileReader = open('ratings.txt', 'r')

while True:
    name = fileReader.readline().strip().lower()
    if not name:
        break
    scores = fileReader.readline().split()
    intScores = []

    for score in scores:
        intScores.append(int(score))

    ratings[name] = intScores

fileReader.close()

# Write a function dotprod(x,y) 
def dotprod(x, y):
    total = 0

    for i in range(len(x)):
        total += x[i] * y[i]
    
    return total


# Compute affinity scores for each user.  Store it in a data structure at the module level. 
affinityScores = {}

def computeAffinityScores():
    for name1 in ratings:
        for name2 in ratings:
            if name1 != name2:
                score = dotprod(ratings[name1], ratings[name2])
                if score > 0:
                    affinityScores[name1] = affinityScores.get(name1, {})
                    affinityScores[name1][name2] = score

computeAffinityScores()

#YOU NEED TO PULL THE TOP TWO PEOPLE OUT OF THE AFFINITY SCORE DICTIONARY! THEN YOU CAN DO ALL OF THE BELOW.
# Write the friends function, which returns a sorted list of the names of the two readers with the highest 
# affinity scores compared to the reader in question. Use the sorted function for all sorting in this program. 
def friends(name):
    friendsList = sorted(affinityScores[name], key=affinityScores[name].get, reverse=True)
    friendsList = friendsList[0:2]
    return friendsList


# # Returns the indexes of all occurrences of give element in
# # the list- listOfElements. I will use this function to look up the indexes of all books given a positive rating. 
def getIndexPositions(listOfElements, element):
    indexPosList = []
    for i in range(len(listOfElements)): 
        if listOfElements[i] == element:
            indexPosList.append(i)
    return indexPosList   


# Write recommend by calling friends and then getting the recommended books from the two friends obtained. 
def recomend(name):
    twoFriends = friends(name)
    recommendations = []

    #Remove books read by current person from friends lists.
    firstFriend = ratings[twoFriends[0]].copy()
    secondFriend = ratings[twoFriends[1]].copy()
    for num, rate in enumerate(ratings[name]):
        if rate != 0:
            firstFriend[num] = 0
            secondFriend[num] = 0

    
    #Find the index values of all of the three's and five's. 
    recommendations.append(getIndexPositions(firstFriend, 3))   
    recommendations.append(getIndexPositions(secondFriend, 3))  
    recommendations.append(getIndexPositions(firstFriend, 5)) 
    recommendations.append(getIndexPositions(secondFriend, 5))#pull the 3 and 5's for each friend out of ratings. 

    #compress recommendations into one list with no duplicates.
    flat_list = [] 
    for sublist in recommendations:
        for item in sublist:
            flat_list.append(item)
    recommendations = list(dict.fromkeys(flat_list))


    bookRecommendations = []
    for indexValue in recommendations: #This is all the books that received a 3 and 5 ratings
        bookRecommendations.append(books[indexValue])
        bookRecommendations = sorted(bookRecommendations, key=lambda tup: (tup[0].split()[-1], tup[0].split()[0], tup[1]))

    finalString = ""
    for item in bookRecommendations:
        finalString += str("\n") + str("\t") + str(item)

    return finalString

def report():

    sortedKeys = sorted(ratings, key=str.lower)
    megaString = ""
    for people in sortedKeys:
        twoFriends = friends(people)
        megaString += people
        megaString += str(": ")
        megaString += str(twoFriends)
        megaString += recomend(people)
        megaString += "\n" + "\n"
    return megaString
        # print(people, str(": "), twoFriends ,recomend(people))


#All of the above should execute when the module is loaded or imported, 
# so you need to make sure you have computed the friends and affinity scores at the module level, independent of main. 
# Your main function only prints the full report, as previously shown.
def main():
    """Prints recomendations for all readers """
    with open('recomendations.txt', 'w') as rec_file:
        print(report(), file=rec_file)

if __name__ == '__main__':
    main() 


