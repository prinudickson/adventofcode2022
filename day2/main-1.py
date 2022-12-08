import re
import pandas as pd

# first u have to open  the file and seperate every line like below:

df = open('input.txt', "r")
lines = df.readlines()
df.close()

# remove /n at the end of each line
for index, line in enumerate(lines):
    lines[index] = line.strip()

# creating a dataframe(consider u want to convert your data to 2 columns)

df_result = pd.DataFrame(columns=('ID', 'first_col', 'second_col'))
i = 0
ID = ""
first_col = ""
second_col = ""
for line in lines:
    # you can use "if" and "replace" in case you had some conditions to manipulate the txt data
    ID = i
    first_col = line[:1]
    second_col = line[-1:]
    # this is how you create next line data
    df_result.loc[i] = [ID, first_col, second_col]
    i = i+1


# A, X = Rock
# B, Y = Paper
# C, Z = Scissors

df_result["outcome"] = df_result.apply(lambda row: "lose" if (row["first_col"] == "A" and row["second_col"] == "Z")
                                       else ("lose" if (row["first_col"] == "C" and row["second_col"] == "Y")
                                             else ("lose" if (row["first_col"] == "B" and row["second_col"] == "X")
                                                   else ("draw" if (row["first_col"] == "A" and row["second_col"] == "X")
                                                         else ("draw" if (row["first_col"] == "B" and row["second_col"] == "Y")
                                                               else ("draw" if (row["first_col"] == "C" and row["second_col"] == "Z")
                                                               else ("win")))))), axis=1)


df_result["first_col_points"] = df_result.apply(lambda row: 1 if (row["first_col"] == "A")
                                                else (2 if (row["first_col"] == "B")
                                                      else (3 if (row["first_col"] == "C")
                                                      else (0))), axis=1)

df_result["second_col_points"] = df_result.apply(lambda row: 1 if (row["second_col"] == "X")
                                                 else (2 if (row["second_col"] == "Y")
                                                       else (3 if (row["second_col"] == "Z")
                                                       else (0))), axis=1)

df_result["outcome_points"] = df_result.apply(lambda row: 6 if (row["outcome"] == "win")
                                              else (0 if (row["outcome"] == "lose")
                                                    else (3 if (row["outcome"] == "draw")
                                                          else (0))), axis=1)


print(df_result.head(20))
print(df_result["second_col_points"].sum())
print(df_result["outcome_points"].sum())

df_result.to_excel("output.xlsx", engine="xlsxwriter")
