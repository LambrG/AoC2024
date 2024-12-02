import file_reader as fr

dataset = fr.read_data('02.txt')
sada = []
count1 = 0
count2 = 0

def is_safe(sada):
    
    asceding = 1
    descending = 1
    for i, number in enumerate(sada):
        if i == 0:
            continue
        res = number - sada[i-1]
        asceding *=  0 < res < 4
        descending *= -4 < res < 0
    return asceding + descending

def evaluate_skipped(sada):
    for i in range(len(sada)):
        subset = sada[:i] + sada[i+1:]
        if is_safe(subset) ==1:
            return 1
    return 0


for data in dataset:
    sada = [int(x) for x in data.split()]
    result = is_safe(sada)
    if result == 1:
        count1 += is_safe(sada)
    else:
        count2 += evaluate_skipped(sada)

print(count1)
print(count1 + count2)