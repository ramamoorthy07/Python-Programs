#get input from the user
num=int(input("Enter the value:"))
factorial=1
if(num<0):
    print("please enter the positive number")
elif(num==0):
    print("0 is factorial of 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("The Factorial of num is:",factorial)              
