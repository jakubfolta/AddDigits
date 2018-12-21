def addDigits(number):
    total = 0
    for x in str(number):
        total += int(x)
    return total

print(addDigits(33456))

def addingDigits(number):
    return sum(int(x) for x in str(number))

print(addingDigits(344563))

def addingDigits(number):
    return sum([int(x) for x in str(number)])
    
print(addingDigits(232))
