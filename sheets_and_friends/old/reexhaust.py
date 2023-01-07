import pprint

from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime.linkml_model import SchemaDefinition, ClassDefinition

from sheets_and_friends.converters.sheet2linkml import Sheet2LinkML

list_of_slots = ['agrochem_addition', 'air_temp_regm', 'al_sat', 'al_sat_meth', 'alt', 'annual_precpt', 'annual_temp',
                 'biotic_regm', 'biotic_relationship', 'carb_nitro_ratio', 'chem_administration', 'climate_environment',
                 'collection_date', 'crop_rotation', 'cur_land_use', 'cur_vegetation', 'cur_vegetation_meth', 'depth',
                 'drainage_class', 'elev', 'env_broad_scale', 'env_local_scale', 'env_medium', 'experimental_factor',
                 'extreme_event', 'fao_class', 'fire', 'flooding', 'gaseous_environment', 'geo_loc_name',
                 'growth_facil', 'heavy_metals', 'heavy_metals_meth', 'horizon_meth', 'humidity_regm', 'lat_lon',
                 'light_regm', 'link_class_info', 'link_climate_info', 'local_class', 'local_class_meth',
                 'micro_biomass_meth', 'microbial_biomass', 'misc_param', 'org_matter', 'org_nitro', 'oxy_stat_samp',
                 'ph', 'ph_meth', 'phosphate', 'prev_land_use_meth', 'previous_land_use', 'profile_position',
                 'rel_to_oxygen', 'salinity', 'salinity_meth', 'samp_collec_device', 'samp_collec_method',
                 'samp_mat_process', 'samp_name', 'samp_size', 'samp_store_temp', 'season_precpt', 'season_temp',
                 'sieving', 'size_frac_low', 'size_frac_up', 'slope_aspect', 'slope_gradient', 'soil_horizon',
                 'soil_text_measure', 'soil_texture_meth', 'soil_type', 'soil_type_meth', 'source_mat_id', 'store_cond',
                 'temp', 'tillage', 'tot_carb', 'tot_nitro_cont_meth', 'tot_nitro_content', 'tot_org_c_meth',
                 'tot_org_carb', 'tot_phosp', 'water_cont_soil_meth', 'water_content', 'watering_regm']
source_alias = "mixs"
source_class = "soil MIMS"
source_schema = "../mixs-source/model/schema/mixs.yaml"

destination_schema = SchemaDefinition(name="destination_schema", id="https://example.com/destination_schema")
destination_class = ClassDefinition(name="destination_class")
destination_schema.classes['destination_class'] = destination_class

# ---

class_slot_dict = {
    "pending_ranges": set(),
    "pending_slots": set(),
    "exhausted_ranges": set(),
    "exhausted_slots": set(),
    "exhausted_enums": set(),
    "exhausted_types": set(),
}

exhausted_lite = Sheet2LinkML(path_to_yaml=source_schema)
view_helper = exhausted_lite.make_view_helper(schema_alias=source_alias, class_name=source_class)
slot_provenance = Sheet2LinkML.get_slot_provenance(slot_list=list_of_slots, helped_schema=view_helper)

# pprint.pprint(slot_provenance)

for i in slot_provenance["schema_other"]:
    class_slot_dict["pending_slots"].add(i)
for i in slot_provenance["class_induced"]:
    class_slot_dict["pending_slots"].add(i)

dependency_exhaustion = exhausted_lite.modular_exhaust_class(class_slot_dict, view_helper)

# any slots requested by list_of_slots but not present in dependency_exhaustion['exhausted_slots']
lost_slots = list(set(list_of_slots) - dependency_exhaustion['exhausted_slots'])
lost_slots.sort()
print("Lost slots: ")
pprint.pprint(lost_slots)
print("\n")

for e_name in dependency_exhaustion['exhausted_enums']:
    destination_schema.enums[e_name] = view_helper['view'].get_enum(e_name)

for c_name in dependency_exhaustion['exhausted_ranges']:
    destination_schema.classes[c_name] = view_helper['view'].get_class(c_name)

# refactor?
for t_name in dependency_exhaustion['exhausted_types']:
    destination_schema.types[t_name] = view_helper['view'].get_type(t_name)

for pk, pv in dependency_exhaustion['prefixes'].items():
    destination_schema.prefixes[pk] = pv

for sk, sv in dependency_exhaustion['subsets'].items():
    destination_schema.subsets[sk] = sv

dumped = yaml_dumper.dumps(destination_schema)

print(dumped)
