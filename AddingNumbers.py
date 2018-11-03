def adding(numbers):
  return sum(int(dig) for dig in str(numbers))

print(adding(11234))


def add(numbers):
  total = 0
  for dig in str(numbers):
    total += int(dig)
  return total

print(add(12765))


def add(numbers):
  total = []
  for dig in str(numbers):
    total.append(int(dig))
  return sum(total)

print(add(32456))
