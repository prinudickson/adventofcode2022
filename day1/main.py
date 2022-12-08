import numpy as np
agg_list = []
num_list = []

with open('day1-1.txt') as f:
    # with open('day1-1.txt') as f:
    for line in f.readlines():
        if line.strip() != '':
            num_list.append(int(line.strip()))
        else:
            agg_list.append(num_list)
            num_list = []

agg_list.append(num_list)

res = list(map(sum, agg_list))

res.sort()

print("final list - ", str(res))


print("order ma value in list - ", res.index(max(res)))

# d = {}
# for index, value in enumerate(agg_list):
#     d[index] = value

# print(d)


# print(sum([int(values[0]) for key, values in d.items()]))


# for key, value in d:
#     d[key] = sum([int(values[0]) for values in value.items()])
