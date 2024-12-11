from collections import deque, defaultdict


with open('11.txt') as f:
    dataset = deque([int(x) for x in f.read().split()])
#dataset = deque([125,17])


""" for _ in range(25):
    for i in range(len(dataset)):
        x = dataset.popleft()
        digits = len(str(x))
        if x == 0:
            dataset.append(1)
        elif digits % 2 == 0:
            dataset.extend([int(str(x)[:digits//2]), int(str(x)[digits//2:])])
        else:
            dataset.append(x*2024)

print(len(dataset)) """


data_dict = defaultdict(int)
for number in dataset:
    data_dict[number] += 1


for _ in range(75):
    new_data_dict = defaultdict(int)
    for stone, stone_count in data_dict.items():
        digits = len(str(stone))
        if stone == 0:
            new_data_dict[1] += stone_count
        elif digits % 2 == 0:
            new_data_dict[int(str(stone)[:digits//2])] += stone_count
            new_data_dict[int(str(stone)[digits//2:])] += stone_count
        else:
            new_data_dict[stone*2024] += stone_count
    data_dict = new_data_dict

print(sum(data_dict.values()))