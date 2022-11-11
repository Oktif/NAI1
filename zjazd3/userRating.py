'''
This class contains some functions used for our program:
haveRated and getRating will check if particular movie was rated and if it was, functions will return its values
getTopRated will return the highest rated movies
getMinRated will return the lowest rated movies
getAverageScore will return average score of movies rated by user
'''
class userRating:
  def __init__(self, name, ratings):
    self.name = name
    self.ratings = ratings

  def haveRated(self, movie):
    return movie in self.ratings.keys()

  def getRating(self, movie):
    return self.ratings.get(movie)

  def getTopRated(self, count = 3):
    tempDict = self.ratings.copy()
    topRatings = []
    for i in range(count):
      v = list(tempDict.values())
      k = list(tempDict.keys())
      key = v.index(max(v))
      topRatings.append({k[key] : tempDict.pop(k[key])})
    return topRatings

  def getMinRated(self, count = 3):
    tempDict = self.ratings.copy()
    minRatings = []
    for i in range(count):
      v = list(tempDict.values())
      k = list(tempDict.keys())
      key = v.index(min(v))
      minRatings.append({k[key] : tempDict.pop(k[key])})
    return minRatings

  def getAverageScore(self):
    return sum(self.ratings.values()) / len(self.ratings)

  def  __str__(self):
    return 'username : {} \n' \
           'ratings : {} '.format(self.name, self.ratings)