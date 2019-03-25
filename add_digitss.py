def add_digits(numbers):
    return (sum([int(x) for x in list(str(numbers))]))

print(add_digits(432565))

def add_digits(digits):
    total = []
    for x in str(digits):
        total.append(int(x))
    

add_digits(424455676578)
