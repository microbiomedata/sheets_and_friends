import pprint

import deepdiff
from linkml_runtime.utils.schemaview import SchemaView

import yaml

mixs_file = "../mixs-source/model/schema/mixs.yaml"
mixs_view = SchemaView(mixs_file)
mims_subclasses = mixs_view.class_descendants("MIMS")
mims_subclasses.sort()

print("mixs view created")

dh_file = "../artifacts/nmdc_dh.yaml"
dh_view = SchemaView(dh_file)
dh_interface_classes = dh_view.class_descendants("dh_interface")
dh_interface_classes.sort()

print("dh view created")

mixs_class_name = "soil MIMS"
dh_class_name = "soil_emsl_jgi_mg"

mixs_cis = mixs_view.class_induced_slots(mixs_class_name)
mixs_cis_lod = [i.__dict__ for i in mixs_cis]
mixs_cis_names = [i.name for i in mixs_cis]
mixs_cis_dict = dict(zip(mixs_cis_names, mixs_cis_lod))

print("mixs cis_dict created")

dh_cis = dh_view.class_induced_slots(dh_class_name)
dh_cis_lod = [i.__dict__ for i in dh_cis]
dh_cis_names = [i.name for i in dh_cis]
dh_cis_dict = dict(zip(dh_cis_names, dh_cis_lod))

print("dh cis_dict created")

dd = deepdiff.DeepDiff(mixs_cis_dict, dh_cis_dict)

pprint.pprint(dd, width=300)

# with open('dh_deep_diff.yaml', 'w') as outfile:
#     yaml.dump(dd.to_dict(), outfile, default_flow_style=False)

# for i in mims_subclasses:
#     print(i)
#
# # MIMS
# # agriculture MIMS
# # air MIMS
# # built environment MIMS
# # food-animal and animal feed MIMS
# # food-farm environment MIMS
# # food-food production facility MIMS
# # food-human foods MIMS
# # host-associated MIMS
# # human-associated MIMS
# # human-gut MIMS
# # human-oral MIMS
# # human-skin MIMS
# # human-vaginal MIMS
# # hydrocarbon resources-cores MIMS
# # hydrocarbon resources-fluids_swabs MIMS
# # microbial mat_biofilm MIMS
# # miscellaneous natural or artificial environment MIMS
# # plant-associated MIMS
# # sediment MIMS
# # soil MIMS
# # symbiont-associated MIMS
# # wastewater_sludge MIMS
# # water MIMS
#
# print("\n")
#
# for i in dh_interface_classes:
#     print(i)
#
# # air
# # biofilm
# # built_env
# # dh_interface
# # plant-associated
# # sediment
# # soil
# # soil_emsl
# # soil_emsl_jgi_mg
# # soil_emsl_jgi_mt
# # soil_jgi_mg
# # soil_jgi_mt
# # water
