def adding(number):
  tot = []
  for num in str(number):
    tot.append(int(num))
  return sum(tot)

print(adding(1235678))



def adding(number):
  return sum(int(num) for num in str(number))

print(adding(3446722))


def add(digits):
  total = 0
  for digit in str(digits):
    total += int(digit)
  return total

print(add(1222345))


def adding(numbers):
  numbersGroup = []
  for digit in str(numbers):
    numbersGroup.append(int(digit))
  return sum(numbersGroup)

print(adding(11234))
