import pandas as pd

# Sample DataFrame 1
data1 = {'sec_id_alias': ['abc', 'xy', 'ghi'], "OTHER_COL":["X","Y","Z"]}
df1 = pd.DataFrame(data1)

# Sample DataFrame 2
data2 = {'key_column': ['abcdef', 'xyz', 'ghijkl'], "MY_COL":["A","B","C"]}
df2 = pd.DataFrame(data2)

def search(regex: str, df, case=False):
    """Search all the text columns of `df`, return rows with any matches."""
    textlikes = df.select_dtypes(include=[object, "string"])
    return df[
        textlikes.apply(
            lambda column: column.str.contains(regex, regex=True, case=case, na=False)
        ).any(axis=1)
    ]

final_df = pd.DataFrame()
for _, row in df1.iterrows():
    result = search(row["sec_id_alias"],df2)
    result = result.assign(sec_id_alias=row["sec_id_alias"])
    final_df = pd.concat([final_df, result])

final_df = pd.merge(df1, final_df, on = "sec_id_alias", how="inner")
print(final_df)

