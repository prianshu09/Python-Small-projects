import random
import string

print("*******  Welcome to encryption/Decryption module  *******\n\n")

r = random.choice(string.ascii_letters)
a = random.choice(string.ascii_letters)
n = random.choice(string.ascii_letters)
d = random.choice(string.ascii_letters)
o = random.choice(string.ascii_letters)
m = random.choice(string.ascii_letters)

text = input("Enter your text: ")
words = text.split(" ")

print("\nEnter [1] to encode")
print("Enter [0] to decode\n")
# print("Enter [3] to Try again or Exit")

inp = input("Enter your choice: ")

inp = True if (inp == "1") else False

if (inp):
  nwords = []
  for word in words:
    if (len(word) >= 3):
      ran = r + a + n
      dom = d + o + m
      newstr = ran + word[1:] + word[0] + dom
      nwords.append(newstr)
    else:
      nwords.append(word[::-1])
  print("\n", " ".join(nwords))

else:

  nwords = []
  for word in words:
    if (len(word) >= 3):
      newstr = word[3:-3]
      newstr = newstr[-1] + newstr[:-1]
      nwords.append(newstr)
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))
