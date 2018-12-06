#this program is for taking out the mean from list

#this for taking input
num = list(input("Enter numbers>"))

#for checking maxi and minii
maxi = max(num)
minii = min(num)

num.remove(maxi)
num.remove(minii)
total=sum(num)
#taking the mean and printing
num = len(num)
print total/num
