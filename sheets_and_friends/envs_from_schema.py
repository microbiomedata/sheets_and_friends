from linkml_runtime import SchemaView

# from linkml_runtime.dumpers import yaml_dumper

mixs_yaml_path = \
    "https://raw.githubusercontent.com/GenomicsStandardsConsortium/mixs/main/model/schema/mixs.yaml"
mixs_view = SchemaView(mixs_yaml_path)

mixs_classes = mixs_view.all_classes()
mixs_class_names = list(mixs_classes.keys())
mixs_class_names.sort()

is_as = set()
mixins = set()
for current_cn in mixs_class_names:
    # print(current_cn)
    current_class = mixs_classes[current_cn]
    # print(yaml_dumper.dumps(mixs_classes[current_cn]))
    if current_class.is_a:
        is_as.add(current_class.is_a)
    for current_mixin in current_class.mixins:
        mixins.add(current_mixin)


def list_set(current_set):
    current_list = list(current_set)
    current_list.sort()
    for i in current_list:
        print(i)
    # print('\n')


list_set(is_as)
# list_set(mixins)
