secret_number = 484

print("Hi! This is a game called ^secret number^.\n\nI have picked a secret number between 1 and 1000.\n\nIf you want to escape from the loop you have to find it! Good luck.\n")
num=int(input("I think the secret number is...:\n\n"))
print("Let's see if you got it right!!\nThe number has been placed...\n")
if num==secret_number:
    print("You've found it!!! I can not believe you did it at the first try!! Here is a kiss:\n\nMUUUUUUUUUUUUUUAHHHHH")
else:
    while num!=484:
        print("Oh...\n\nI think you are not lucky at this point.\n\nYou have to try again. Or else you'll be stuck in my loop forever!!!\n\nDon't disappoint me. I believe in you!!")
        num=int(input("Try again!!:\n"))
        if num==secret_number:
            print("You've found it!\n\nYou could've got a kiss if you could have found it at the fisrt try....\n\nDo not worry here is a smile for you....\n\n:) :) :)\n\nstart the game again to get the kiss.\nDo not worry the secret number will be the same")
            break
        else:
            continue

#Here is a little game to make a smile on your face. I hope you enjoy it.
#BuseOzkose 07/27/2022
