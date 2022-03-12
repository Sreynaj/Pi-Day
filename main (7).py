#greeting our users!
#print("""Let's start practicing using Pi for today.
      #A = π r²""")
#from math import pi

#print("A=", pi* r**2)
#print('')
#str=input('Happy Pi Day!')
#print('')

#game section
print("Let's play game!")
name=input("What's your name:")
print("Hi!",name,", let's get ready for the game.")
print('')
str=input("Ready!")

MAX_ATTEMPS_ALLOWED = 5
attemp_number = 0
right_answer = False
while attemp_number<MAX_ATTEMPS_ALLOWED and right_answer==False:
  attemp_number = attemp_number + 1
  print("Attemp number: ", attemp_number)
  # the fisrt level of the game typing pi digits
  x = float(input("The first three digits of pi are:"))
  if x == 3.14:
    right_answer = True
    print("Congrats! you have passed the level 1!")
  else:
    
    print("Oops! I don't think your answer is correct, Let's try again")

# the second level of the game 
x = float(input("The next two digits of pi are: 3.14"))
if x == 15:
  print("Congrats! Let's go to another level!")
else:
  print("Oops! I don't think your answer is correct,let's try again")
  x = float(input("The next two digits of pi are: 3.14"))
print('')

#The third level of the game 
x = float(input("The next four digits of pi are: 3.1415"))
if x == 9265:
  print("Congrats! you have passed the level 3!")
else:
  print("Oops! I don't think your answer is correct, let's try again")
  x = float(input("The next four digits of pi are: 3.1415"))
#The fourth level of the game 
x = float(input("The next five digits of pi are: 3.14159265"))
if x == 35897 :
  print("Congrats! you have passed the level 4!")
else:
  print("Oops! I don't think your answer is correct, let's try again")
  x = float(input("The next five digits of pi are: 3.14153.14159265"))
#The fith level of the game 
x = float(input("The next seven digits of pi are: 3.1415926535897"))
if x == 9323846 :
  print("Congrats! you have passed the level 4!")
else:
  print("Oops! I don't think your answer is correct, let's try again")
  x = float(input("The next five digits of pi are: 3.1415926535897"))