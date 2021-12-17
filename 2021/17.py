#!/usr/bin/env python
# coding: utf-8

# In[20]:


xtar = [150, 193]
ytar = [-136, -86]


# Part 1

ymax = 0
vy0_max = 0

vy_list = list(range(1000))
for vy0 in vy_list:
    vy = vy0
    y, y_localmax = 0, 0
    while True:
        y = y + vy
        if y > y_localmax:
            y_localmax = y
        vy -= 1
        if min(ytar) <= y <= max(ytar):
            if y_localmax > ymax:
                ymax = y_localmax
                vy0_max = vy0
            break
        if y < min(ytar):
            break
print('Max y', ymax)
print('Max vy0:', vy0_max)


# Part 2

def inTarget(x, y, xtar, ytar):
    if min(xtar) <= x <= max(xtar):
        if min(ytar) <= y <= max(ytar):
            return(True)
    return(False)


vx_list = list(range(1, max(xtar)+1))
vy_list = list(range(min(ytar), 140))

winners = 0
for vx0 in vx_list:
    for vy0 in vy_list:
        vx = vx0
        vy = vy0
        x, y = 0, 0
        while True:
            x += vx
            y += vy
            if vx > 0:
                vx -= 1
            vy -= 1
            if inTarget(x, y, xtar, ytar):
                winners += 1
                break
            if y < min(ytar):
                break
            if x > max(xtar):
                break
print('Solutions:', winners)

