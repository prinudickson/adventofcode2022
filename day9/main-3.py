import re
import pandas as pd
import numpy as np
import math

input_df = open('input-dev.txt', 'r')
lines = input_df.readlines()
input_df.close()

for index, line in enumerate(lines):
    lines[index] = line.strip()

data_df = pd.DataFrame(columns=('ID', 'raw', 'direction', 'magnitude'))
i = 0
ID = ""
raw = ""
direction = ""
magnitude = ""

starting_point = [0, 0]
path_list = [[0, 0]]
route_list = [[0, 0]]

for line in lines:
    ID = i
    raw = line
    direction = line.split(' ')[0]
    magnitude = line.split(' ')[1]
    new_point = ''
    routes = []
    if direction == 'R':
        prev_point = list(path_list[-1])
        new_point = prev_point.copy()
        new_point[0] = new_point[0]+int(magnitude)
        for k in range(0, int(magnitude)):
            start = prev_point.copy()
            start[0] = start[0]+k
            routes.append(start)
    elif direction == 'L':
        prev_point = list(path_list[-1])
        new_point = prev_point.copy()
        new_point[0] = new_point[0]-int(magnitude)
        for k in range(0, int(magnitude)):
            start = prev_point.copy()
            start[0] = start[0]-k
            routes.append(start)
    elif direction == 'U':
        prev_point = list(path_list[-1])
        new_point = prev_point.copy()
        new_point[1] = new_point[1]+int(magnitude)
        for k in range(0, int(magnitude)):
            start = prev_point.copy()
            start[1] = start[1]+k
            routes.append(start)
    elif direction == 'D':
        prev_point = list(path_list[-1])
        new_point = prev_point.copy()
        new_point[1] = new_point[1]-int(magnitude)
        for k in range(0, int(magnitude)):
            start = prev_point.copy()
            start[1] = start[1]-k
            routes.append(start)
    path_list.append(new_point)
    route_list.append(routes)

    data_df.loc[i] = [ID, raw, direction, magnitude]
    i = i+1

# Clean dataframe
print(data_df)

# All the markers followed by the head.
print(path_list)

# Here we remove the first element as it is there with a [0,0] instead of [[0,0]]
route_list.pop(0)

# Prints the route without the starting point. Make sure to add in the final calculation.
print(route_list)

route_list_flat = [item for sublist in route_list for item in sublist]

print(route_list_flat)

tracker_path = [[0, 0]]
start = [0, 0]

for l in route_list_flat:
    if l == tracker_path[-1]:
        pass
    else:
        print("************")
        new_trace = ''
        print(l, tracker_path[-1])
        v = l[1] - tracker_path[-1][1]
        # print(v)
        h = l[0] - tracker_path[-1][0]
        # print(h)
        if h in [0, 1] and v in [0, 1]:
            print('within threshold')
            print(h, v)
            pass
        elif h == 2 and v in [0, 1]:
            print("horizantal movement here")
            print(h, v)
            new_trace = [tracker_path[-1][0]+h-1, tracker_path[-1][1]+v]
            tracker_path.append(new_trace)
            print(tracker_path)
        elif h in [0, 1] and v == 2:
            print("Vertical movement here")
            print(h, v)
            new_trace = [tracker_path[-1][0]+h, tracker_path[-1][1]+v-1]
            tracker_path.append(new_trace)
            print(tracker_path)
        elif h in [0, -1] and v in [0, -1]:
            print('within threshold')
            print(h, v)
            pass
        elif h == -2 and v in [0, -1]:
            print("Negative horizantal movement here")
            print(h, v)
            new_trace = [tracker_path[-1][0]+h+1, tracker_path[-1][1]+v]
            tracker_path.append(new_trace)
            print(tracker_path)
        elif h in [0, -1] and v == -2:
            print("Negative Vertical movement here")
            print(h, v)
            new_trace = [tracker_path[-1][0]+h, tracker_path[-1][1]+v+1]
            tracker_path.append(new_trace)
            print(tracker_path)

        # elif 0 > v > -2 and 0 > h > -2:
        #     pass
        # elif -2 <= v < 0 and h <= -2:
        #     print("h here")
        #     new_trace = [tracker_path[-1][0]+h+1, tracker_path[-1][1]+v]
        #     tracker_path.append(new_trace)
        #     print(tracker_path)
        # elif -2 <= h < 0 and 0 < v <= -2:
        #     print("v here")
        #     new_trace = [tracker_path[-1][0]+h, tracker_path[-1][1]+v+1]
        #     tracker_path.append(new_trace)
        #     print(tracker_path)
        else:
            pass

print(tracker_path)

# for index, rl in enumerate(route_list):
#     if rl == []:
#         pass
#     else:
#         route_list[index].pop(0)

# print(route_list)

# indices_with_next = []
# indices_without_next = []
# next_pop = 'no'
# for index, rl in enumerate(route_list):
#     if rl == []:
#         next_pop = 'yes'
#         indices_with_next.append(index)
#     elif next_pop == 'yes' and len(rl) > 1:
#         next_pop = 'no'
#     elif next_pop == 'yes' and len(rl) == 1:
#         next_pop = 'no'
#         indices_without_next.append(index)

# index_drop_first_el = [x+1 for x in indices_with_next]

# print(indices_with_next)
# print(index_drop_first_el)
# for d in index_drop_first_el:
#     if route_list[d] == []:
#         pass
#     else:
#         route_list[d].pop(0)

# i = 0
# for d in indices_with_next:
#     route_list.pop(d-i)
#     i = i+1

# # print([value for index, value in enumerate(
# #     route_list) if index != indices_with_next])
# # final_route = [value for index, value in enumerate(
# #     route_list) if index != indices_with_next]

# # print(route_list)

# # print(data_df)
# # print(path_list)
# # print(route_list_ini)
# # print(route_list)
# # number_of_el = -1
# # number_of_null = 0
# # i = 0
# # for el in route_list:
# #     if el != []:
# #         number_of_el += len(el)
# #         print(el)
# #         print(number_of_el)
# #     if el == []:
# #         number_of_null += 1

# # route_list.pop(0)
# #route_list[0] = [[0, 0]]
# route_list_flat = [item for sublist in route_list for item in sublist]

# # print(route_list_flat)

# #route_list_flat_unique = [*set(route_list_flat)]

# uniques = []

# prev_val = ''
# for i in route_list_flat:
#     if i in uniques:
#         pass
#     else:
#         uniques.append(i)

# print(uniques)

# print(len(uniques))

# # print("total number of path steps taken by Tail")
# # print(number_of_el)

# # print("number of unique steps taken by tail")
# # print(len(route_list_flat_unique))

# # print("number of null")
# # print(number_of_null)
# # # print(number_of_el-number_of_null)
