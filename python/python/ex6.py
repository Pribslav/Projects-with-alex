#this defines types_of_people as 10
types_of_people = 10
#this inserts 10 into the string
x = f"There are {types_of_people} types of people."

#this defines binary and dont
binary = "binary"
do_not = "don't"

#this string sets up y to format binary and dont
y = f"Those who know {binary} and those who {do_not}."

#this prints the strings we have made
print(x)
print(y)

#this prints x and y nestled inside other strings
print(f"I said: {x}")
print(f"I also said: '{y}'")

#this defines hilarious as false and defines joke_evaluation. 
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

#this prints out joke evaluation and adds the false to it.
print(joke_evaluation.format(hilarious))

#defines two strings as letters
w = "This is the left side of..."
e = "a string with a right side."

#prints the two strings 
print(w + e) 
