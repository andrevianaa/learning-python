print("Welcome to the Quiz Game.")
player = input("Enter a nickname: ")
print("Welcome",player)

playing = input("Star the game? ")
if playing.lower() == "n":
    print("See you another time then, bye.")
    quit()
if playing.lower() == "y":
    print("Let's begin!")

score = 0

answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 100
else:
    print("Wrong answer.")

answer = input("What does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 100
else:
    print("Wrong answer.")

answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 100
else:
    print("Wrong answer.")

answer = input("What does SSD stands for? ")
if answer.lower() == "solid state drive":
    print("Correct!")
    score += 100
else:
    print("Wrong answer.")

answer = input("What does PSU stands for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 100
else:
    print("Wrong answer.")

answer = input("What does PC stands for? ")
if answer.lower() == "personal computer":
    print("Correct!")
    score += 100
else:
    print("Wrong answer.")

print("Your score is:",score)
if score >= 399:
    print("Congrats",player,"you won the game!")
else:
    print("Sorry",player,"you lost the game, try one more time.")