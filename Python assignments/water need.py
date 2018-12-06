#this program is for calculating the water need for all the animals

#firsat we  will read the csv file.
zoo = open("zoo.csv",'rt')
read_file= zoo.readlines()
#now we will create variables for each animals
water = 0
water2 = 0
water3 = 0
water4 = 0
water5 = 0
#we will create loop to read each line and adding
for i in read_file:
    split = i.split(',')
    #using conditions we will calculate the total suply
    if split[0] == 'elephant':
        water = water + int(split[2])

    elif split[0] == 'tiger':
        water2 = water2 + int(split[2])

    elif split[0] == 'lion':
        water3 = water3 + int(split[2])

    elif split[0] == 'zebra':
        water4 = water4 + int(split[2])

    elif split[0] == 'kangaroo':
        water5 = water5 + int(split[2])
#now we will print for every animal and for total water need
print water
print water2
print water3
print water4
print water5
new = water + water2  + water3 +  water4 + water5
print new
zoo.close()

