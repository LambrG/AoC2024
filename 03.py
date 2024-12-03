from file_reader import read_data
import re


dataset = read_data('03.txt')
dataset2 = ''.join(dataset)
pattern1 = r"mul\((\d{1,3}),(\d{1,3})\)"

def extract_line(pattern , line):
    cisla = re.findall(pattern, line)
    dvojice = [(int(x), int(y)) for x, y in cisla]
    soucet = 0
    for dve in dvojice:
        x, y = dve
        soucet += x*y
    return soucet

def additional_instructions(pattern, line):
    split_text = re.split(r"do\(\)", line)
    result = 0
    for element in split_text:
        new_line = re.split(r"don't\(\)", element)[0]
        result += extract_line(pattern, new_line)
    return result


vysledek1 = 0
vysledek2 = 0
test = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
test2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
for line in dataset:
    vysledek1 += extract_line(pattern1, line)

vysledek2 += additional_instructions(pattern1, dataset2)

assert extract_line(pattern1, test) == 161
assert additional_instructions(pattern1, test2) == 48

print(vysledek1)
print(vysledek2)
# print(extract_line(pattern1, test))
# print(additional_instructions(pattern1, test2))

