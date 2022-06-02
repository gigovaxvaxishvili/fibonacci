def fibonacci(iteration):
    a = 0
    b = 1
    c = 0

    fibolist = []

    if iteration <= 0:
        print("more than 0")

    elif iteration == 1:
        print(a)

    else:
        while c < iteration:
            fibolist.append(a)
            fib = a + b
            a = b
            b = fib
            c += 1
        return (fibolist)


