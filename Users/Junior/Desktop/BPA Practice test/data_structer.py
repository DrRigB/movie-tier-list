
#Makes the list
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#For in loop, Example from w3schools: fruits = ["apple", "banana", "cherry"] 
#for x in fruits:
#  print(x)

for x in list:
    if x % 2 != 0: #checks if number is odd or even by seeing if there is a remainder
        continue 
    print(x) # prints remaning numbers

