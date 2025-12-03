file = open('values.txt', 'r')

read = file.readlines()
position = 50
zero_count = 0

for line in read:
    direction = line[0]
    clicks = int(line[1:])

    # Move 1 click instead
    for _ in range(clicks):
        if direction == 'L':
            position = (position - 1) % 100
        else: # direction R
            position = (position + 1) % 100

        if position == 0:
            zero_count += 1

print(zero_count)
       