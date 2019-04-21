def add(numbers):
    total = 0
    for x in str(numbers):
        total += int(x)
    return total

print(add(34232))

def add(numbers):
    return sum([int(x) for x in str(numbers)])

print(add(32446))

def add_digits(numbers):
    numbers_list = []
    for x in str(numbers):
        numbers_list.append(int(x))
    return sum(numbers_list)

print(add_digits(12314))
