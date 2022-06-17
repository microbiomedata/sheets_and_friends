from linkml_runtime import SchemaView
import pandas as pd

# meta_view = SchemaView("https://raw.githubusercontent.com/linkml/linkml-model/main/linkml_model/model/schema/meta.yaml")
# sis = meta_view.class_induced_slots('slot_definition')
# for i in sis:
#     print(i.name)

schema_file = "../artifacts/nmdc_dh.yaml"
selected_class = "sediment"

schema_view = SchemaView(schema_file)
cis = schema_view.class_induced_slots(selected_class)

lod = []
for i in cis:
    range_obj = schema_view.get_element(i.range)
    range_type_obj = type(range_obj)
    rtc_class_name = range_type_obj.class_name
    lod.append(
        {
            "slot_name": i.name,
            "range": i.range,
            "string_serialization": i.string_serialization,
            "regex_pattern": i.pattern,
            "min": i.minimum_value,
            "max": i.maximum_value,
            "is_identifier": i.identifier,
            "range_type": rtc_class_name,
        }
    )
    # print(f"{i.name} {i.range} {i.string_serialization}")

df = pd.DataFrame(lod)
df.to_csv("target/retabulate_ranges_etc.tsv", sep="\t", index=False)
