n=int(input("Enter the number of terms of the Fibonacci series to be printed: "))

def fib(n):
    x, y = 0, 1
    if n <= 0:
        print("Enter a proper term!")
    elif n == 1:
        print("Fibonacci Series up to", n, "terms:")
        print(x)
    else:
        print("Fibonacci Series up to", n, "terms:")
        for i in range(n):
            print(x, end=", ")
            x,y = y,x+y

fib(n)