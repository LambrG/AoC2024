from collections import defaultdict


def validate(rules, update):
    result = True
    keys = update.keys()
    ruledict = defaultdict(int)
    for rule in rules:        
        x, y = rule
        if x in keys and y in keys:
            ruledict[x] -= 1
            ruledict[y] += 1
            if update[x] > update[y]:
                result = False
    return result, ruledict


with open('05.txt') as f:
    rules, updates = f.read().split('\n\n')

list_of_updates = []
updates = updates.split('\n')

for line in updates[:len(updates)-1]:
    update_pages = {}
    pages = line.split()
    pages = [int(x) for x in line.split(',')]
    update_pages['middle_page'] = pages[len(pages)//2]
    for i, page in enumerate(pages):
        update_pages[page] = i
    list_of_updates.append(update_pages)


rules = [(int(x), int(y)) for line in rules.split('\n') for x, y in [line.split('|')]]

result1 = 0
result2 = 0
for update in list_of_updates:
    valid, ruledict = validate(rules, update)
    if valid:
        result1 += update['middle_page']
    else:
        sorted_rules = sorted(ruledict.items(), key = lambda x: x[1])
        result2 += sorted_rules[len(sorted_rules)//2][0]

print(result1)
print(result2)