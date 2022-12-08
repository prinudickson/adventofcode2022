import re
import pandas as pd
import numpy as np
import math


print("********************************")

#Read the arrangement data.. 

df_arrangement = pd.read_excel('input-arrangement.xlsx')
# lines_arrangement = df_arrangement.readlines()
# df_arrangement.close()

# # remove /n at the end of each line
# for index, line in enumerate(lines_arrangement):
#     lines_arrangement[index] = line.strip()
#     print(line)

# df_arrangement = pd.DataFrame(columns=('ID','raw','stack_1','stack_2','stack_3'))
# i = 0
# ID = ""
# stack_1 = ""
# stack_2 = ""
# stack_3 = ""

# for line in lines_arrangement:
#     ID = i
#     raw = line
#     # this is how you create next line data
#     print(line)
#     print(type(line))
#     print(line.split(''))
#     print(type(line.split(' ')))
#     stack_1 = line.split(' ')[0]
#     stack_2 = line.split(' ')[1]
#     stack_3 = line.split(' ')[2]
#     df_arrangement.loc[i] = [ID, raw,stack_1, stack_2, stack_3]

print(df_arrangement)

ini_arrangement_raw = df_arrangement
#ini_arrangement_raw = pd.read_csv('input-ini-dev.txt', header=None, delim_whitespace=True, names='stack_1 stack_2 stack_3'.split(' '))

mylist = [[i+1] for i in range(len(ini_arrangement_raw))]
mylist.reverse()
ini_arrangement_raw['order_id'] = np.resize(mylist,len(ini_arrangement_raw))
ini_arrangement_raw['order_id'] = ini_arrangement_raw.apply(lambda row: row['order_id'], axis=1)
#ini_arrangement_raw = ini_arrangement_raw[:-1]
print(ini_arrangement_raw)

#Convert the initial arrangement into long format.. 
ini_arrangement = pd.melt(ini_arrangement_raw, id_vars='order_id', value_vars=['stack_1', 'stack_2', 'stack_3', 'stack_4', 'stack_5', 'stack_6', 'stack_7', 'stack_8', 'stack_9'])
#ini_arrangement=ini_arrangement[~ini_arrangement['value'].isna()]
print(len(ini_arrangement))
# ini_arrangement['value'].replace('', np.nan, inplace=True)
# #ini_arrangement=ini_arrangement[ini_arrangement['value'].astype(bool)]  
# ini_arrangement.dropna(subset=['value'], inplace=True)
# ini_arrangement.dropna(inplace = True)
print(ini_arrangement['value'][8])
print(type(ini_arrangement['value'][8]))
ini_arrangement['value'] = ini_arrangement['value'].str.strip()
ini_arrangement = ini_arrangement[ini_arrangement['value'] !='']

print(len(ini_arrangement))
print("Checkpoint")
print(ini_arrangement.head(10))



df = open('input-movement.txt', "r")
lines = df.readlines()
df.close()

# remove /n at the end of each line
for index, line in enumerate(lines):
    lines[index] = line.strip()

arrangement_process = ini_arrangement

df_result = pd.DataFrame(columns=('ID', 'raw','frm', 'to', 'qnty'))
i = 0
ID = ""
raw = ""
frm = ""
to = ""
qnty = ""

