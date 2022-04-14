import logging
import os
from typing import List, Optional, Dict, Any, Union

import click
import click_log
import pandas as pd
from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime.utils.schemaview import SchemaView

# define type annotation for filename
FILENAME = Union[str, bytes, os.PathLike]

logger = logging.getLogger(__name__)
click_log.basic_config(logger)


@click.command()
@click_log.simple_verbosity_option(logger)
@click.option("--yaml_input", type=click.Path(exists=True), required=True)
@click.option("--config_tsv", type=click.Path(exists=True), required=True)
@click.option("--yaml_output", type=click.Path(), required=True)
def add_regex_validators(
    yaml_input: FILENAME, config_tsv: FILENAME, yaml_output: FILENAME
):
    """Apply pattern property to all LinkML slots with a string serialization.

    :param yaml_input: Input NMDC YAML without pattern property
    :param config_tsv: validation_converter sheet downloaded as TSV
    :param yaml_output: Output NMDC YAML with pattern property applied
        to slots
    """
    # fetch validation_converter sheet as pd df
    validation_rules_df = pd.read_csv(config_tsv, sep="\t", header=0)

    # load previously generated schema into SchemaView object
    nmdc_sv = SchemaView(yaml_input)

    # loop through all slots in the above schema
    # and modify slots in place
    for _, slot_defn in nmdc_sv.all_slots().items():

        # when slot range in filtered list from validation_converter
        if (
            slot_defn.range
            in validation_rules_df[
                validation_rules_df["to_type"] == "DH pattern regex"
            ]["from_val"].to_list()
        ):
            slot_defn.pattern = validation_rules_df[
                validation_rules_df["from_val"] == slot_defn.range
            ]["to_val"].to_list()[0]

        # when slot string_serialization in filtered list 
        # from validation_converter
        if (
            slot_defn.string_serialization
            in validation_rules_df[
                validation_rules_df["to_type"] == "DH pattern regex"
            ]["from_val"].to_list()
        ):
            slot_defn.pattern = validation_rules_df[
                validation_rules_df["from_val"] == slot_defn.string_serialization
            ]["to_val"].to_list()[0]

    # export new schema from modified schema, with pattern
    yaml_dumper.dump(nmdc_sv.schema, yaml_output)
    
    logger.info(f"NMDC Schema YAML outputted to: {yaml_output}")
