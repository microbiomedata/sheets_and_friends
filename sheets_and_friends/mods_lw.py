import pandas as pd

selected_class = "soil_emsl_jgi_mg"

# ---

grouping_cols = ["slot", "target"]

data_cols = ["value"]

selected_columns = grouping_cols + data_cols

mods_long = pd.read_csv(".cogs/tracked/modifications_long.tsv", sep="\t")

selected_ml = mods_long.loc[mods_long["class"].eq(selected_class), selected_columns]

grouped_multiple = selected_ml.groupby(grouping_cols).size()

grouped_multiple = grouped_multiple.reset_index()

grouped_multiple.rename(columns={0: "count"}, inplace=True)

grouped_violators = grouped_multiple.loc[grouped_multiple["count"] > 1]

exclusion_targets = list(grouped_violators["target"])

post_exclusion = selected_ml.loc[~selected_ml["target"].isin(exclusion_targets)]

cast_wide = post_exclusion.pivot(index="slot", columns="target", values="value")

cast_wide.to_csv("target/mods_lw.tsv", sep="\t")
