f = open("./input1")
lines = [int(l.rstrip()) for l in f]

total = 0
for v in lines:
  a = v/3
  b = int(a) - 2
  total = total + b
  #print(v, a, b)
print("sum:", total)


def fuel(weight):
  fuel_weight = int(weight/3) - 2
  if fuel_weight <= 0:
    return 0
  return fuel_weight + fuel(fuel_weight)

print("corrected for fuel weight: ", sum(map(fuel, lines)))
