import re
import pandas as pd
import numpy as np
import math

df = open('input.txt', "r")
lines = df.readlines()
df.close()

# print(lines)

# remove /n at the end of each line
for index, line in enumerate(lines):
    lines[index] = line.strip()


df_result = pd.DataFrame(
    columns=('ID', 'raw', 'classification', 'name', 'current_folder', 'size', 'parent_order', 'parent_folder'))
i = 1
ID = ""
raw = ""
classification = ""
parent_list = ['root']
current_folder = '/'
prev_value = ""
parent_folder = ""
parent_order = 0

for line in lines:
    ID = i
    raw = line
    # parent_folder = '/'
    if line != prev_value:
        parent_order = 0
    else:
        parent_order = 1
    prev_value = line

    if line.split(' ')[0] == '$':
        classification = 'command'
        size = 0
        name = ''
        if line.split(' ')[1] == 'cd' and line.split(' ')[2] != '/' and line.split(' ')[2] != '..':
            current_folder = line.split(' ')[2]
            #current_folder = parent_list[0]+line.split(' ')[2]
            name = line.split(' ')[2]
            parent_list.append(list(reversed(parent_list))
                               [0]+'-'+current_folder)
            # print(parent_list)
        if line.split(' ')[1] == 'cd' and line.split(' ')[2] != '/' and line.split(' ')[2] == '..':
            current_folder = line.split(' ')[2]
            #current_folder = parent_list[0]+line.split(' ')[2]
            name = line.split(' ')[2]
            # print('parent_order*******')
            # print(parent_order)
            # print(type(parent_order))
            #print("adding new to parent list gen")
            # print(list(reversed(parent_list)))
            #ad_x = 1 + parent_order
            # print(ad_x)
            # print("use_input")
            # print(list(reversed(parent_list))
            #       [0].split('-')[:-(1)])
            to_append = list(reversed(parent_list))[0].split('-')[:-(1)]
            parent_list.append('-'.join(to_append))
            # print('after appending')

        else:
            pass
    elif line.split(' ')[0] == 'dir':
        classification = 'folder'
        name = line.split(' ')[1]
        size = 0
    elif line.split(' ')[0].isnumeric():
        classification = 'file'
        name = line.split(' ')[1]
        size = int(line.split(' ')[0])
    else:
        classification = 'unknown'

    print('line')
    print(line)
    # print('parent_order')
    # print(parent_order)
    # print('parent_list')
    # print(parent_list)

    if current_folder == '/':
        parent_folder = 'root'
    else:
        # updated_list = parent_list
        # updated_list.reverse()
        # print('updated_list')
        # print(updated_list)
        # print(parent_order)
        # if updated_list[parent_order] != '..':
        #     parent_folder = updated_list[parent_order]
        # elif updated_list[parent_order+1] != '..':
        #     parent_folder = updated_list[parent_order+1]
        # elif updated_list[parent_order+2] != '..':
        #     parent_folder = updated_list[parent_order+2]
        # elif updated_list[parent_order+3] != '..':
        #     parent_folder = updated_list[parent_order+3]
        print('reversed list')
        print(list(reversed(parent_list)))
        if list(reversed(parent_list))[0] != '..':
            parent_folder = list(reversed(parent_list))[0]
            print("value from reversed list 1")
            print(list(reversed(parent_list))[0])
        elif list(reversed(parent_list))[parent_order+1] != '..':
            parent_folder = list(reversed(parent_list))[parent_order+1]
            print("value from reversed list 2")
            print(list(reversed(parent_list))[parent_order+1])
        elif list(reversed(parent_list))[parent_order+2] != '..':
            parent_folder = list(reversed(parent_list))[parent_order+2]
            print("value from reversed list 3")
            print(list(reversed(parent_list))[parent_order+2])
        elif list(reversed(parent_list))[parent_order+3] != '..':
            parent_folder = list(reversed(parent_list))[parent_order+3]
            print("value from reversed list 4")
            print(list(reversed(parent_list))[parent_order+3])

    df_result.loc[i] = [ID, raw, classification,
                        name, current_folder, size, parent_order, parent_folder]
    print("*************")
    i = i+1

