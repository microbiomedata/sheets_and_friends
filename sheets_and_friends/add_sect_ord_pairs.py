import logging
import pprint

import click
import click_log
import glom.core as gc
import pandas as pd
import yaml
from glom import glom, assign

pd.set_option('display.max_columns', None)

logger = logging.getLogger(__name__)
click_log.basic_config(logger)


@click.command()
@click_log.simple_verbosity_option(logger)
@click.option("--yaml_input", type=click.Path(exists=True), required=True)
@click.option("--config_tsv", type=click.Path(exists=True), required=True)
@click.option("--yaml_output", type=click.Path(), required=True)
def mod_by_path(yaml_input: str, config_tsv: str, yaml_output: str):
    """
    :param yaml_input:
    :param config_tsv:
    :param yaml_output:
    :return:
    """

    with open(yaml_input, 'r') as stream:
        try:
            schema_dict = yaml.safe_load(stream)
        except yaml.YAMLError as e:
            logger.warning(e)

    mod_rule_frame = pd.read_csv(config_tsv, sep="\t")

    mod_rule_lod = mod_rule_frame.to_dict(orient='records')

    logger.info(pprint.pformat(mod_rule_lod))

    for i in mod_rule_lod:
        base_path = f"classes.{i['class']}.slot_usage.{i['slot']}"
        try:
            logger.info(f"{i['class']} {i['slot']} {i['section']} {i['column_order']}")
            slot_usage_extract = glom(schema_dict, base_path)
            # print(slot_usage_extract)
            if 'annotations' not in slot_usage_extract:
                # print(f"no annotations on {i['slot']} yet")
                slot_usage_extract['annotations'] = {}
            assign(obj=slot_usage_extract, path="annotations.dh:section_name",
                   val={'tag': 'dh:section_name', 'value': i['section']})
            assign(obj=slot_usage_extract, path="annotations.dh:column_number",
                   val={'tag': 'dh:column_number', 'value': i['column_order']})

        except gc.PathAccessError as e:
            logger.warning(e)

    with open(yaml_output, 'w') as outfile:
        yaml.dump(schema_dict, outfile, default_flow_style=False, sort_keys=False)


if __name__ == '__main__':
    mod_by_path()
