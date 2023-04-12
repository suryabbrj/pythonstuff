def gcd(x, y):
    while(y):
        x, y = y, x%y
    print(x)
    return x

def find_lcm(x, y):
    lcm = (x*y)//gcd(x, y)
    return lcm

num1 = int(input("enter the first number : "))
num2 = int(input("enter the second number : "))
print("the GCD of ", num1 , "and ", num2, "=")
print("the LCM is ",find_lcm(num1, num2))
