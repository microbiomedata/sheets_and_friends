import pandas as pd

helper_file = "artifacts/for_data_harmonizer_template/exampleInput/soil_emsl_jgi_mg_capitalizastion_helper.tsv"
helper = pd.read_csv(helper_file, sep="\t")
helper = helper[0:2]
old_col_names = helper[0:1].values[0]
new_col_names = helper[1:2].values[0]
print(old_col_names)
print(new_col_names)

old_file = "data/nmdc_test_data_valid.tsv"
old_frame = pd.read_csv(old_file, sep="\t", skiprows=1)
print(list(old_frame.columns))

old_col_count = len(old_frame.columns)
print(old_col_count)

new_orientation = old_frame[old_col_names]
print(new_orientation)
new_col_count = len(new_orientation.columns)
print(new_col_count)

new_orientation.columns = new_col_names
new_orientation.to_csv("artifacts/nmdc_test_data_valid.tsv", sep="\t", index=False)
