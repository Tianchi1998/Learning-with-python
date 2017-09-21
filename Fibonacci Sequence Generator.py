fibonacci_sequence = []

def fib(m,n):
    if (m+n) > 100:
        return
    fibonacci_sequence.append(m+n)
    fib(n,m+n)

fib(0,1)
print(fibonacci_sequence)
