import random

#name="Shweta"
print("enter your name:")
name = input()
#print("Dear "+name);
message = "Dear {0}"
print(message.format(name))

minNum=4
maxNum=10
aRandomNum = random.randint(minNum,maxNum)
message = "Guess a number between {0} and {1}"
print(message.format(minNum,maxNum))


rightGuess = False
tryCount = 0
while tryCount < 3 and not rightGuess:
    guessedNum = int(input())
    tryCount += 1
    if guessedNum == aRandomNum:
        rightGuess = True
        #break
    elif guessedNum < aRandomNum:
        print("too less!")
    elif guessedNum > aRandomNum:
        print("too high!")

if rightGuess:
    print("you guessed right in " + str(tryCount) + "trie(s)")
else:
    print("sorry, you couldn't guess the number "+ str(aRandomNum) + " within " + str(tryCount) + " tries.")

