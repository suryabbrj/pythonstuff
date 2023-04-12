lst = []
n = int(input("enter the range : "))
if(n<1):
    print("list size is too low, please retry with a larger value!!")
else:
    
    print("enter the elements : ")
    for i in range(0, n):
        elem = int(input())
        lst.append(elem)

    lst.sort()
    print("the sorted array is : ", lst)
    item = int(input("enter the item you want to search in the list : "))
    low = 0
    high = len(lst)-1

    while low<= high:
        mid = (low + high) // 2
        if lst[mid] == item:
            print("item found!!!")
            break
        elif lst[mid] > item:
            high = mid - 1
            
        else:
            low = mid + 1
            
    else:
        print("item doesn't exist in the list : ", lst) 
        