def adding(numbers):
  total = 0
  for digit in str(numbers):
    total += int(digit)
  return total


print(adding(546372))

def addingnum(digits):
  return sum(int(num) for num in str(digits))


print(addingnum(11234))
