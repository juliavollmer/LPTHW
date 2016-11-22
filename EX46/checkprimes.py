import calc
mydata = [501, 207, 349, 67, 83, 14579, 839]
result = []
for num in mydata:
    result.append((num, calc.isprime(num)))

print result
