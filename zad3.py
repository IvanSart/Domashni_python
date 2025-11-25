def fib(n):
    if n <= 1:
        return n
    x = 0
    y = 1
    for i in range(n):
        x, y = y, x + y
    return x

def fib_rec(n):
    if n <= 1:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)

print(fib(5))
print(fib_rec(8))