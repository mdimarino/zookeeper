initial_deposit = int(input())

current = initial_deposit
years = 0
while current < 700000:
    current *= 1.071
    years += 1

print(years)
