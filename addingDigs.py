def adding(numbers):
  total = 0
  for digit in str(numbers):
    total += int(digit)
  return total

print(adding(1164759))

def add(numbers):
  return sum(int(digit) for digit in str(numbers))

print(add(62537))
