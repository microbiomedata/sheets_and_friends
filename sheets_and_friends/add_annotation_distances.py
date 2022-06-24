# import typer
#
#
# def main(name: str):
#     typer.echo(f"Hello {name}")
#
#
# if __name__ == "__main__":
#     typer.run(main)

import pandas as pd
from strsimpy import Cosine
import matplotlib.pyplot as plt

# todo read in the descendants of biome
# todo read in the counts of env_broad_scale values from the INSDC biosamples
# import click
# import click_log
#
# logger = click_log.get_logger(__name__)
pd.set_option("display.max_columns", None)

shingle_size = 3

# @click.command()
# @click_log.simple_verbosity_option(logger)
# @click.option("--input_file", type=click.Path(exists=True), required=True)
# @click.option("--output_file", type=click.Path(), required=True)
# def main(input_file: str, output_file: str):
#     """
#     Gets slots, listed in config_tsv, from source_model and puts them in recipient_model
#     :param input_file:
#     :param output_file:
#     :return:
#     """
#
#     logger.info(f"Reading in {input_file}")


annotations_frame = pd.read_csv(
    "../artifacts/soil_broad_scales_annotated.tsv", sep="\t"
)

# get cosine distance between annotations_frame["subject_label"] and annotations_frame["object_label"]

cosine_obj = Cosine(shingle_size)

annotations_frame["ss_sl_cosine_dist"] = annotations_frame.apply(
    lambda row: cosine_obj.distance(
        row["subject_source"].lower().strip(" \r\n\t"), row["subject_label"].lower().strip(" \r\n\t")
    ),
    axis=1,
)

annotations_frame["ss_ol_cosine_dist"] = annotations_frame.apply(
    lambda row: cosine_obj.distance(
        row["subject_source"].lower().strip(" \r\n\t"), row["object_label"].lower().strip(" \r\n\t")
    ),
    axis=1,
)

biomes_frame = pd.read_csv(
    "../artifacts/biome_label_and_subclasses.txt", sep=" ! ", header=None
)

biomes_frame.columns = ["object_id", "biome"]
biomes_frame["biome"] = True

annotations_frame = annotations_frame.merge(biomes_frame, how="left", on="object_id")

insdc_frame = pd.read_csv(
    "../artifacts/selected_observed_soil_broad_scales.tsv", sep="\t"
)

insdc_frame.columns = ["subject_source", "sample_count"]

annotations_frame = annotations_frame.merge(
    insdc_frame, how="left", on="subject_source"
)

annotations_frame['biome'].fillna(False, inplace=True)

annotations_frame['confidence'] = annotations_frame.apply(
    lambda row: ((1 - (row['ss_ol_cosine_dist'])) ** 1.5) * (1 - (row['ss_sl_cosine_dist'])) * (
            (int(row['biome']) * 0.1) + 0.9),
    axis=1)

annotations_frame["rank"] = annotations_frame.groupby("subject_source")["confidence"].rank("dense", ascending=False)

# for_plot = annotations_frame.loc[annotations_frame["rank"] <= 2, ["confidence", "rank"]]
#
# for_plot['rank'] = for_plot['rank'].astype(str)
#
# # print(for_plot)
#
# for_plot['confidence'].hist(by=for_plot['rank'], bins=30, range=[0, 1])
# plt.show()

annotations_frame["acceptable"] = annotations_frame["confidence"] >= 0.5

annotations_frame.sort_values(by=["acceptable", "rank", "subject_source"], ascending=[False, True, True], inplace=True)

print(annotations_frame)

annotations_frame.to_csv(
    "../artifacts/soil_broad_scales_annotated_cosine.tsv", sep="\t", index=False
)
