from file_reader import read_data
import re

dataset = read_data('14.txt')

q1 = q2 = q3 = q4 = 0
for line in dataset:
    x, y, vx, vy = [int(num) for num in re.findall(r"-?\d+", line)]
    #print(x, y, vx, vy, sep="|")
    c = (x + vx*100)%101
    r = (y + vy*100)%103
    #print(c,r)
    if c < 50 and r < 51:
        q1 +=1
    if c < 50 and r > 51:
        q2 += 1
    if c > 50 and r < 51:
        q3 += 1
    if c > 50 and r > 51:
        q4 += 1
    print(q1,q2,q3,q4)

print(q1*q2*q3*q4)

# Thanks to HyperNeutrino
min_product = (len(dataset)//4)**4
best_i = 0

for i in range(101*103):
    q1 = q2 = q3 = q4 = 0
    for line in dataset:
        x, y, vx, vy = [int(num) for num in re.findall(r"-?\d+", line)]
        #print(x, y, vx, vy, sep="|")
        c = (x + vx*i)%101
        r = (y + vy*i)%103
        #print(c,r)
        if c < 50 and r < 51:
            q1 +=1
        if c < 50 and r > 51:
            q2 += 1
        if c > 50 and r < 51:
            q3 += 1
        if c > 50 and r > 51:
            q4 += 1
    res = q1*q2*q3*q4
    if  res < min_product:
        min_product = res
        best_i = i


print(best_i)