# print(df_result)

df_summarised = df_result.groupby(
    'parent_folder', as_index=False).agg({"size": "sum"})

df_summarised = df_summarised.sort_values(
    by='size', ascending=False, na_position='last')

# print(df_summarised.head(20))

df_size_list = pd.DataFrame(columns=(
    'ID', 'parent_folder', 'size', 'size_list', 'size_list_num', 'size_total'))

a = 0

for x in df_summarised['parent_folder']:
    ID = a
    size = ''
    size_list = ''
    size_list_num = ''
    size_total = ''
    parent_folder = x
    size = list(df_summarised[df_summarised.parent_folder == x]['size'])[0]
    temp_list = []
    for y in df_summarised['parent_folder']:
        if y != x:
            if y.find(x) != -1:
                temp_list.append(
                    list(df_summarised[df_summarised.parent_folder == y]['size'])[0])
            else:
                pass
        else:
            pass
    print(x)
    print(temp_list)
    size_list = temp_list
    size_list_num = sum(size_list)
    size_total = size + size_list_num

    df_size_list.loc[a] = [ID, parent_folder, size,
                           size_list, size_list_num, size_total]

    a = a+1

# print(df_size_list)

df_size_list.to_excel("df_size_list.xlsx")

# i = 1
# ID = ''
# folder_name = ''
# size = ''
# df_folders = pd.DataFrame(columns=('ID', 'folder_name', 'size'))

# folder_list = list(df_result['current'].unique())
# folder_list.reverse()

# # copy_df_result = df_result
# print(folder_list)
# print(len(folder_list))

# for x in folder_list:
#     ID = i
#     folder_name = x
#     # print(df_result[df_result['parent_raw'] == x]['size'])
#     size_list = list(df_result[df_result['current'] == x]['size'])
#     size_list = [i for i in size_list if i != '']
#     # print(size_list)
#     size = 0
#     for s in range(0, len(size_list)):
#         size = size+size_list[s]

#     df_folders.loc[i] = [ID, folder_name, size]
#     df_result['size'] = df_result.apply(lambda row: size if (row['folder_name'] == x and row['classification'] == 'folder')
#                                         else (row['size']), axis=1)

#     i = i+1

# df_summarised.to_excel('summarydata.xlsx')
# df_result["raw_shif"] = df_result["raw"].shift()

# raw_list = list(df_result.raw)
# updated_list = []
# prev_value = ''

# for i in raw_list:
#     if i != prev_value:
#         updated_list.append(0)
#     else:
#         updated_list.append(1)
#     prev_value = i

# df_result['parent_order'] = updated_list

# print(df_result)
# print(raw_list)
# print(updated_list)
# df_result['classification'] = df_result.apply(lambda row: 'command' if row['raw'].split(' ')[0] == '$'
#                                               else ('folder' if row['raw'].split(' ')[0] == 'dir'
#                                               else ('file' if row['raw'].split(' ')[0].isnumeric()
#                                                     else ('unknown'))), axis=1)

# df_result['size'] = df_result.apply(lambda row: int(row['raw'].split(' ')[0]) if row['classification'] == 'file'
#                                     else (''), axis=1)

# df_result['parent'] = df_result.apply(lambda row: )

# list_of_folders = df_result.apply(lambda row: row['raw'].split(' ')[1] == 'cd']
# print(list_of_folders)
# df_result['current_raw'] = df_result.apply(lambda row: row['raw'].split(' ')[2] if row['classification'] == 'command' and len(row['raw'].split(' ')) > 2
#                                            else (''), axis=1)

# df_result['folder_name'] = df_result.apply(lambda row: row['raw'].split(' ')[1] if row['classification'] == 'folder'
#                                            else (''), axis=1)

