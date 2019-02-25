def add(numbers):
  total = []
  for digit in str(numbers):
    total.append(int(digit))
  return sum(total)

print(add(43267))


def adding(numbers):
  total = 0
  for number in str(numbers):
    total += int(number)
  return total

print(adding(1123))

def add_numbers(digits):
  return sum([int(x) for x in str(digits)])

print(add_numbers(42134245))


def add_numbers(digits):
  total = []
  for x in str(digits):
    total.append(int(x))
  return sum(total)

print(add_numbers(3123))

