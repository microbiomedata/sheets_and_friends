#nmdc_schemasheet_key = 1RACmVPhqpfm2ELm152CzmiEy2sDmULmbN9G0qXK8NDs #nmdc-dh-sheets now incompatible
nmdc_schemasheet_key = 1cMlPKgjZh-v21aMYCm9x1TxzE5BwGQptBQcvuaYAtC8 # nmdc-dh-sheets-mam-non-anno... rename me!

credentials_file = local/nmdc-dh-sheets-0b754bedc29d.json

desired_interface = soil_emsl_jgi_mg

.PHONY: all clean cogs_fetch add_sect_ord_pairs

all: clean project docs/template/nmdc/data.js artifacts/nmdc_dh_vs_mixs_enums.yaml

# https://gist.github.com/steinwaywhw/a4cd19cda655b8249d908261a62687f8
# https://stackoverflow.com/questions/10121182/multi-line-bash-commands-in-makefile
# https://stackoverflow.com/questions/1078524/how-to-specify-the-download-location-with-wget
# has bin as a dependency
bin/robot.jar:
	curl -s https://api.github.com/repos/ontodev/robot/releases/latest  | grep 'browser_download_url.*\.jar"' |  cut -d : -f 2,3 | tr -d \" | wget -O $@ -i -

# create new directory called bin if it doesn't already exist
bin:
	mkdir -p $@

downloads/envo.owl:
	# --location (-L) pursues redirects
	curl --location http://purl.obolibrary.org/obo/envo.owl -o $@

# patternize
target/envo_sco.tsv: downloads/envo.owl bin/robot.jar
	java -jar bin/robot.jar query --input $< --query sparql/sco.sparql $@

target/envo_labs.tsv: downloads/envo.owl bin/robot.jar
	java -jar bin/robot.jar query --input $< --query sparql/labels.sparql $@

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
artifacts/nmdc_dh.yaml: .cogs/tracked/modifications_long.tsv artifacts/with_shuttles.yaml
	poetry run mod_by_path \
		--config_tsv $< \
		--yaml_input $(word 2,$^) \
		--yaml_output $@  2>> logs/mod_by_path.log

