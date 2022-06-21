import logging
import pprint
from typing import Any, List

import click
import click_log
import pandas as pd

logger = logging.getLogger(__name__)
click_log.basic_config(logger)

pd.set_option("display.max_columns", None)

sep = "\t"


# todo
#   check for validity of slot and packages (in schema? or mixs standard?) class_curie (in ontology)
#   check for mismatches between class_curie label
#   check for dupes in ???
#   group in some other way? like package, slot (with class_curie pasted?)
#     prob not: leaving curie and label unpackd


@click.command()
@click_log.simple_verbosity_option(logger)
@click.option("--tsv_in", type=click.Path(exists=True), required=True)
@click.option("--tsv_out", type=click.Path(), required=True)
@click.option("--stacked_col", required=True)
@click.option("--sort_key", multiple=True)
def cli(tsv_in: str, tsv_out: str, stacked_col: str, sort_key: List[str]):
    """
    Gets slots, listed in config_tsv, from source_model and puts them in recipient_model
    :param tsv_in:
    :param tsv_out:
    :param stacked_col:
    :return:
    """

    stacked_frame = pd.read_csv(tsv_in, sep=sep)

    stacked_frame[stacked_col] = stacked_frame[stacked_col].str.split("|", expand=False)

    stacked_frame = stacked_frame.explode(column=stacked_col)

    allcols = list(stacked_frame.columns)

    allcols.remove(stacked_col)

    stacked_frame[stacked_col] = stacked_frame.groupby(allcols)[stacked_col].transform(
        lambda x: '|'.join(x.sort_values().unique()))

    if len(sort_key) > 0:
        stacked_frame.sort_values(by=list(sort_key), inplace=True)

        stacked_frame.drop_duplicates(inplace=True)

    stacked_frame.to_csv(tsv_out, sep=sep, index=False)


if __name__ == "__main__":
    cli()
