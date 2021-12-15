# Day 1

fn = 'input.txt'
data = []
for line in open(fn):
    data.append(int(line.strip()))

# Part 1
inc = 0
for ind, val in enumerate(data[:-1]):
    if val < data[ind+1]:
        inc += 1
print(inc)

# Part 2
inc = 0
for ind, val in enumerate(data[:-3]):
    if sum(data[ind:ind+3]) < sum(data[ind+1:ind+4]):
        inc += 1
print(inc)

