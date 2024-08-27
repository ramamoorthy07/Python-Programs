def recur_fibo(n):
    if n<=1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))
num=int(input("Enter the number:"))
if num<=0:
    print("please Enter the possitive number")
else:
    print("Fibonacci Sequence:")
    for i in range(num):
        print(recur_fibo(i))
