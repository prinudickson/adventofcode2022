import pandas as pd
import re

# first u have to open  the file and seperate every line like below:

df = open('input.txt', "r")
lines = df.readlines()
df.close()

# remove /n at the end of each line
for index, line in enumerate(lines):
    lines[index] = line.strip()

# creating a dataframe(consider u want to convert your data to 2 columns)

df_result = pd.DataFrame(columns=('ID', 'first_col', 'second_col_expected'))
i = 0
ID = ""
first_col = ""
second_col_expected = ""
for line in lines:
    # you can use "if" and "replace" in case you had some conditions to manipulate the txt data
    ID = i
    first_col = line[:1]
    second_col_expected = line[-1:]
    # this is how you create next line data
    df_result.loc[i] = [ID, first_col, second_col_expected]
    i = i+1


# A, X = Rock
# B, Y = Paper
# C, Z = Scissors
df_result["second_col"] = df_result.apply(lambda row: row["first_col"] if (row["second_col_expected"] == "Y")
                                          else ("A" if (row["second_col_expected"] == "Z" and row["first_col"] == "C")
                                                else ("C" if (row["second_col_expected"] == "Z" and row["first_col"] == "B")
                                                else ("B" if (row["second_col_expected"] == "Z" and row["first_col"] == "A")
                                                      else ("B" if (row["second_col_expected"] == "X" and row["first_col"] == "C")
                                                            else ("A" if (row["second_col_expected"] == "X" and row["first_col"] == "B")
                                                                  else ("C" if (row["second_col_expected"] == "X" and row["first_col"] == "A")
                                                                        else ("unknown"))))))), axis=1)


df_result["outcome"] = df_result.apply(lambda row: "lose" if (row["first_col"] == "A" and row["second_col"] == "C")
                                       else ("lose" if (row["first_col"] == "C" and row["second_col"] == "B")
                                             else ("lose" if (row["first_col"] == "B" and row["second_col"] == "A")
                                                   else ("draw" if (row["first_col"] == "A" and row["second_col"] == "A")
                                                         else ("draw" if (row["first_col"] == "B" and row["second_col"] == "B")
                                                               else ("draw" if (row["first_col"] == "C" and row["second_col"] == "C")
                                                               else ("win")))))), axis=1)


df_result["first_col_points"] = df_result.apply(lambda row: 1 if (row["first_col"] == "A")
                                                else (2 if (row["first_col"] == "B")
                                                      else (3 if (row["first_col"] == "C")
                                                      else (0))), axis=1)

df_result["second_col_points"] = df_result.apply(lambda row: 1 if (row["second_col"] == "A")
                                                 else (2 if (row["second_col"] == "B")
                                                       else (3 if (row["second_col"] == "C")
                                                       else (0))), axis=1)

df_result["outcome_points"] = df_result.apply(lambda row: 6 if (row["outcome"] == "win")
                                              else (0 if (row["outcome"] == "lose")
                                                    else (3 if (row["outcome"] == "draw")
                                                          else (0))), axis=1)


print(df_result.head(20))
print(df_result["second_col_points"].sum())
print(df_result["outcome_points"].sum())

df_result.to_excel("output.xlsx", engine="xlsxwriter")
