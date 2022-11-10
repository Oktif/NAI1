'''
Programming Team: Maciej Zakrzewski, Oktawian Filipkowski.
Purpose of this program is to recommend movies to watch or to warn users against watching bad ones.
We will start by importing libraries
'''
from ratingParse import parse
from userRating import userRating
from userSelection import user_name
'''
Then we will import parsed data
'''
userRatings = parse()
'''
Next we will ask user to provide us his full Name and Surname, to assign this program with his ID
'''
u = user_name()
user = userRatings[u]
'''
Now program will make advanced calculations using data provided with .csv file
'''
comparingList = user.ratings
s = 0
for i in range(len(userRatings)):
    if i != u:
        user_temp = userRatings[i]
        comparedList = user_temp.ratings
        x = comparingList
        y = comparedList
        shared_items = {k: x[k] for k in x if k in y and x[k] == y[k]}
        if (len(shared_items)) >= s:
            s = i
            user2 = userRatings[s]

'''
After calculations user's soulmate will be found and movies will be reccomended for our dear user
ps. In case of Mr.Czapiewski "Listy do M" are used as an option because there is typo in the name of the movie
'''
print('Congrats', user.name, 'your soulmate is', user2.name)
print('Your average score is',user.getAverageScore(), 'your\'s soulmate\'s is', user2.getAverageScore(), 'quite a picky bunch, aren\'t ya?')
List1 = user.ratings
List2 = user2.ratings
print('You both watched', set(List1).intersection(List2))
List3 = list(user.getTopRated(10))
List4 = list(user.getMinRated(10))
List5 = list(user2.getTopRated(10))
List6 = list(user2.getMinRated(10))
List7 = list()
List8 = list()

def in_list(list1,list2):
    for i in list1:
        if i not in list2:
            List7.append(i)
    return True

def in_list2(list1,list2):
    for i in list1:
        if i not in list2:
            List8.append(i)
    return True
in_list(List5,List3)
in_list2(List6,List4)

print('You should watch:', List7[:5])
print('You shouldn\'t watch:', List8[:4:-1])