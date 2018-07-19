roll = input ("Would you like to roll the dice? ")

while roll == "yes":
	from random import randint
	print (randint (2,12))
	roll = input ("Would you like to roll the dice? ")
	