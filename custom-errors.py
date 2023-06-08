err = input("type quit to exit or enter the number between 5 to 9 : ")


if (str(err) == "quit"):
   print("End of the program")
  
elif(int(err)<5 or int(err)>9):
 
  raise ValueError('''The value should be between 5 and 9 ''')
  