for line in lines:
    ID = i
    raw = line
    # this is how you create next line data
    frm = line.split(' ')[3]
    to = line.split(' ')[5]
    qnty = line.split(' ')[1]
    df_result.loc[i] = [ID, raw, frm, to, qnty]

    #updating the arrangement every loop...
    #variable = 'stack_'+str(frm)
    arrangement_process_selection_1 = arrangement_process[arrangement_process['variable'] == 'stack_'+str(frm)]
    arrangement_process_selection_2 = arrangement_process_selection_1.nlargest(int(qnty), 'order_id')

    #remove current record from arangement_process
    arrangement_process_removal_1 = pd.concat([arrangement_process,arrangement_process_selection_2]).drop_duplicates(keep=False)
    #print(arrangement_process)
    #print(arrangement_process_selection_2)

    assignment_order_start = arrangement_process[arrangement_process['variable'] == 'stack_'+str(to)]['order_id'].max()
    if math.isnan(assignment_order_start):
        assignment_order_start = 0
    else:
        pass
    #print(assignment_order_start)

    #updating records and adding them back. 
    arrangement_process_selection_2['variable'] = arrangement_process_selection_2.apply(lambda row: 'stack_'+str(to), axis=1)
    #print(arrangement_process_selection_2)
    

    order_list = [[k+1] for k in range(len(arrangement_process_selection_2))]
    #print(order_list)
    #print(type(order_list))
    order_list.reverse()

    #print(order_list)
    order_list_upd = [int(x[0])+assignment_order_start for x in order_list]
    #print(order_list_upd)

    arrangement_process_selection_2['order_id'] = np.resize(order_list_upd,len(arrangement_process_selection_2))
    records_tobe_added = arrangement_process_selection_2
    #print(records_tobe_added)
    #print(type(records_tobe_added))
    #print(arrangement_process_removal_1)
    #print(type(arrangement_process_removal_1))
    frames = [arrangement_process_removal_1, records_tobe_added]
    arrangement_process = pd.concat(frames)
    #print(arrangement_process)

    i = i+1


print(arrangement_process)

arrangement_process_wide = pd.pivot(arrangement_process, index=['order_id'], columns='variable', values='value')
print(arrangement_process_wide)
#print(df_result.head())
# # mylist = [[i+1]*3 for i in range(len(df_result))]
# # col_list = ['a', 'b', 'c']
# # collist = [[i] for i in col_list]
# # df_result['group_id'] = np.resize(mylist,len(df_result))
# # df_result['col_list'] = np.resize(collist,len(df_result))

# print(df_result.head())

# df_expanded = df_result['raw'].str.split(',', expand=True)
# df_expanded.columns = ['col'+str(i) for i in df_expanded.columns]
# df_expanded["raw"] = df_result["raw"]
# print(df_expanded.head())


# df_expanded['range_0'] = df_expanded.apply(lambda row: list(range(int(row['col0'].split('-')[0]),int(row['col0'].split('-')[1])+1)), axis=1)
# df_expanded['range_1'] = df_expanded.apply(lambda row: list(range(int(row['col1'].split('-')[0]),int(row['col1'].split('-')[1])+1)), axis=1)

# df_expanded['overlaps'] = df_expanded.apply(lambda row: 1 if ((set(row['range_0']).issubset(set(row['range_1']))) or (set(row['range_1']).issubset(set(row['range_0']))))
#                                                                 else(0), axis=1)
# print(df_expanded.head())


# # print(df_groups)

# # def common_letters(s1, s2, s3):
# #     a=list(set(s1)&set(s2)&set(s3))
# #     return a[0]

# # # ##Alphabet order ---
# print(df_expanded.overlaps.sum())
# # # Generate lowercase Mapping
# # lower_case = {chr(i+96):i for i in range(1,27)}
# # # Generates :
# # # {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13, 'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}

# # # Generate UPPERCASE Mapping
# # upper_case_raw = {chr(i+64):i for i in range(1,27)}

# # # Generates :
# # # {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

# # some_constant = 26
# # upper_case = {k:v+some_constant for k,v in upper_case_raw.items()}

# # def merge_dict(dict1, dict2):
# #     return(dict2.update(dict1))

# # alphabet_order = {}
# # alphabet_order = lower_case | upper_case


# # # ## Identify priority --- 
# # # df_groups = pd.DataFrame(df_groups)
# # df_groups["common_letters"] = df_groups.apply(lambda row: common_letters(row["a"], row["b"], row["c"]), axis = 1)

# # df_groups["priority_letter"] = df_groups.apply(lambda row: alphabet_order.get(row['common_letters'], 'NO KEY'), axis=1)

# # print(df_groups.head())
# # print(df_groups['priority_letter'].sum())