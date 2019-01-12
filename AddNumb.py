def adding(numbers):
  return sum(int(digit) for digit in str(numbers))

print(adding(163783))


def adding(numbers):
  total = 0
  for number in str(numbers):
    total += int(number)
  return total

print(adding(9876))

def addNumbers(numbers):
  total = 0
  for x in str(numbers):
    total += int(x)
  return total

print(addNumbers(423566))

def addNumbersFromList(numbers):
  total = 0
  for x in numbers:
    total += x
  return total

print(addNumbersFromList([3, 4, 6, 4, 2, 2, 3]))
