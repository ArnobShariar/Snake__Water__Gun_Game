import random

def check(comp, user):
    if comp == user:
        return 0
    if(comp == 0 and user == 1):
        return -1
    if (comp == 2 and user == 0):
        return -1
    if (comp == 1 and user == 2):
        return -1


    else:
        return 1

comp = random.randint(0,2)
user = int(input('''Enter any number between 0,1 or 2 to play.
                        0 for Snake
                        1 for Water
                        2 for Gun.         : '''))

score = check(comp, user)
print("You: ", user)
print(("computer: ", comp))

if(score == 0):
    print("It's a draw")
elif(score == -1):
    print("Computer Won")
else:
    print("Hurray!! You Won")
