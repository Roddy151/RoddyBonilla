def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
factorial_5=factorial(5)
print("Factorial de 5: ", factorial_5)

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else: 
        return fibonacci(n-2) + fibonacci(n-1)


print(fibonacci(9))