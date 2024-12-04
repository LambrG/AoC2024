from file_reader import read_data

def rotate(dataset):
    return [list(row) for row in zip(*dataset)][::-1]

def part1(dataset):
    count = 0
    for y in range(len(dataset)):
        for x in range(len(dataset[y])):
            if dataset[y][x] == 'X':
                try:
                    if dataset[y][x+1] == 'M':
                        if dataset[y][x+2] == 'A':
                            if dataset[y][x+3] =='S':
                                count +=1
                except:
                    pass
                try:
                    if dataset[y+1][x+1] == 'M':
                        if dataset[y+2][x+2] == 'A':
                            if dataset[y+3][x+3] =='S':
                                count +=1
                except:
                    pass
    return(count)

#dataset = read_data('test.txt')
dataset = read_data('04.txt')

for i in range(len(dataset)):
    dataset[i] = list(dataset[i])

count = 0
for i in range(4):
    count += part1(dataset)
    dataset = rotate(dataset)

print(count)
