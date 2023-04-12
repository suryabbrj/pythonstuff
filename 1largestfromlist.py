lst = []
n = int(input("enter the number of elements : "))
print("enter the elements in the list : ")
for i in range(0, n):
    elem = int(input())
    lst.append(elem)
    
print(lst)
print("\nlargest element in this list is :", max(lst))
    