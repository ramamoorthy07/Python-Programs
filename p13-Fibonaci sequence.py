#get input from the user
num=int(input("Enter the value:"))
n1,n2=0,1
count=0
if(num<0):
    print("please enter the positive number")
elif(num==0):
    print("0")
else:
    while count<num:
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3
        count+=1
