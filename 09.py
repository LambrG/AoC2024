from collections import deque, defaultdict

with open('09.txt') as f:
    dataset = f.read().strip()



testcase = '2333133121414131402'



filesystem = deque()
files = defaultdict()
empty_space = []
running_sum = 0     
for i, index in enumerate(dataset):
    index = int(index)
    
    if i % 2 == 1:
        if index != 0:
            empty_space.append((len(filesystem),index))
    else:
        files[i//2] = (len(filesystem), index)
    for file in range(index):
        if i % 2 == 1:
            filesystem.append('.')            
        else:
            filesystem.append(i//2)
        running_sum += index

# print(filesystem)
print(empty_space)
print(files)


def part1(filesystem):
    index = 0
    result = 0
    while len(filesystem)> 0:
        first_item = filesystem.popleft()
        if first_item == '.':
            last_item = filesystem.pop()
            while last_item == '.':
                last_item = filesystem.pop()
            result += index * last_item
        else:
            result += index * first_item
        index += 1
    return result

def part2(files, empty_space):
    file_id = len(dataset)//2
    while file_id > 0:
        pos, size = files[file_id]
        for i, (start, lenght) in enumerate(empty_space):
            if start >= pos:
                empty_space = empty_space[:i]
                break
            if size <= lenght:
                files[file_id] = (start, size)
                if size == lenght:
                    empty_space.pop(i)
                else:
                    empty_space[i] = (start + size, lenght - size)
                break
        file_id -= 1
    total = 0
    for id, (position, size) in files.items():
        for i in range(position, position + size):
            total += id * i
    return total             



print(part1(filesystem))
print(part2(files,empty_space))