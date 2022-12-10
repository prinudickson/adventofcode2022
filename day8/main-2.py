from itertools import takewhile
import re
import pandas as pd
import numpy as np
import math

df = open('input.txt', "r")
lines = df.readlines()
df.close()

# remove /n at the end of each line
for index, line in enumerate(lines):
    lines[index] = line.strip()

df_result = pd.DataFrame(columns=('ID', 'raw'))
i = 0
ID = ""
raw = ""

for line in lines:
    ID = i
    raw = line
    df_result.loc[i] = [ID, raw]
    i = i+1

# print(df_result)

# df2 = pd.DataFrame(list(df_result['raw']))
# print(df2)
df_result['split_trees'] = df_result.apply(
    lambda row: list(row['raw']), axis=1)


df = pd.DataFrame([pd.Series(x) for x in list(df_result.split_trees)])
df.columns = ['col_{}'.format(x+1) for x in df.columns]

# print(df)

# letter_counter = 0


def split_list(x, n, type):
    y = []
    z = 0
    if type == 'start':
        for i in x:
            if z < n and n != 0:
                y.append(i)
            elif n == 0:
                y = ['-1']
            z = z+1
    elif type == 'end':
        for i in x:
            if z > n and n != 0:
                y.append(i)
            elif n == 0:
                y = x
                y.pop(n)
                break
            z = z+1
    if y == []:
        y = ['-1']
    else:
        pass
    return y


# def order_element(li, x):
#     i = 1
#     for l in li:
#         print(l)
#         set_value = ''
#         if int(l) < int(x) and int(l) != -1 and set_value != 'pass':
#             i = i+1
#         else:
#             #i = i
#             set_value = 'pass'
#             # pass
#     return i


# def order_element(li, x):
#     # indices = [
#     #     index for index, item in enumerate(li)
#     #     if int(item) > int(x)

#     # ]
#     indices = []
#     for index, item in enumerate(li):
#         # print(index)
#         # print(item)
#         if int(item) >= int(x):
#             indices.append(index)
#             # print(indices)
#         else:
#             pass

#     # if len(indices) == 0:
#     #     indices = [0]
#     print(indices)

#     if len(indices) == 0:
#         output = 1
#     else:
#         print(indices)
#         try:
#             indices.remove(0)
#         except ValueError:
#             pass
#         if len(indices) == 0:
#             output = 1
#         else:
#             output = min(indices)+1

#     return output

# def order_element(li, x):
#     # return next(l[0] for l in enumerate(li) if int(l[1]) > int(x))
#     #y = filter(lambda x: int(x) > int(x), li)[0]
#     y = np.argwhere(np.array(li) > x)[0][0]
#     return y


# def order_element(seq, m):
#     return [ii for ii in range(0, len(seq)) if seq[ii] > m][0]


# def order_element(l, b):
#     y = len([x for x in takewhile(lambda x: x[1] <= b, enumerate(l))])
#     print(l, b, y)
#     return y+1


# def order_element(l, x):
#     for i in l:
#         if int(i) < int(x):
#             print("****order element****")
#             print(l, x, i, l.index(i)+1)
#             return l.index(i)+1


# def order_element(l, x):
#     temp = -1
#     for i in l:
#         if int(i) >= x:
#             temp = temp + 1
#             print(temp)
#             break
#         if temp < 0:
#             temp = 0
#         else:
#             temp = temp - 1
#     # try:
#     #     result = l.index(i, temp)+1
#     # except ValueError:
#     #     result = l.index(i, temp-1)+1
#     #print(l, x, i, temp, l.index(i, temp)+1)
#     # if all values are less than
#     return l.index(i, temp)+1


def order_element(li, x):
    #indices = [index for index, item in enumerate(li) if item >= x]
    temp = []
    for index, item in enumerate(li):
        if int(item) >= x:
            temp.append(index)
            break
    return temp


def replace_none(x, li):
    print(x, type(x), li)
    if x == []:
        # print("here")
        y = len(li)
    elif x == [0]:
        y = 1
    else:
        #print("not here")
        y = x[0]+1
    return y


print(df)
col = list(df)
# print(col)

