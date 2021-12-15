# Day 2

fn = '02.txt'
commands = open(fn).read().strip().split('\n')

# Part 1
x = 0
d = 0
for line in commands:
    [command, val] = line.strip().split(' ')
    val = int(val)
    if command == 'forward':
        x += val
    if command == 'down':
        d += val
    if command == 'up':
        d -= val
print(x*d)

# Part 2
x = 0
d = 0
a = 0
for line in commands:
    [command, val] = line.strip().split(' ')
    val = int(val)
    if command == 'forward':
        x += val
        d += a*val
    if command == 'down':
        a += val
    if command == 'up':
        a -= val
print(x*d)

