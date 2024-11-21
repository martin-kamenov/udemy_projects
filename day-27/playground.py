# def add(*args):
#     return sum(args)

def add(*args):
    numbers = 0

    for num in args:
        numbers += num

    return numbers


print(add(5, 10, 69, 100, 3))