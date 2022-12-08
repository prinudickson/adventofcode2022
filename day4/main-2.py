import re
import pandas as pd
import numpy as np

# first u have to open  the file and seperate every line like below:

df = open('input.txt', "r")
lines = df.readlines()
df.close()

# remove /n at the end of each line
for index, line in enumerate(lines):
    lines[index] = line.strip()

print(lines)

# creating a dataframe(consider u want to convert your data to 2 columns)
df_result = pd.DataFrame(columns=('ID', 'raw','first_col', 'second_col'))
i = 0
ID = ""
first_col = ""
second_col = ""
for line in lines:
    # you can use "if" and "replace" in case you had some conditions to manipulate the txt data
    ID = i
    raw = line
    # this is how you create next line data
    df_result.loc[i] = [ID, raw, first_col, second_col]
    i = i+1

# mylist = [[i+1]*3 for i in range(len(df_result))]
# col_list = ['a', 'b', 'c']
# collist = [[i] for i in col_list]
# df_result['group_id'] = np.resize(mylist,len(df_result))
# df_result['col_list'] = np.resize(collist,len(df_result))

print(df_result.head())

df_expanded = df_result['raw'].str.split(',', expand=True)
df_expanded.columns = ['col'+str(i) for i in df_expanded.columns]
df_expanded["raw"] = df_result["raw"]
print(df_expanded.head())


df_expanded['range_0'] = df_expanded.apply(lambda row: list(range(int(row['col0'].split('-')[0]),int(row['col0'].split('-')[1])+1)), axis=1)
df_expanded['range_1'] = df_expanded.apply(lambda row: list(range(int(row['col1'].split('-')[0]),int(row['col1'].split('-')[1])+1)), axis=1)

df_expanded['overlaps'] = df_expanded.apply(lambda row: 1 if (len(set(row['range_0'])&set(row['range_1'])) > 0)
                                                                else(0), axis=1)
print(df_expanded.head())


# print(df_groups)

# def common_letters(s1, s2, s3):
#     a=list(set(s1)&set(s2)&set(s3))
#     return a[0]

# # ##Alphabet order ---
print(df_expanded.overlaps.sum())
# # Generate lowercase Mapping
# lower_case = {chr(i+96):i for i in range(1,27)}
# # Generates :
# # {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13, 'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}

# # Generate UPPERCASE Mapping
# upper_case_raw = {chr(i+64):i for i in range(1,27)}

# # Generates :
# # {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

# some_constant = 26
# upper_case = {k:v+some_constant for k,v in upper_case_raw.items()}

# def merge_dict(dict1, dict2):
#     return(dict2.update(dict1))

# alphabet_order = {}
# alphabet_order = lower_case | upper_case


# # ## Identify priority --- 
# # df_groups = pd.DataFrame(df_groups)
# df_groups["common_letters"] = df_groups.apply(lambda row: common_letters(row["a"], row["b"], row["c"]), axis = 1)

# df_groups["priority_letter"] = df_groups.apply(lambda row: alphabet_order.get(row['common_letters'], 'NO KEY'), axis=1)

# print(df_groups.head())
# print(df_groups['priority_letter'].sum())