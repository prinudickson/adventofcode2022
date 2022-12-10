import re
import pandas as pd
import numpy as np
import math

input_df = open('input.txt', 'r')
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


start = [0, 0]


def tracker_path_calc(route_list_flat):
    prev_value = [0, 0]
    for l in route_list_flat:
        if l == prev_value:
            pass
        else:
            new_trace = ''
            v = l[1] - prev_value[1]
            h = l[0] - prev_value[0]
            if h in [-1, 0, 1] and v in [-1, 0, 1]:
                pass
            elif h == 2 and v in [0, 1]:
                new_trace = [prev_value[0]+h-1, prev_value[1]+v]
                print(new_trace)
                prev_value = new_trace.copy()
                # tracker_path.append(new_trace)
                yield new_trace
            elif h in [0, 1] and v == 2:
                new_trace = [prev_value[0]+h, prev_value[1]+v-1]
                print(new_trace)
                prev_value = new_trace.copy()
                # tracker_path.append(new_trace)
                yield new_trace
            elif h == -2 and v in [-1, 0]:
                new_trace = [prev_value[0]+h+1, prev_value[1]+v]
                print(new_trace)
                prev_value = new_trace.copy()
                # tracker_path.append(new_trace)
                yield new_trace
            elif h == -2 and v in [1, 0]:
                new_trace = [prev_value[0]+h+1, prev_value[1]+v]
                print(new_trace)
                prev_value = new_trace.copy()
                # tracker_path.append(new_trace)
                yield new_trace
            elif h == 2 and v in [-1, 0]:
                new_trace = [prev_value[0]+h-1, prev_value[1]+v]
                print(new_trace)
                prev_value = new_trace.copy()
                # tracker_path.append(new_trace)
                yield new_trace
            elif h in [-1, 0] and v == -2:
                new_trace = [prev_value[0]+h, prev_value[1]+v+1]
                print(new_trace)
                prev_value = new_trace.copy()
                # tracker_path.append(new_trace)
                yield new_trace
            elif h in [1, 0] and v == -2:
                new_trace = [prev_value[0]+h, prev_value[1]+v+1]
                print(new_trace)
                prev_value = new_trace.copy()
                # tracker_path.append(new_trace)
                yield new_trace
            else:
                pass


trace_generator = tracker_path_calc(route_list_flat)

# for l in route_list_flat:
#     if l == tracker_path[-1]:
#         pass
#     else:
#         # print("************")
#         new_trace = ''
#         #print(l, tracker_path[-1])

#         v = l[1] - tracker_path[-1][1]
#         # print(v)
#         h = l[0] - tracker_path[-1][0]
#         #print(h, v)
#         # print(h)
#         if h in [-1, 0, 1] and v in [-1, 0, 1]:
#             # print('within threshold#')
#             #print(h, v)
#             pass
#         elif h == 2 and v in [0, 1]:
#             # print("horizantal movement here#")
#             #print(h, v)
#             new_trace = [tracker_path[-1][0]+h-1, tracker_path[-1][1]+v]
#             tracker_path.append(new_trace)
#             # print(tracker_path)
#         elif h in [0, 1] and v == 2:
#             # print("Vertical movement here#")
#             #print(h, v)
#             new_trace = [tracker_path[-1][0]+h, tracker_path[-1][1]+v-1]
#             tracker_path.append(new_trace)
#             # print(tracker_path)
#         # elif h in [0, -1] and v in [0, -1]:
#         #     print('within threshold#')
#         #     print(h, v)
#         #     pass
#         elif h == -2 and v in [-1, 0]:
#             #print("Negative horizantal movement here$$$$$$$$$$$")
#             #print(h, v)
#             new_trace = [tracker_path[-1][0]+h+1, tracker_path[-1][1]+v]
#             tracker_path.append(new_trace)
#             # print(tracker_path)
#         elif h == -2 and v in [1, 0]:
#             # print("Negative horizantal POSITIVE VERTICAL movement here#")
#             #print(h, v)
#             new_trace = [tracker_path[-1][0]+h+1, tracker_path[-1][1]+v]
#             tracker_path.append(new_trace)
#             # print(tracker_path)
#         elif h == 2 and v in [-1, 0]:
#             #print("POsitive Horizontal, Negative Vertical movement here")
#             #print(h, v)
#             new_trace = [tracker_path[-1][0]+h-1, tracker_path[-1][1]+v]
#             tracker_path.append(new_trace)
#             # print(tracker_path)
#         elif h in [-1, 0] and v == -2:
#             #print("Negative Vertical movement here")
#             #print(h, v)
#             new_trace = [tracker_path[-1][0]+h, tracker_path[-1][1]+v+1]
#             tracker_path.append(new_trace)
#             # print(tracker_path)
#         elif h in [1, 0] and v == -2:
#             # print("Negative Vertical POSITIVE horizontal movement here#")
#             #print(h, v)
#             new_trace = [tracker_path[-1][0]+h, tracker_path[-1][1]+v+1]
#             tracker_path.append(new_trace)
#             # print(tracker_path)
#         else:
#             pass
print("route list")
print(route_list_flat)
print("traces")
print(trace_generator)
print("$$$$Length of the initial route path")
print(len(route_list))
print("$$$$Length of th etracker path")
# print(len(trace_generator))
i = 0
for x in trace_generator:
    # print(x)
    i = i+1

print(i)

# for index, rl in enumerate(route_list):
#     if rl == []:
#         pass
#     else:
#         route_list[index].pop(0)
# print(route_list)

# print(route_list_flat)

# print(data_df)
# uniques = []

# #prev_val = ''
# for i in tracker_path:
#     # print(i)
#     # print(uniques)
#     if i in uniques:
#         #print("appending this")
#         # print(uniques)
#         pass
#     else:
#         uniques.append(i)

# # print(uniques)
# print("length of uniques")
# print(len(uniques))
