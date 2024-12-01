import file_reader as fr
from collections import Counter

data = fr.read_data('01.txt')

soucet = 0
left = []
right = []
for pair in data:
    a,b = pair.split()
    left.append(int(a))
    right.append(int(b))

left = sorted(left)
right = sorted(right)
print(left)

for i in range(len(left)):
    soucet += abs(left[i] - right [i])

soucet2 = 0 
counter = Counter(right)

for number in left:
    soucet2 += number * counter[number]


print(soucet)
print(soucet2)
