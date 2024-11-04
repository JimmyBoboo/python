
def fac(n):
    if n == 1:
        return 1
    
    return n * fac(n-1)



def fib(n):
    if n <=1:
        return n
    return fib(n-1) + fib(n-2)

print(fac(1))
print(fac(4))
print(fac(50))

print(fib(2))
print(fib(5))
print(fib(20))

