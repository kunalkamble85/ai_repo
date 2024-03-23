from argparse import ArgumentParser
import pandas as pd
from dotenv import load_dotenv
import yaml


def load_config(table_name):
    with open(f"./config/{table_name}.yaml") as stream:
        try:
            return yaml.safe_load(stream)
        except:
            print(f"Error while loading yaml file: {table_name}.yaml")

def compare_dataset(df1, df2, unique_key, column_mapping):
    right_on_keys = []
    for key in unique_key:
        if key in column_mapping: right_on_keys.append(column_mapping.get(key))
        else: right_on_keys.append(key)

    result_cols = []
    for col1, col2, in column_mapping.items():
        if col1 == col2 and col1 not in unique_key:
            df1.rename({col1:f"{col1}_x"}, axis = 1)
            df2.rename({col1:f"{col1}_y"}, axis = 1)
            result_cols.append(f"{col1}_x")
            result_cols.append(f"{col1}_y")
        else:
            result_cols.append(col1)
            if col1 != col2: 
                result_cols.append(col2)
    
    df3 = pd.merge(df1, df2, left_on=unique_key, right_on=right_on_keys, how= "outer")
    df3 = df3[result_cols]

    for col1, col2 in column_mapping.items():
        if col1 == col2 and col1 not in unique_key:
            df3[f"{col1}_{col2}_DIFF"] = df3[f"{col1}_x"] == df3[f"{col2}_y"]
        elif col1 not in unique_key:
            df3[f"{col1}_{col2}_DIFF"] = df3[f"{col1}"] == df3[f"{col2}"]
    
    print("\n------------------------------------------------------------------------")
    print(df3.head())
    print("\n------------------------------------------------------------------------")
    df3.to_csv("./data/result.csv", index=False)



def read_files(file1, file2):
    df1 = pd.read_csv(file1, sep=sep, escapechar=escape_char, date_format=date_format)
    df1 = df1.fillna("")
    df2 = pd.read_csv(file2, sep=sep, escapechar=escape_char, date_format=date_format)
    df2 = df2.fillna("")
    return df1, df2


def get_col_to_compare(columns_to_compare, column_mapping):
    if columns_to_compare is None:
        columns_to_compare = [col for col in df1.columns if col in df2.columns]
    if column_mapping is None: column_mapping = {}
    for column in columns_to_compare:
        if column not in column_mapping:
            column_mapping[column] = column
    return columns_to_compare, column_mapping


if __name__ == "__main__":
    load_dotenv()
    parser = ArgumentParser()
    parser.add_argument("-files","-f", required=False, help="2 comma separated files to compare", default="./data/SEC_CAP1.csv,./data/SEC_CAP2.csv")
    parser.add_argument("-sep","-s", required=False, default=",")
    parser.add_argument("-quote_char","-q", required=False, default=None)
    parser.add_argument("-escape_char","-e", required=False, default="\\")
    parser.add_argument("-date_format", "-df", required=False, default=None)
    args = parser.parse_args()
    sep = args.sep
    escape_char = args.escape_char
    date_format = args.date_format
    files = args.files.split(",")
    if len(files) != 2:
        raise Exception("Please enter 2 comma separated files to compare.")
    table_name = "SEC_CAP"
    config_map = load_config(table_name)
    config_map = config_map.get(table_name)
    print(config_map)
    
    df1, df2 = read_files(files[0], files[1])

    unique_key = config_map.get("UNIQUE_KEY")
    columns_to_compare = config_map.get("COLUMNS_TO_MATCH")
    column_mapping = config_map.get("COLUMN_MAPPING")

    columns_to_compare, column_mapping = get_col_to_compare(columns_to_compare, column_mapping)
    compare_dataset(df1, df2, unique_key, column_mapping)

