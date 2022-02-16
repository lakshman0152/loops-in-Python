from tracemalloc import start


print("welcome !\n")
print("SUM OF RANGE OF NUMBERS \n")

start = int(input("Enter start number : "))
end = int(input("Enter end number : "))
print("")

sum = 0 
for num in range(start , end+1):
    sum += num
print("Your sum of numbers from "+str(start)+ " to "+str(end)+ " is "+ str(sum))

print("")
print("Thank you for using this application!")