#results_df = pd.DataFrame()
results_df = df.iloc[:0, :].copy()
parent_list = []
l = 0
for i in col:
    k = 0
    left_list = []
    right_list = []
    top_list = []
    bottom_list = []
    child_list = []
    for j in df[i]:
        # print("#####Values#####")
        # print(j)
        col_list = list(df[i])
        print('initial col list')
        # print('total_list')
        print(col_list)
        # print(type(col_list))
        row_list = list(df.loc[k])
        print('initial row list')
        print(row_list)
        # print(type(row_list))
        # print('Indexes')
        # print(col_list[k])
        # print(row_list[l])
        top_list = split_list(col_list, k, 'start')
        top_list.reverse()
        #top_list = list(map(int, top_list))
        print('top_list')
        print(top_list)
        bottom_list = split_list(col_list, k, 'end')
        #bottom_list = list(map(int, bottom_list))
        print('bottom_list')
        print(bottom_list)

        # print(row_list)
        left_list = split_list(row_list, l, 'start')
        left_list.reverse()
        #left_list = list(map(int, left_list))
        print('left_list')
        print(left_list)
        right_list = split_list(row_list, l, 'end')
        #right_list = list(map(int, right_list))
        print('right_list')
        print(right_list)
        # print("testcase111111")
        # col_list.pop(k)
        # # print('Updated col list')
        # # print(col_list)
        # row_list.pop(l)
        # print('Updated row list')
        # print(row_list)
        # print("######order#######")
        # top_check = all(int(j) > abs(int(z)) for z in top_list)
        # bottom_check = all(int(j) > abs(int(z)) for z in bottom_list)
        # left_check = all(int(j) > abs(int(z)) for z in left_list)
        # right_check = all(int(j) > abs(int(z)) for z in right_list)
        top_order = replace_none(order_element(top_list, int(j)), top_list)
        # print("testcase1222222")
        bottom_order = replace_none(
            order_element(bottom_list, int(j)), bottom_list)
        left_order = replace_none(order_element(left_list, int(j)), left_list)
        right_order = replace_none(
            order_element(right_list, int(j)), right_list)
        # print(next(l[0]
        #            for l in enumerate(top_list) if int(l[1]) > int(j)))
        # top_order = next(l[0]
        #                  for l in enumerate(top_list) if int(l[1]) > int(j))
        # bottom_order = next(l[0] for l in enumerate(
        #     bottom_list) if int(l[1]) > int(j))
        # left_order = next(l[0]
        #                   for l in enumerate(left_list) if int(l[1]) > int(j))
        # right_order = next(l[0] for l in enumerate(
        #     right_list) if int(l[1]) > int(j))
        print(top_order, bottom_order, left_order, right_order)
        # print(bottom_order)
        # print(left_order)
        # print(right_order)

        overall_check = top_order*bottom_order*left_order*right_order

        # print(overall_check)
        #joined_list = col_list + row_list

        #overall_check = all(z >= j for z in joined_list)
        # print(col_check)
        # print(joined_list)
        child_list.append(overall_check)
        k = k+1

    results_df.loc[l] = child_list
    l = l+1

print(df)
print(results_df)

results_df_t = results_df.T

print("**analyse***")
results_df_t.to_excel("results_df_t.xlsx")
df.to_excel("df.xlsx")

print(results_df.T)

# print('.iloc[0]')
# print(results_df.iloc[0])
# print('.iloc[-1]')
# print(results_df.iloc[-1])
#print('.iloc[:, 0]')
#print(results_df.iloc[:, 0])
#print('.iloc[:, -1]')
#print(results_df.iloc[:, -1])


# results_df.iloc[0] = 0
# results_df.iloc[-1] = 0
# results_df.iloc[:, 0] = 0
# results_df.iloc[:, -1] = 0

print(results_df)

# print(results_df.value_counts())
print(list(results_df.max()))
print(results_df.max().max())
print(results_df_t.max().max())


# for id in df_result['ID']:
#     if id != 0 and id != df_result['ID'].max():
#         print(id)
#         print('base')
#         base = list(list(df_result[df_result.ID == id]['raw'])[0])
#         print(base)
#         t = 1
#         for tree in base:
#             print(list(df_result[df_result.ID == id]['raw']))
#             print(list(df_result[df_result.ID == id]['raw'])[0])
#             print(list(list(df_result[df_result.ID == id]['raw'])[0])[
#                 letter_counter])

#         letter_counter = letter_counter+1
