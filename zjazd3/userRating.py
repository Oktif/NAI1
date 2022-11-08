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

  def getAverageScore(self):
    return sum(self.ratings.values()) / len(self.ratings)

  def  __str__(self):
    return 'username : {} \n' \
           'ratings : {} '.format(self.name, self.ratings)