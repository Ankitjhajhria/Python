#this is python program to find  prime numbers

#we will now give a variable for the first prime number
counter = 2
#we will now make a loop for getting the all numbers
while counter < 1000:
    i = 1
    #again a loop for the loop for taking out prime numbers from all numbers
    while i < counter:
        i = i + 1
        if counter %i==0:
            break
        #giving conditions for printing them.
    if i == counter:
        print counter
    counter = counter + 1
