from csv_diff import load_csv, compare
diff = compare(
    load_csv(open("data_comparision/test_data/american_bankruptcy1.csv"), key=["company_name","year"]),
    load_csv(open("data_comparision/test_data/american_bankruptcy2.csv"), key=["company_name","year"])
)