def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a

    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b

def lucas(n):
    a = 2
    b = 1
    c = 0

    if n == 0:
        return a


    for i in range(a, n + 1):
        c = a + b
        a = b
        b = c

    return b


def sum_series(n, a=0, b=1):
    c = 0
    d = 1

    if n == 0:
      return a

    if a == 0:
        r = n
    else:
        r = n + 1
    if a == 2:
        d = 2
    for i in range(d, r):
        c = a + b
        a = b
        b = c
    return b
