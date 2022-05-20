x = int(input("enter a value for x: "))
y = int(input("enter a value for y: "))


def factorial(x, y):

    res = x

    for i in range(1, y):
        if i <= y:
            res *= x
        else:
            break

    return res


print(factorial(x, y))
