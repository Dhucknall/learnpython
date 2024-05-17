#Python program that will take in a number from the user and print if it is positive, negative, or zero.
number = int(input("Please enter a number :"))
if number < 0:
	print("The number is negative")
elif number > 0:
	print("The number is positive")
else:
	print("The number is 0")

