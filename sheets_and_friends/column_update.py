import os.path

import pandas as pd

from pathlib import Path

old_file = "data/nmdc_test_data_valid.tsv"

extension_val = ".tsv"
suffix_val = "_lowercased"
path_prefix = "artifacts"

basename = Path(old_file).stem
with_extension = basename + suffix_val + extension_val
with_path = os.path.join(path_prefix, with_extension)

helper_file = "artifacts/for_data_harmonizer_template/exampleInput/soil_emsl_jgi_mg_capitalizastion_helper.tsv"

helper = pd.read_csv(helper_file, sep="\t")
# helper = helper[0:2]
old_col_names = helper[0:1].values[0]
new_col_names = helper[1:2].values[0]

old_frame = pd.read_csv(old_file, sep="\t", skiprows=1)

old_col_count = len(old_frame.columns)

new_orientation = old_frame[old_col_names]

new_col_count = len(new_orientation.columns)

new_orientation.columns = new_col_names
new_orientation.to_csv(with_path, sep="\t", index=False)
