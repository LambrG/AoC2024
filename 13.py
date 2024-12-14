from file_reader import read_data
import re
from collections import defaultdict

def get_tuple(line):
    extract = pattern.findall(line)
    x, y = extract
    return (int(x), int(y))

dataset = read_data('13.txt')
pattern = re.compile(r"\d+")

machines = []
for j in range(len(dataset)//4 +1):
    i = j*4
    machine = defaultdict()
    machine['A'] = get_tuple(dataset[i])
    machine['B'] = get_tuple(dataset[i+1])
  
    machine['prize'] = get_tuple(dataset[i+2])
    machines.append(machine)
    print(machine)


result = 0

for machine in machines:
    a1, a2 = machine['A']
    b1, b2 = machine['B']
    c1, c2 = machine['prize']
    c1 += 10000000000000
    c2 += 10000000000000
    a_presses = (c1 * b2 - c2 * b1 ) / (a1 * b2 - a2 * b1)
    b_presses = (c1 - a1 * a_presses) / b1
    if a_presses % 1 == 0 and b_presses % 1 == 0:
        result += int(a_presses*3 + b_presses)
    print(a_presses, b_presses)

print(result)