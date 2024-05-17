#Quiz
print("Quiz time!")
score = 0
books = int(input("How many books are there in the Harry Potter series? "))
if books == 7:
    print("Correct! ")
    score +=1
else:
    print("incorrect")

print()

sum1 = int(input("What is 3*(2-1)? 3 "))
if sum1 == 3:
    print("You are correct")
    score +=1
else:
    print("Incorrect")

sum2 = int(input("What is 3*2-1? "))
if sum2 == 5:
    print("Correct!")
    score+=1
else:
    print("Incorrect")

print("1. Kelly Clarkson")
print("2. K.T. Tunstall")
print("3. Hillary Duff")
print("4. Bon Jovi")

singer = int(input("Who sings Black Horse and the Cherry Tree? "))

if singer == 2:
    print("Correct")
    score +=1
else:
    print("Wrong!")

print ("1. George Washington")
print ("2. Abraham Lincoln")
print ("3. John Adams")
print ("4. Thomas Jefferson")

bill= int(input("Who is on the front of a one dollar bill "))

if bill == 1:
    print("Correct your a true patriot")
    score+=1
else:
    print("Oh no you dont know your history!")
    
print ("You scored ",score ,"out of 5")
percent = score * 100 / 5
print("You got ",percent," percent correct")


    

