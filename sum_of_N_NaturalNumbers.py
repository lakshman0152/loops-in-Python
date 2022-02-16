print ("SUM OF N NATURAL NUMBERS \n")

user_number = input("How many numbers you want to add : ")

sum = 0
start = 1

while(start <= int(user_number)):
    sum = sum + start
    start +=1
    print("Your sum of "+ user_number +" numbers is : "+str(sum))

else:
    print("Enter a positive number")


