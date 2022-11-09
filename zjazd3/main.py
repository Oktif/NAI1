'''
Programming Team: Maciej Zakrzewski, Oktawian Filipkowski.
Purpose of this program is to recommend movies to watch or to warn users against watching bad ones.
We will start by importing liblaries
'''
from ratingParse import parse
from userRating import userRating

'''
Then we will import parsed data
'''
userRatings = parse()

'''
Next user will provide program with his id
'''
u = int(input('Please provide program with your identification number '))
user = userRatings[u]
print('You entered', u, 'that means your identification is', user.name)
comparingList = user.ratings
s = 0

'''
Now program will make advanced calculations using data provided with .csv file
'''
for i in range(17):
    if i != u:
        user2 = userRatings[i]
        comparedList = user2.ratings
        x = comparingList
        y = comparedList
        shared_items = {k: x[k] for k in x if k in y and x[k] == y[k]}
        if (len(shared_items)) >= s:
            s = i
            user3 = userRatings[s]

'''
After calculations user's soulmate will be found and movies will be reccomended for our dear user
'''
print('Congrats', user.name, 'your soulmate is', user3.name)
print('Your average score is',user.getAverageScore(), 'your\'s soulmate\'s is', user3.getAverageScore(), 'quite a picky bunch, aren\'t ya?')
List1 = user.ratings
List2 = user3.ratings
print('You both watched', set(List1).intersection(List2))
List3 = list(user.getTopRated(10))
List4 = list(user.getMinRated(10))
List5 = list(user3.getTopRated(10))
List6 = list(user3.getMinRated(10))
List7 = list()
#for List5, List3 in zip(List5, List3):
#    List7.append((List5, List3))
List8 = list()
#for List6, List4 in zip(List6, List4):
#    List8.append((List6, List4))

#print(List6)
#print(List4)

def in_list(list1,list2):
    for i in list1:
        if i not in list2:
            List8.append(i)
    return True

def in_list2(list1,list2):
    for i in list1:
        if i not in list2:
            List8.append(i)
    return True

def in_list2(list1,list2):
    for i in list1:
        if i not in list2:
            List7.append(i)
    return True
in_list2(List5,List3)
in_list(List6,List4)

#result = list(set(List6).difference(List4))
#print(result)

print('You should watch:', List7[:5])
print('You shouldn\'t watch:', List8[:5:-1])