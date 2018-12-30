def adding(number):
    total = []
    for x in str(number):
        total.append(int(x))
    return sum(total)

print(adding(43256))
