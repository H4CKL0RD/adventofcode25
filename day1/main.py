file = open('values.txt', 'r')

read = file.readlines()
dial_counter = 50
real_solution = 0

for line in read:
    if line[0] == 'L':
        print("left")
        dial_counter = dial_counter - int(line[1:-1])
        dial_counter = dial_counter % 100
        print(dial_counter)
        if dial_counter == 0:
            real_solution = real_solution + 1
    if line[0] == "R":
        print("right")
        dial_counter = dial_counter + int(line[1:-1])
        dial_counter = dial_counter % 100
        print(dial_counter)
        if dial_counter == 0:
            real_solution = real_solution + 1

print(real_solution)