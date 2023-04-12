n = int(input("enter the range : "))
counter = 0
i = 2
while counter<n:
    sum = 0
    for j in range (1, i-1):
        if i%j ==0:
            sum = sum + j
        j = j + 1
    if sum == i:
        print(i)
        counter = counter + 1
    i = i + 1