# df_result['current'] = df_result['current_raw'].replace(
#     '', np.NaN).fillna(method='ffill')

# df_result['folder_unique'] = df_result.apply(lambda row: row['current']+row['folder_name'] if row['folder_name'] != ''
#                                              else (''), axis=1)

# parent_list_raw = list(df_result['current'])


# parent_list = []

# prev = ''
# prev_prev = ''
# for x in parent_list_raw:
#     if x == '/':
#         parent_list.append(x)
#         prev = x
#         prev_prev = x
#     elif x != '/' and x != '..':
#         parent_list.append(prev)
#         prev = x
#         prev_prev = prev
#     elif x == '..':
#         prev = prev_prev
#         parent_list.append(prev)

#         prev_prev = prev_prev

# print(parent_list_raw)
# print(parent_list)

# df_result['current_folder'] = ""


# # df_result['parent_name'] = df_result.apply(lambda row: row['raw'].split(' ')[1] if row['classification'] == 'folder'
# #                                            else (''), axis=1)


# # df_result['folder_parent'] = df_result.apply(lambda row: row[''])

# #df_result['current_folder'] = ""

# # current_folder = '/'

# # for i in df_result[ID]:
# #     if df_result[df_result['ID'] == i]['raw'].split(' ')[2] == '/':
# #         df_result[df_result['ID'] == i]['current_folder'] = current_folder


# # def assign_prev(a, i):
# #     return np.concatenate(([False], a[1:] == a[:-1]))


# #df['match'] = comp_prev(df.col1.values)

# i = 1
# ID = ''
# folder_name = ''
# size = ''
# df_folders = pd.DataFrame(columns=('ID', 'folder_name', 'size'))

# folder_list = list(df_result['current'].unique())
# folder_list.reverse()

# # copy_df_result = df_result
# print(folder_list)
# print(len(folder_list))

# for x in folder_list:
#     ID = i
#     folder_name = x
#     # print(df_result[df_result['parent_raw'] == x]['size'])
#     size_list = list(df_result[df_result['current'] == x]['size'])
#     size_list = [i for i in size_list if i != '']
#     # print(size_list)
#     size = 0
#     for s in range(0, len(size_list)):
#         size = size+size_list[s]

#     df_folders.loc[i] = [ID, folder_name, size]
#     df_result['size'] = df_result.apply(lambda row: size if (row['folder_name'] == x and row['classification'] == 'folder')
#                                         else (row['size']), axis=1)

#     i = i+1

# # print(df_folders)
# # print(folder_list)
# # print(copy_df_result)
# print(df_result)

# # print(df_result.dtypes)

# df_summarised_raw = df_result[['current', 'size']]

# # print(df_summarised_raw)
# df_summarised_raw = df_summarised_raw.replace(
#     '', np.NaN).dropna(
#     axis=0,
#     how='any',
# )

# # print(df_summarised_raw)

# df_summarised = df_summarised_raw.groupby(
#     'current', as_index=False).agg({"size": "sum"})

# df_summarised = df_summarised.sort_values(
#     by='size', ascending=False, na_position='first')

# print(df_summarised.head(15))

# print(df_summarised[df_summarised['size'] > 100000]['size'])


#     #updating the arrangement every loop...
#     #variable = 'stack_'+str(frm)
#     arrangement_process_selection_1 = arrangement_process[arrangement_process['variable'] == 'stack_'+str(frm)]
#     arrangement_process_selection_2 = arrangement_process_selection_1.nlargest(int(qnty), 'order_id')

#     #remove current record from arangement_process
#     arrangement_process_removal_1 = pd.concat([arrangement_process,arrangement_process_selection_2]).drop_duplicates(keep=False)
#     #print(arrangement_process)
#     #print(arrangement_process_selection_2)

#     assignment_order_start = arrangement_process[arrangement_process['variable'] == 'stack_'+str(to)]['order_id'].max()
#     if math.isnan(assignment_order_start):
#         assignment_order_start = 0
#     else:
#         pass
#     #print(assignment_order_start)

