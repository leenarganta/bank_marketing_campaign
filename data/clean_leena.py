import pandas as pd
import re

df = pd.read_csv("bank/bank-full.csv", sep=";")

for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].fillna(df[col].mode()[0])
    else:
        df[col] = df[col].fillna(df[col].median())

numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    df = df[(df[col] >= Q1 - 1.5 * IQR) & (df[col] <= Q3 + 1.5 * IQR)]

df["job"] = df["job"].apply(lambda x: re.sub(r"[^a-zA-Z ]+", "", x.lower().strip()))

df.to_csv("bank_cleaned_leena.csv", index=False)
