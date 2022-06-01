def fibonacci(i):
    if i==0:
        return 0
    elif i==1:
        return 1
    else:
        return fibonacci(i-2) + fibonacci(i-1)


def lucas(n):
    a = 2
    b = 1

    if n == 0:
        return a

    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c

    return b