#     #updating records and adding them back.
#     arrangement_process_selection_2['variable'] = arrangement_process_selection_2.apply(lambda row: 'stack_'+str(to), axis=1)
#     #print(arrangement_process_selection_2)


#     order_list = [[k+1] for k in range(len(arrangement_process_selection_2))]
#     #print(order_list)
#     #print(type(order_list))
#     order_list.reverse()

#     #print(order_list)
#     order_list_upd = [int(x[0])+assignment_order_start for x in order_list]
#     #print(order_list_upd)

#     arrangement_process_selection_2['order_id'] = np.resize(order_list_upd,len(arrangement_process_selection_2))
#     records_tobe_added = arrangement_process_selection_2
#     #print(records_tobe_added)
#     #print(type(records_tobe_added))
#     #print(arrangement_process_removal_1)
#     #print(type(arrangement_process_removal_1))
#     frames = [arrangement_process_removal_1, records_tobe_added]
#     arrangement_process = pd.concat(frames)
#     #print(arrangement_process)

#     i = i+1


# print(arrangement_process)

# arrangement_process_wide = pd.pivot(arrangement_process, index=['order_id'], columns='variable', values='value')
# print(arrangement_process_wide)
# #print(df_result.head())
# # # mylist = [[i+1]*3 for i in range(len(df_result))]
# # # col_list = ['a', 'b', 'c']
# # # collist = [[i] for i in col_list]
# # # df_result['group_id'] = np.resize(mylist,len(df_result))
# # # df_result['col_list'] = np.resize(collist,len(df_result))

# # print(df_result.head())

# # df_expanded = df_result['raw'].str.split(',', expand=True)
# # df_expanded.columns = ['col'+str(i) for i in df_expanded.columns]
# # df_expanded["raw"] = df_result["raw"]
# # print(df_expanded.head())


# # df_expanded['range_0'] = df_expanded.apply(lambda row: list(range(int(row['col0'].split('-')[0]),int(row['col0'].split('-')[1])+1)), axis=1)
# # df_expanded['range_1'] = df_expanded.apply(lambda row: list(range(int(row['col1'].split('-')[0]),int(row['col1'].split('-')[1])+1)), axis=1)

# # df_expanded['overlaps'] = df_expanded.apply(lambda row: 1 if ((set(row['range_0']).issubset(set(row['range_1']))) or (set(row['range_1']).issubset(set(row['range_0']))))
# #                                                                 else(0), axis=1)
# # print(df_expanded.head())


# # # print(df_groups)

# # # def common_letters(s1, s2, s3):
# # #     a=list(set(s1)&set(s2)&set(s3))
# # #     return a[0]

# # # # ##Alphabet order ---
# # print(df_expanded.overlaps.sum())
# # # # Generate lowercase Mapping
# # # lower_case = {chr(i+96):i for i in range(1,27)}
# # # # Generates :
# # # # {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13, 'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}

# # # # Generate UPPERCASE Mapping
# # # upper_case_raw = {chr(i+64):i for i in range(1,27)}

# # # # Generates :
# # # # {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

# # # some_constant = 26
# # # upper_case = {k:v+some_constant for k,v in upper_case_raw.items()}

# # # def merge_dict(dict1, dict2):
# # #     return(dict2.update(dict1))

# # # alphabet_order = {}
# # # alphabet_order = lower_case | upper_case


# # # # ## Identify priority ---
# # # # df_groups = pd.DataFrame(df_groups)
# # # df_groups["common_letters"] = df_groups.apply(lambda row: common_letters(row["a"], row["b"], row["c"]), axis = 1)

# # # df_groups["priority_letter"] = df_groups.apply(lambda row: alphabet_order.get(row['common_letters'], 'NO KEY'), axis=1)

# # # print(df_groups.head())
# # # print(df_groups['priority_letter'].sum())
