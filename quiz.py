print("*******  Welcome to ~ CHEMISTRY QUIZ ~  *******")
name = input("\nEnter your name: ",)
print("\n")


ques = [
  ["Q1: What is the chemcial formula of Sulphuric acid ?", "Amount : $350" ],  
  ["Q2: Which acid is present in human stomach?", "Amount : $560"],
  ["Q3: What is the chemical formula for Acetic Acid", "Amount : $1000"] ]

ans = ["H2SO4", "HCL", "CH3COOH"]

i = 0
while i < len(ques):
  print(ques[i]) 
  answer = input("\nEnter the answer : ")
  print("\n")
  
  if (answer == ans[i]):
      i = i+1
  else:
    print("Better Luck next time")
    break

else:
   print(f"You won {name}, you are a Champion !!!!")
