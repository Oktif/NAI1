'''
Programming Team: Maciej Zakrzewski, Oktawian Filipkowski.
Purpose of this program is to recommend movies to watch or to warn users against watching bad ones.
We will start by importing libraries
'''
from ratingParse import parse
from userRating import userRating
from userSelection import user_name
from movieCalculation import cosine_dic
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
We start with shared similarity method
'''
comparingList = user.ratings
s = 0
for t in range(len(userRatings)):
    if t != u:
        user_temp = userRatings[t]
        comparedList = user_temp.ratings
        x = comparingList
        y = comparedList
        shared_items = {k: x[k] for k in x if k in y and x[k] == y[k]}
        if (len(shared_items)) >= s:
            s = t
            user2 = userRatings[s]
'''Alternative version for bonus exercise is cosine similarity'''
z = 0
for j in range(len(userRatings)):
    if j != u:
        user_temp = userRatings[j]
        comparedList2 = user_temp.ratings
        x = comparingList
        y = comparedList2
        cosine_similarity = cosine_dic(x, y)
        if cosine_similarity > z:
            z = cosine_similarity
            zz = j
            user3 = userRatings[zz]



'''
After calculations user's soulmate will be found and movies will be reccomended for our dear user
ps. In case of Mr.Czapiewski "Listy do M" are used as an option because there is typo in the name of the movie
Lets start with shared similarity 
'''
print('Congrats', user.name, 'according shared similarity method your soulmate is', user2.name)
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

'''
Now we do the same for cosine similarity method
'''
print('''
*****************************************************************************************************************
''')
print('Congrats', user.name, 'according cosine similarity method your soulmate is', user3.name)
print('Your average score is',user.getAverageScore(), 'your\'s soulmate\'s is', user3.getAverageScore(), 'quite a picky bunch, aren\'t ya?')
List11 = user.ratings
List21 = user3.ratings
print('You both watched', set(List11).intersection(List21))
List31 = user.getTopRated(15)
List41 = user.getMinRated(15)
List51 = user3.getTopRated(15)
List61 = user3.getMinRated(15)
List71 = list()
List81 = list()

def in_list(list1,list2,list3):
    keys1 = []
    keys2 = []
    for i in (list1):
        keys1.append(list(i.keys()))
    for g in (list2):
        keys2.append(list(g.keys()))
    for h in keys1:
        if h not in keys2:
            list3.append(h)
    return list3




def in_list2(list1,list2):
    for i in list1:
        if i not in list2:
            List81.append(i)
    return True


in_list(List51,List31,List71)
in_list(List61,List41,List81)
print('You should watch:', List71[:5])
print('You shouldn\'t watch:', List81[:5])






