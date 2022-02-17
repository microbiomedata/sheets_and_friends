nmdc_schemasheet_key = 1RACmVPhqpfm2ELm152CzmiEy2sDmULmbN9G0qXK8NDs
credentials_file = local/nmdc-dh-sheets-0b754bedc29d.json

.PHONY: all clean cogs_fetch

all: clean project DataHarmonizer/template/soil_emsl_jgi_mg/data.js

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
	rm -rf target/*txt
	rm -rf target/*tsv
	rm -rf DataHarmonizer/template/soil_emsl_jgi_mg

squeaky_clean: clean
	rm -rf .cogs

project: artifacts/soil_biosample.yaml
	poetry run gen-project --exclude shacl --exclude owl --dir $@ $< 2>> target/gen-project.log

target/data.tsv: artifacts/soil_biosample.yaml .cogs/tracked/validation_converter.tsv
	poetry run linkml2dataharmonizer --model_file $< --selected_class soil_emsl_jgi_mg 2> target/linkml2dataharmonizer.log
	rm -rf artifacts/from_sheets2linkml.yaml
	rm -rf artifacts/with_shuttles.yaml

# should be programmatically getting the GOLD path terms, too
# mot to mention making their pull-downs dependent on upstream selections
# tie this in more clearly with other enums? actually we are intentionally "saving these for last"
target/%-extracted_list.txt: .cogs/tracked/envo_terms_for_mixs_env_triad.tsv
	grep $(word 2,$(subst -, ,$(subst -extracted_list.txt,,$(subst target/,,$@)))) $< | grep $(word 1,$(subst -, ,$(subst -extracted_list.txt,,$(subst target/,,$@)))) | cut -f2 > $@


# TEMPLATE THESE!
target/soil-env_broad_scale-indented.tsv: target/soil-env_broad_scale-extracted_list.txt
	poetry run hident \
		--sco_tab_file_name artifacts/envo_sco.tsv \
		--lab_tab_file_name artifacts/envo_labs.tsv \
		--curie_file_name $< \
		--pad_char _ \
		--pad_count 2 \
		--parent_term 'broad-scale environmental context' \
		--indented_tsv $@

target/soil-env_local_scale-indented.tsv: target/soil-env_local_scale-extracted_list.txt
	poetry run hident \
		--sco_tab_file_name artifacts/envo_sco.tsv \
		--lab_tab_file_name artifacts/envo_labs.tsv \
		--curie_file_name $< \
		--pad_char _ \
		--pad_count 2 \
		--parent_term 'local environmental context' \
		--indented_tsv $@

target/soil-env_medium-indented.tsv: target/soil-env_medium-extracted_list.txt
	poetry run hident \
		--sco_tab_file_name artifacts/envo_sco.tsv \
		--lab_tab_file_name artifacts/envo_labs.tsv \
		--curie_file_name $< \
		--pad_char _ \
		--pad_count 2 \
		--parent_term 'environmental medium' \
		--indented_tsv $@

target/data_promoted.tsv: target/data.tsv \
target/soil-env_broad_scale-indented.tsv \
target/soil-env_local_scale-indented.tsv \
target/soil-env_medium-indented.tsv
	poetry run promote_to_select \
		--promote 'broad-scale environmental context' \
		--promote 'local environmental context' \
		--promote 'environmental medium' \
		--data_tsv_in $< \
		--extra_row_files $(word 2,$^) \
		--extra_row_files $(word 3,$^) \
		--extra_row_files $(word 4,$^) \
		--data_tsv_out $@

# this converts data.tsv to a data harmonizer main.html + main.js etc.
DataHarmonizer/template/soil_emsl_jgi_mg/data.js: target/data_promoted.tsv
	-mkdir -p DataHarmonizer/template/soil_emsl_jgi_mg
	cp $< $(subst .js,.tsv,$@)
	cp -r artifacts/for_data_harmonizer_template/* DataHarmonizer/template/soil_emsl_jgi_mg
	cd DataHarmonizer/template/soil_emsl_jgi_mg && poetry run python ../../script/make_data.py 2> make_data.log && cd -
	cp -r DataHarmonizer/* docs

docs/template/soil_emsl_jgi_mg/data.js: DataHarmonizer/template/soil_emsl_jgi_mg/data.js
	cp -r DataHarmonizer/* docs
	rm -rf docs/images
	rm -rf docs/template/canada_covid19
	rm -rf docs/template/gisaid
	rm -rf docs/template/grdi
	rm -rf docs/template/pha4ge
	rm -rf docs/template/phac_dexa
	rm -rf docs/template/export.js
	rm -rf docs/template/reference_template.html
	rm -rf docs/template/canada_covid19




#	cp -r libraries docs
#	cp -r script docs
#	cp -r template docs
#	cp main.css main.html docs

#  stage in the docs folder which will be exposed via GH pages?
# or do we want the LinkML generated docs to go in GH pages?
#	# add, commit, push and merge main (with GH pages enabled) so that people can see the results at
#	#   https://turbomam.github.io/DataHarmonizer/main.html
#	#   go to the GH pages setup screen eg https://github.com/org/repo/settings/pages
#	#     ensure that the pages are being built from the docs folder in the master/main branch