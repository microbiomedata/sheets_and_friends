nmdc_schemasheet_key = 1cMlPKgjZh-v21aMYCm9x1TxzE5BwGQptBQcvuaYAtC8 # sheets-for-nmdc-submission-schema, was nmdc-dh-sheets-mam-non-anno

credentials_file = local/nmdc-dh-sheets-0b754bedc29d.json

# todo: gen-linkml expects the schema to be provided as a filesystem path
#   now that the nmdc-schema submodule had been removed, people running this makefile
#   will have to provide a path to the nmdc.yaml file
#   which will provide relative paths to its imports
#   can this be solved by bundling teh YAML files in the nmdc-schema PyPI package?
nmdc_schema_filepath = /Users/MAM/Documents/gitrepos/nmdc-schema/src/schema/nmdc.yaml
#mixs_schema_filepath = /Users/MAM/Documents/gitrepos/mixs/model/schema/mixs.yaml
mixs_schema_path = https://raw.githubusercontent.com/GenomicsStandardsConsortium/mixs/main/model/schema/mixs.yaml

.PHONY: all clean cogs_fetch project squeaky_clean

all: clean artifacts/nmdc_submission_schema.yaml artifacts/nmdc_submission_schema_generated.yaml \
docs/template/nmdc_submission_schema/schema.js \
artifacts/nmdc_submission_schema_vs_mixs_enums.yaml

docs/template/nmdc_submission_schema/schema.js:
	# omitting project generation step
	# has project been silently broken for a long time?
	# should probably add a schema validation step
	# are envo and gold subsets still applied to *soil* templates?
	rm -rf DataHarmonizer/template/nmdc_submission_schema
	rm -rf DataHarmonizer/template/nmdc_dh
	mkdir -p DataHarmonizer/template/nmdc_submission_schema/source
	cp artifacts/nmdc_submission_schema.yaml DataHarmonizer/template/nmdc_submission_schema/source
	# generalize this?
	cd DataHarmonizer/template/nmdc_submission_schema ; poetry run python ../../script/linkml.py --input source/nmdc_submission_schema.yaml
	cp -r DataHarmonizer/main.html DataHarmonizer/main.js DataHarmonizer/main.css DataHarmonizer/libraries DataHarmonizer/script DataHarmonizer/template docs
	cp artifacts/for_data_harmonizer_scripts/GoldEcosystemTree.js docs/template/nmdc_submission_schema
	cp artifacts/for_data_harmonizer_scripts/ConfigureFieldSettings.js docs/template/nmdc_submission_schema

.cogs:
	poetry run cogs connect -k $(nmdc_schemasheet_key) -c $(credentials_file)

# requires fetch step for satisfying dependencies?
.cogs/tracked/%: .cogs
	poetry run cogs add $(subst .tsv,,$(subst .cogs/tracked/,,$@))
	poetry run cogs fetch
	sleep 10

cogs_fetch: .cogs
	poetry run cogs fetch

artifacts/from_sheets2linkml.yaml: .cogs/tracked/schema_boilerplate.tsv .cogs/tracked/dh_interfaces.tsv \
.cogs/tracked/mixins.tsv .cogs/tracked/mixin_slots.tsv .cogs/tracked/enums.tsv .cogs/tracked/sections_as_slots.tsv
	poetry run cogs fetch
	poetry run sheets2linkml -o $@ $^ 2>> logs/sheets2linkml.log

# was >>
artifacts/with_shuttles.yaml: .cogs/tracked/import_slots_regardless.tsv artifacts/from_sheets2linkml.yaml
	poetry run do_shuttle --config_tsv $< --yaml_output $@ --recipient_model $(word 2,$^) 2> logs/do_shuttle.log

# clean? cogs_fetch?
artifacts/nmdc_submission_schema.yaml: .cogs/tracked/modifications_long.tsv .cogs/tracked/validation_converter.tsv artifacts/with_shuttles.yaml
	poetry run modifications_and_validation \
		--yaml_input $(word 3,$^) \
		--modifications_config_tsv $< \
		--validation_config_tsv $(word 2,$^)  \
		--yaml_output $@  2>> logs/modifications_and_validation.log

clean:
	rm -rf DataHarmonizer/template/MIxS
	rm -rf DataHarmonizer/template/MIxS/schema.js
	rm -rf DataHarmonizer/template/canada_covid19
	rm -rf DataHarmonizer/template/gisaid
	rm -rf DataHarmonizer/template/grdi
	rm -rf DataHarmonizer/template/menu.js
	rm -rf DataHarmonizer/template/monkeypox
	rm -rf DataHarmonizer/template/nmdc
	rm -rf DataHarmonizer/template/nmdc_submission_schema/schema.js
	rm -rf DataHarmonizer/template/nmdc_submission_schema/source/nmdc_submission_schema.yaml
	rm -rf DataHarmonizer/template/pha4ge
	rm -rf DataHarmonizer/template/phac_dexa
	rm -rf artifacts/*yaml
	rm -rf artifacts/from_sheets2linkml.yaml artifacts/with_shuttles.yaml docs/script/linkml.py
	rm -rf docs/*
	rm -rf logs/*log
	rm -rf project/*py
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
	rm -rf target/*log
	rm -rf target/*tsv
	rm -rf target/*txt
	rm -rf target/compare_enums.yaml

squeaky_clean: clean
	rm -rf .cogs
	rm -rf bin/*
	rm -rf downloads/*

project: artifacts/nmdc_submission_schema.yaml
	poetry run gen-project \
		--exclude shacl \
		--exclude owl \
		--exclude excel \
		--exclude java \
		--dir $@ $< 2>> logs/gen-project.log

# todo these last two steps do QC
#  they require on the presence of certain files in teh local filesystem and cloud be omitted from `make all`
artifacts/nmdc_submission_schema_generated.yaml:
	poetry run gen-linkml --format yaml $(nmdc_schema_filepath) > $@

# todo add enum_name when ready
artifacts/nmdc_submission_schema_vs_mixs_enums.yaml: artifacts/nmdc_submission_schema.yaml
	poetry run compare_enums \
		--left_model $< \
		--right_model $(mixs_schema_path) \
		--yaml_output $@
