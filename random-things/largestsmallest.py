number = input("Enter a number/done: ")
smallest = number
largest = number 
while (number != "done"):
    number = input("Enter a number/done: ")
    if (number.isnumeric()):
        if (number > largest):
            largest = number
        elif (number < smallest):
            smallest = number        
print(largest)
print(smallest)    
   