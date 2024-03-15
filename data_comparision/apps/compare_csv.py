from argparse import ArgumentParser
import pandas as pd
from dotenv import load_dotenv


def read_file(file_path):
    df = pd.read_csv(file_path, sep=sep, escapechar=escape_char, date_format=date_format)
    return df

def compare_files(files):
    file1 = files[0]
    file2 = files[1]
    file1_df = read_file(file1)
    file2_df = read_file(file2)
    diff = file1_df.compare(file2_df)
    diff.to_csv("diff.csv", index=False)
    print(diff.head(100))

if __name__ == "__main__":
    load_dotenv()
    parser = ArgumentParser()
    parser.add_argument("-sep","-s", required=False, default=",")
    parser.add_argument("-quote_char","-q", required=False, default=None)
    parser.add_argument("-escape_char","-e", required=False, default="\\")
    parser.add_argument("-date_format", "-df", required=False, default=None)
    parser.add_argument("-files","-f", required=True, help="2 comma separated files to compare")
    args = parser.parse_args()
    sep = args.sep
    escape_char = args.escape_char
    date_format = args.date_format
    files = args.files.split(",")
    if len(files)!=2:
        raise Exception("Please enter 2 comma separated files to compare.")
    compare_files(files)

