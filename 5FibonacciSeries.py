def fibo(n):
    if n<=1:
        return n
    else:
        return(fibo(n-1) + fibo(n-2))

nterms = int(input("enter the limit for the series : "))
print("fibonacci series with ", nterms, "range is : ")
for i in range(nterms):
    print(fibo(i))