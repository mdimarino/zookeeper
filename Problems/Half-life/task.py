starting_atoms = int(input())
resulting_atoms = int(input())

decay = starting_atoms
counting_days = 0
while decay > resulting_atoms:
    decay //= 2
    counting_days += 1

print(counting_days * 12)
