# Function for nth Fibonacci number





def fibonacci(n):
    # n = A decimal integer

    a = 0
    b = 1
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")
    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return a
    # Check if n is 1
    # then it will return 1
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        # Return fibonacci Number
        return b


# Iterative Python 3 program
# to find n'th Lucas Number

# Iterative function

def lucas(n):
    # n = A decimal integer
    # declaring base values
    # for positions 0 and 1
    a = 2
    b = 1
    c = 0
    # Check if n is 0
    # then it will return 0
    if n == 0:
        return a

    # generating number
    for i in range(a, n + 1):
        c = a + b
        a = b
        b = c
# Return n'th Lucas Number
    return b

#Here is function of the Python Program to find the sum of series:
def sum_series(n, a=0 ):
    #n A decimal integer
    #a = 0 if you want return fibonacci Number or 2 if you want return Lucas Numbers
    b = 1

    d = 1
    # Check if n is 0
    # then it will return 0
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
    # Return fibonacci Number or Lucas Numbers , Depends on what you entered
    return b