clean:
	rm -rf DataHarmonizer/template/nmdc
	rm -rf artifacts/*yaml
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

squeaky_clean: clean
	rm -rf .cogs
	rm -rf bin/*
	rm -rf downloads/*

project: artifacts/nmdc_dh.yaml
	poetry run gen-project \
		--exclude shacl \
		--exclude owl \
		--exclude excel \
		--exclude java \
		--dir $@ $< 2>> logs/gen-project.log

target/data.tsv: artifacts/nmdc_dh.yaml .cogs/tracked/validation_converter.tsv
	poetry run linkml2dataharmonizer --model_file $< --selected_class $(desired_interface) 2> logs/linkml2dataharmonizer.log
	rm -rf artifacts/from_sheets2linkml.yaml
	rm -rf artifacts/with_shuttles.yaml
	rm -rf artifacts/with_sections_etc.yaml

# should be programmatically getting the GOLD path terms, too
# mot to mention making their pull-downs dependent on upstream selections
# tie this in more clearly with other enums? actually we are intentionally "saving these for last"
target/%-extracted_list.txt: .cogs/tracked/envo_terms_for_mixs_env_triad.tsv
	grep $(word 2,$(subst -, ,$(subst -extracted_list.txt,,$(subst target/,,$@)))) $< | grep $(word 1,$(subst -, ,$(subst -extracted_list.txt,,$(subst target/,,$@)))) | cut -f2 > $@


# patternize/TEMPLATE THESE!
target/soil-env_broad_scale-indented.tsv: target/soil-env_broad_scale-extracted_list.txt target/envo_sco.tsv target/envo_labs.tsv
	poetry run hident \
		--sco_tab_file_name $(word 2,$^) \
		--lab_tab_file_name $(word 3,$^) \
		--curie_file_name $< \
		--pad_char _ \
		--pad_count 2 \
		--parent_term 'broad-scale environmental context' \
		--indented_tsv $@

target/soil-env_local_scale-indented.tsv: target/soil-env_local_scale-extracted_list.txt target/envo_sco.tsv target/envo_labs.tsv
	poetry run hident \
		--sco_tab_file_name $(word 2,$^) \
		--lab_tab_file_name $(word 3,$^) \
		--curie_file_name $< \
		--pad_char _ \
		--pad_count 2 \
		--parent_term 'local environmental context' \
		--indented_tsv $@

target/soil-env_medium-indented.tsv: target/soil-env_medium-extracted_list.txt target/envo_sco.tsv target/envo_labs.tsv
	poetry run hident \
		--sco_tab_file_name $(word 2,$^) \
		--lab_tab_file_name $(word 3,$^) \
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
DataHarmonizer/template/nmdc/data.js: target/data_promoted.tsv
	-mkdir -p $(subst /data.js,,$@)
	# copy target/data_promoted.tsv to DataHarmonizer/template/nmdc/data.tsv
	# so we can generate the data.js in it's canonical place
	cp $< $(subst .js,.tsv,$@)
	# copy other files required by make_data.py
	cp -r artifacts/for_data_harmonizer_template/* $(subst /data.js,,$@)
	# generate DataHarmonizer/template/nmdc/data.js
	cd DataHarmonizer/template/nmdc && poetry run python ../../script/make_data.py 2> make_data.log && cd -

docs/template/nmdc/data.js: DataHarmonizer/template/nmdc/data.js
	# move all of the DataHarmonizer submodule into docs/, for GH pages to see
	cp -r DataHarmonizer/* docs
	# restore the DataHarmonizer submodule to "the way we found it"
	rm -rf DataHarmonizer/template/nmdc
	# move in the main.js that Brandon and Mark have modified vs https://github.com/cidgoh/DataHarmonizer/blob/master/script/main.js
	cp -r artifacts/for_data_harmonizer_scripts/* docs/script
	# move artifacts, including the example valid data file into the docs directory (monitored by GH pages)
	# cp -r artifacts docs
	# remove DH stuff that's not relevant to interacting with the NMDC interface
	rm -rf docs/README.md
	rm -rf docs/images
	rm -rf docs/requirements.txt
	rm -rf docs/script/make_data.py
	rm -rf docs/template/canada_covid19
	rm -rf docs/template/export.js
	rm -rf docs/template/gisaid
	rm -rf docs/template/grdi
	rm -rf docs/template/pha4ge
	rm -rf docs/template/phac_dexa
	rm -rf docs/template/reference_template.html
	rm -rf docs/template/nmdc/reference_template.html
	#
	# rm -rf docs/script/exampleInput docs/script/reference_template.html # how are these getting in there?


#  stage in the docs directory which will be exposed via GH pages?
# do we want the LinkML generated docs to go in GH pages?
#	# add, commit, push and merge main (with GH pages enabled) so that people can see the results at
#	#   https://turbomam.github.io/DataHarmonizer/main.html
#	#   go to the GH pages setup screen eg https://github.com/org/repo/settings/pages
#	#     ensure that the pages are being built from the docs directory in the master/main branch

# todo add enum_name when ready
artifacts/nmdc_dh_vs_mixs_enums.yaml: artifacts/nmdc_dh.yaml
	poetry run compare_enums \
		--left_model $< \
		--right_model mixs-source/model/schema/mixs.yaml \
		--yaml_output $@

target/mods_lw.tsv:
	poetry run python sheets_and_friends/mods_lw.py

target/helped_valid.tsv:
	poetry run python sheets_and_friends/column_update.py

target/recommended_slots.tsv: mixs-source/model/schema/mixs.yaml
	poetry run python sheets_and_friends/get_reccomended_slots.py \
		--yaml_input $< \
		--source_mixin 'MIMS' \
		--tsv_output $@

