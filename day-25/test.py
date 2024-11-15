import pandas as pd
import time

start = time.time()
print(start)
titanic = pd.read_csv("titanic_data.csv")
#
# titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)
#
# titanic = pd.read_excel("titanic.xlsx", sheet_name="passengers")

# age_sex = titanic[["Name", "Age", "Sex"]]
#
# above_35 = titanic[titanic["Age"] > 35]
#
# class_23 = titanic[titanic["Pclass"].isin([2, 3])]
#
# class_23 = titanic[(titanic["Pclass"] == 2) | (titanic["Pclass"] == 3)]
#
# age_no_na = titanic[titanic["Age"].notna()]

adult_names = titanic.loc[titanic["Age"] > 35, "Name"]

print(adult_names)
end = time.time()
print(end)
print(end - start)