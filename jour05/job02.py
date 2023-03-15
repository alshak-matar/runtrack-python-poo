def power(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n % 2 == 0:
        return power(x*x, n/2)
    else:
        return x * power(x*x, (n-1)/2)

x = int(input("Enter an integer x: "))
n = int(input("Enter an integer n: "))
result = power(x, n)
print(x, "raised to the power of", n, "is", result)
