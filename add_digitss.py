def add_digits(numbers):
    return (sum([int(x) for x in list(str(numbers))]))

print(add_digits(432565))
