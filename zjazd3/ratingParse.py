from userRating import userRating

def parse():
    file = open('dane.csv', 'r')
    lines = file.read().split('\n')
    userRatings = []
    for line in lines:
        line = line.rstrip(';')
        lineElements = [elem.strip() for elem in line.split(';')]
        user = lineElements[0]
        data = lineElements[1:]
        ratings = {}
        for i in range(0, len(data) - 1, 2):
            ratings.update({data[i]: float(data[i + 1])})
        userRatings.append(userRating(user, ratings))
    return userRatings