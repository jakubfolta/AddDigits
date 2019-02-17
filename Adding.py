def adding(dig):
  return sum(int(x) for x in str(dig))

print(adding(37483932))


def add_dig(digi):
  tot = []
  for x in str(digi):
    tot.append(int(x))
  return sum(tot)

print(add_dig(534568))


def adding_dig(num):
  tot = 0
  for x in str(num):
    tot += int(x)
  return tot

print(adding_dig(53446781))

def add_digi(num):
  return sum(int(x) for x in str(num))

print(add_digi(4235612))


def adding(num):
  total = 0
  for x in str(num):
    total += int(x)
  return total

    
print(adding(4245))


def add_dig(numbers):
  total = 0
  for num in str(numbers):
    total += int(num)
  return total

print(add_dig(6573811))


def adding(num):
  return sum(int(dig) for dig in str(num))

print(adding(3237122))


def adding(number):
  total = [0]

  for x in str(number):
    total.append(int(x))
  return sum(total)


print(adding(121))

def addDigits(numbers):
  return sum(int(x) for x in str(numbers))

print(addDigits(121111111))


def addDigits(numbers):
  total = []
  for x in str(numbers):
    total.append(int(x))
  return total

print(addDigits(1121211))

  
