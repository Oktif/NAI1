from ratingParse import parse
userRatings = parse()
'''
Loop used for inputting desired user
'''
def user_name():
    u = None
    while u == None:
        user_inputted = input('Please type-in full name of the User: ')
        for i in range(len(userRatings)):
            user_1 = userRatings[i]
            if user_inputted == user_1.name:
                u = i
                break
            elif user_inputted.upper() == 'AMNESIA':
                print(user_1.name)
                continue
        else:
            print('incorrect data, please enter correct one, if you are unsure whats your name enter AMNESIA')
            continue
        return u
