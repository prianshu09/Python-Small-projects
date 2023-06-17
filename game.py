# This is snake water and gun game & uses the same logic as of rock paper scissors game

print("******* Welcome to ~ Snake Water Gun ~ ********")

import random

ran = random.randint(1, 3)

if (ran == 1):
   pc = "s"  
elif(ran == 2):
   pc = "w"
elif(ran == 3):
   pc = "g"


def game (pc, you):
  if (pc == you):
     return None

  elif pc == "s":
     if you == "g":
       return True
     if you == "w":
       return False
 
  elif pc == "w":
     if you == "s":
       return True
     if you == "g":
       return False

  elif pc == "g":
     if you == "w":
       return True
     if you == "s":
       return False


print("Computer's turn : ")

print("Choose [s] for snake, [w] for water, [g] for gun")
you = input("Choice : ")

gameplay = game(pc, you)  

if gameplay == None:
  print("This game is a Tie")

elif gameplay == True:
  print("Yay! You Win")

else:
  print("You loose, better luck next time")



print("\n\n ***** Game Stats ***** ")
print("Pc chose : ", pc)
print("You chose: ", you)
