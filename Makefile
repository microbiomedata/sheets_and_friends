nmdc_schemasheet_key = 1RACmVPhqpfm2ELm152CzmiEy2sDmULmbN9G0qXK8NDs
credentials_file = local/nmdc-dh-sheets-0b754bedc29d.json

.PHONY: all clean cogs_fetch mod_by_path temp

all: artifacts/soil_emls_jgi_mg_new.yaml

.cogs:
	poetry run cogs connect -k $(nmdc_schemasheet_key) -c $(credentials_file)

# requires fetch step for satisfying dependencies?
.cogs/tracked/%: .cogs
	poetry run cogs add $(subst .tsv,,$(subst .cogs/tracked/,,$@))
	poetry run cogs fetch

cogs_fetch: .cogs
	poetry run cogs fetch

# .cogs/tracked/sections.tsv
artifacts/from_sheets2linkml.yaml: .cogs/tracked/cornerstone.tsv .cogs/tracked/new_terms.tsv \
  .cogs/tracked/enums.tsv .cogs/tracked/sections_as_classes.tsv .cogs/tracked/placeholders_awaiting_auto_imp.tsv
	poetry run cogs fetch
	poetry run sheets2linkml -o $@ $^ 2>> target/sheets2linkml.log

artifacts/with_shuttles.yaml: .cogs/tracked/import_slots_regardless.tsv artifacts/from_sheets2linkml.yaml
	poetry run do_shuttle --config_tsv $< --yaml_output $@ --recipient_model $(word 2,$^) 2>> target/do_shuttle.log

# clean? cogs_fetch?
artifacts/soil_biosample.yaml: .cogs/tracked/modifications_long.tsv artifacts/with_shuttles.yaml
	poetry run mod_by_path \
		--config_tsv $< \
		--yaml_input $(word 2,$^) \
		--yaml_output $@  2>> target/mod_by_path.log

clean:
	rm -rf artifacts/*yaml
	rm -rf target/*log
	rm -rf project/docs/*
	rm -rf project/excel/*
	rm -rf project/graphql/*
	rm -rf project/java/*
	rm -rf project/jsonld/*
	rm -rf project/jsonschema/*
	rm -rf project/owl/*
	rm -rf project/prefixmap/*
	rm -rf project/protobuf/*
	rm -rf project/shacl/*
	rm -rf project/shex/*
	rm -rf project/sqlschema/*
	rm -rf project/*py


squeaky_clean: clean
	rm -rf .cogs

# --exclude yaml
project: clean artifacts/soil_biosample.yaml
	poetry run gen-project --exclude shacl --exclude owl --dir $@ $(word 2,$^) 2>> target/project.log

selected_class = soil_emsl_jgi_mg
target/data.tsv: artifacts/soil_biosample.yaml .cogs/tracked/validation_converter.tsv
	poetry run linkml2dataharmonizer --model_file $< --selected_class $(selected_class) 2> target/linkml_to_dh_light.log
