def add(numbers):
  total = 0
  for digit in str(numbers):
    total += int(digit)
  return total

print(add(35272839))


def adding(numbers):
  return sum(int(digit) for digit in str(numbers))

print(adding(4232423))
