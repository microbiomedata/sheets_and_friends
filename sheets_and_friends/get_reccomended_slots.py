import logging

import click
import click_log
import pandas as pd
from linkml_runtime import SchemaView

pd.set_option('display.max_columns', None)

logger = logging.getLogger(__name__)
click_log.basic_config(logger)


# yaml_input = "../mixs-source/model/schema/mixs.yaml"
# source_class = 'soil MIMS'

# yaml_input = "../nmdc-schema/src/schema/nmdc.yaml"
# source_class = 'biosample'

def per_class_slot_recommender(source_class, source_view, yaml_input):
    # source_classes = source_view.all_classes()
    # source_class_names = list(source_classes.keys())
    # source_class_names.sort()
    # pprint.pprint(source_class_names)

    suggested_slots = source_view.class_induced_slots(source_class)

    suggested_slot_names = [i.name for i in suggested_slots]

    ss_dict = dict(zip(suggested_slot_names, suggested_slots))

    suggested_slot_names.sort()

    lod = []
    for i in suggested_slot_names:
        lod.append({'source class': source_class,
                    'source file or URL': yaml_input,
                    'slot': i,
                    'is_a parent': ss_dict[i].is_a,
                    'destination class': None, 'notes': None
                    })

    df = pd.DataFrame(lod)
    return df


def per_mixin_slot_recommender(source_mixin, source_view, yaml_input):
    frame_list = []
    class_list = source_view.class_children(source_mixin)
    class_list.sort()
    for i in class_list:
        print(i)
        df = per_class_slot_recommender(i, source_view, yaml_input)
        frame_list.append(df)
    concatenated = pd.concat(frame_list)
    return concatenated


@click.command()
@click_log.simple_verbosity_option(logger)
@click.option("--yaml_input", type=click.Path(exists=True), required=True)
@click.option("--source_class")
@click.option("--source_mixin")
@click.option("--tsv_output", type=click.Path(), required=True)
def get_mixs_recommended_slots(yaml_input: str, source_class: str, source_mixin: str, tsv_output: str):
    """
    :param yaml_input:
    :param source_class:
    :param source_mixin:
    :param tsv_output:
    :return:
    """

    source_view = SchemaView(yaml_input)

    if source_class is None and source_mixin is not None:
        concatenated = per_mixin_slot_recommender(source_mixin, source_view, yaml_input)
        concatenated.to_csv(tsv_output, sep="\t", index=False)
    elif source_mixin is None and source_class is not None:
        df = per_class_slot_recommender(source_class, source_view, yaml_input)
        df.to_csv(tsv_output, sep="\t", index=False)
    else:
        print("Must provide a class name or mixin name")


if __name__ == '__main__':
    get_mixs_recommended_slots()
