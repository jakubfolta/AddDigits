def addDigits(number):
    total = 0
    for x in str(number):
        total += int(x)
    return total

print(addDigits(323345))

def addingDigits(number):
    return sum(int(x) for x in str(number))

print(addingDigits(3214))

def addingDigits(number):
    total = []
    for x in str(number):
        total.append(int(x))
    return sum(total)

print(addingDigits(2132424))

def addingDigits(number):
    total = 0
    number = str(number)
    lengthOfNumber = len(number)
    while lengthOfNumber > 0:
        total += int(number[lengthOfNumber - 1])
        lengthOfNumber -= 1
    return total

print(addingDigits(112111))
        
