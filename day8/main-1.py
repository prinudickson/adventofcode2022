import re
import pandas as pd
import numpy as np
import math

df = open('input-dev.txt', "r")
lines = df.readlines()
df.close()

# print(lines)

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


def order_element(li, x):
    i = 1
    for l in li:
        if int(l) >= x:
            break
        else:
            i = i+1
    return i


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
        print("#####Values#####")
        print(j)
        col_list = list(df[i])
        # print('initial col list')
        # print('total_list')
        # print(col_list)
        # print(type(col_list))
        row_list = list(df.loc[k])
        # print('initial row list')

        # print(type(row_list))
        # print('Indexes')
        # print(col_list[k])
        # print(row_list[l])
        top_list = split_list(col_list, k, 'start')
        print('top_list')
        print(top_list)
        bottom_list = split_list(col_list, k, 'end')
        print('bottom_list')
        print(bottom_list)

        # print(row_list)
        left_list = split_list(row_list, l, 'start')
        print('left_list')
        print(left_list)
        right_list = split_list(row_list, l, 'end')
        print('right_list')
        print(right_list)
        # col_list.pop(k)
        # # print('Updated col list')
        # # print(col_list)
        # row_list.pop(l)
        # print('Updated row list')
        # print(row_list)
        print("######checks#######")
        top_check = all(int(j) > abs(int(z)) for z in top_list)
        bottom_check = all(int(j) > abs(int(z)) for z in bottom_list)
        left_check = all(int(j) > abs(int(z)) for z in left_list)
        right_check = all(int(j) > abs(int(z)) for z in right_list)
        print(top_check)
        print(bottom_check)
        print(left_check)
        print(right_check)

        overall_check = any([top_check, bottom_check, left_check, right_check])
        print(overall_check)
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
# print('.iloc[0]')
# print(results_df.iloc[0])
# print('.iloc[-1]')
# print(results_df.iloc[-1])
#print('.iloc[:, 0]')
#print(results_df.iloc[:, 0])
#print('.iloc[:, -1]')
#print(results_df.iloc[:, -1])


results_df.iloc[0] = True
results_df.iloc[-1] = True
results_df.iloc[:, 0] = True
results_df.iloc[:, -1] = True

print(results_df)

print(results_df.value_counts())
print(results_df.sum())
print(results_df.sum().sum())
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
