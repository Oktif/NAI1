from ratingParse import parse
from userRating import userRating

userRatings = parse()

exampleUser = userRatings[0]
print(exampleUser.name)
print(exampleUser.haveRated('Braveheart'))
print(exampleUser.getRating('Braveheart'))
print(exampleUser.haveRated('Leon Zawodowiec'))
print(exampleUser.getRating('Leon Zawodowiec'))
print(exampleUser.getAverageScore())
print(exampleUser.getTopRated(10))