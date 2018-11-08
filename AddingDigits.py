def add(numbers):
  total = 0
  for number in str(numbers):
    total += int(number)
  return total


print(add(432477))


def digAdding(numbers):
  digitsList = []
  for number in str(numbers):
    digitsList.append(int(number))
  return sum(digitsList)

print(digAdding(12342))
