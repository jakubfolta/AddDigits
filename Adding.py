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
