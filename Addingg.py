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
