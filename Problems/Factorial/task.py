n = int(input())

count = 1
factorial = 1

while count <= n:
    factorial = factorial * count
    count += 1

print(factorial)
