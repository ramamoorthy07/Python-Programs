def cube_sum(Num):
    total=sum(i**3 for i in range(1,Num+1))
    return total
Num=int(input("Enter the Number:"))
if Num<=0:
    print("Please Enter the Positive Number")
else:
    result=cube_sum(Num)
    print(result)
