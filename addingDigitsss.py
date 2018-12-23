def adding(number):
    total = []
    for x in str(number):
        total.append(int(x))
    return sum(total)

print(adding(43256))

def add(number):
    total = 0
    for x in str(number):
        total += int(x)
    return total

print(add(432423))


