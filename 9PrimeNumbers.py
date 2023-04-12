lst = []
n = int(input("enter the range : "))
print("enter the elements : ")
for i in range(0 , n):
    elem = int(input())
    lst.append(elem)

print("the prime numbers in ", lst, " are : ")
for i in lst:
    for j in range(2,(i//2)+1):
        if i%j == 0:
            break
    else:
        print(i)