from file_reader import read_data


def find_all_outcomes_part1(outcomes, numbers):
    if len(numbers) == 0:
        return outcomes
    if len(outcomes) == 0:
        outcomes.add(numbers[0])
        return find_all_outcomes_part1(outcomes, numbers[1:])
    
    new_outcomes = set()
    for outcome in outcomes:
        new_outcomes.add(outcome + numbers[0])
        new_outcomes.add(outcome * numbers[0])
    return find_all_outcomes_part1(new_outcomes, numbers[1:])


def find_all_outcomes_part2(outcomes, numbers):
    if len(numbers) == 0:
        return outcomes
    if len(outcomes) == 0:
        outcomes.add(numbers[0])
        return find_all_outcomes_part2(outcomes, numbers[1:])    
    new_outcomes = set()
    for outcome in outcomes:
        new_outcomes.add(outcome + numbers[0])
        new_outcomes.add(outcome * numbers[0])
        new_outcomes.add(int(str(outcome) + str(numbers[0])))
    return find_all_outcomes_part2(new_outcomes, numbers[1:])
        


dataset = read_data('07.txt')
'''
test = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

dataset = test.splitlines()
'''
equations = []
for line in dataset:
    eq = {}
    l = line.strip().split(':')
    eq['result'] = int(l[0])
    eq['numbers'] = [int(x) for x in l[1].split()]
    equations.append(eq)

result1 = 0
result2 = 0
for equation in equations:
    outcome = set()
    if equation['result'] in find_all_outcomes_part1(outcome,equation['numbers']):
        result1 += equation['result']
    outcome2 =  set()
    if equation['result'] in find_all_outcomes_part2(outcome2,equation['numbers']):
        result2 += equation['result']

print(result1)
print(result2)

