import re
import pandas as pd
import numpy as np
import math

df = open('input-dev.txt', "r")
lines = df.readlines()
df.close()

print(lines)

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

print(df_result)

letter_counter = 0

for id in df_result['ID']:
    if id != 0 and id != df_result['ID'].max():
        print(id)
        print('base')
        print(list(df_result[df_result.ID == id]['raw']))
        print(list(df_result[df_result.ID == id]['raw'])[0])
        print(list(list(df_result[df_result.ID == id]['raw'])[0])[
              letter_counter])

        letter_counter = letter_counter+1
