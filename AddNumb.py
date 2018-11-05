def adding(numbers):
  return sum(int(digit) for digit in str(numbers))

print(adding(163783))


def adding(numbers):
  total = 0
  for number in str(numbers):
    total += int(number)
  return total

print(adding(9876))
