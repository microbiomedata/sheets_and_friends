from linkml_runtime import SchemaView

# mixs_file = "../mixs-source/model/schema/mixs.yaml"
# mixs_class = 'soil MIMS'

mixs_file = "../nmdc-schema/src/schema/nmdc.yaml"
mixs_class = 'biosample'

mixs_view = SchemaView(mixs_file)

# mixs_classes = mixs_view.all_classes()
# mixs_class_names = list(mixs_classes.keys())
# mixs_class_names.sort()
# pprint.pprint(mixs_class_names)

suggested_slots = mixs_view.class_induced_slots(mixs_class)

suggested_slot_names = [i.name for i in suggested_slots]

ss_dict = dict(zip(suggested_slot_names, suggested_slots))

suggested_slot_names.sort()

# pprint.pprint(suggested_slot_names)

for i in suggested_slot_names:
    print(f"{i}\t{ss_dict[i].is_a}")
