 #get input from the user
num=int(input("Enter the value:"))
string=str(num)
num_digits=len(string)
count=0
temp=num
while temp>0:
    digit=temp%10
    count+=digit**num_digits
    temp//=10
if count==num:
    print(f"{num},is a Amstrang number")
else:
    print(f"{num},is not a Amstrang number")
    

