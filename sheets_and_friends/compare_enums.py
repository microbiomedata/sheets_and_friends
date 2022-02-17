import logging
from typing import Optional, Dict, List  # Any

import click
import click_log
from linkml_runtime.linkml_model import (
    SchemaDefinition
)  # ClassDefinition
from linkml_runtime.utils.schemaview import SchemaView

import re

# import pandas as pd

# from linkml_runtime.dumpers import yaml_dumper
import pprint

logger = logging.getLogger(__name__)
click_log.basic_config(logger)


@click.command()
@click_log.simple_verbosity_option(logger)
@click.option("--left_model", type=click.Path(exists=True), required=True)
@click.option("--right_model", type=click.Path(exists=True), required=True)
@click.option("--enum_name")
@click.option("--yaml_output", type=click.Path(), required=True)
def compare_enums(left_model: str, right_model: str, enum_name: str, yaml_output: str):
    """
    Gets slots, listed in config_tsv, from source_model and puts them in recipient_model
    :param left_model:
    :param right_model:
    :param yaml_output:
    :param enum_name:
    :return:
    """

    # todo help for each option
    # todo docstring

    comparison = [left_model, right_model]

    enum_comparison = EnumComparison()
    for i in comparison:
        basename = get_schema_basename(i)
        enum_comparison.add_view(basename, i)
        enum_comparison.get_enum_names(basename)
        enum_comparison.add_comparee(basename)

    enum_comparison.compare_enums()


if __name__ == '__main__':
    compare_enums()


def get_schema_basename(schema_path):
    schema_basename = re.sub(r'^.*/', '', schema_path)
    schema_basename = re.sub(r'\.yaml$', '', schema_basename)
    return schema_basename


class EnumComparison:
    def __init__(self):
        self.comparison_list: List[str] = []
        self.view_dict: Optional[Dict[str, SchemaView]] = {}
        self.enum_names_dict: Optional[Dict[str, List[str]]] = {}

    def add_comparee(self, comparee):
        self.comparison_list.append(comparee)

    def add_view(self, position, schema_file):
        self.view_dict[position] = SchemaView(schema_file)

    def get_enum_names(self, position):
        positions_enums = self.view_dict[position].all_enums()
        pe_names = [v.name for k, v in positions_enums.items()]
        pe_names.sort()
        self.enum_names_dict[position] = pe_names

    def compare_enums(self):
        left_enum_names = set(self.enum_names_dict[self.comparison_list[0]])
        right_enum_names = set(self.enum_names_dict[self.comparison_list[1]])
        intersection = list(left_enum_names.intersection(right_enum_names))
        intersection.sort()
        enum_comparisons = {}
        enum_comparisons['disjoint_enums'] = {}
        enum_comparisons['disjoint_enums'][self.comparison_list[0]] = list(left_enum_names - right_enum_names)
        enum_comparisons['disjoint_enums'][self.comparison_list[0]].sort()
        enum_comparisons['disjoint_enums'][self.comparison_list[1]] = list(right_enum_names - left_enum_names)
        enum_comparisons['disjoint_enums'][self.comparison_list[1]].sort()
        enum_comparisons['shared_enums'] = {}
        for i in intersection:
            enum_comparisons['shared_enums'][i] = {"key": "value"}
        logger.info(pprint.pformat(enum_comparisons))

        # self.comp_res_dict['intersection'] = intersection
        # for i in self.comparison_list:
        #     self.comp_res_dict[f"{i} only"] = intersection
        # self.comp_res_dict['intersection'] = intersection
