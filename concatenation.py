def addDigits(number):
    total = 0
    for x in str(number):
        total += int(x)
    return total

print(addDigits(323345))
