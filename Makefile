nmdc_schemasheet_key = 1_TSuvEUX68g_o3r1d9wvOYMMbZ3vO4eluvAd2wNJoSU # sheets-for-nmdc-submission-schema, was nmdc-dh-sheets-mam-non-anno
credentials_file = local/nmdc-dh-sheets-0b754bedc29d.json
bisample_sqlite = /Users/MAM/biosample_basex.db
mixs_schema_path = https://raw.githubusercontent.com/GenomicsStandardsConsortium/mixs/main/model/schema/mixs.yaml
RUN = poetry run

.PHONY: all clean cogs_fetch squeaky_clean oak_stuff copy-dist-to-docs prepare-dh-dist unnecessaries

all: \
clean \
artifacts/nmdc_submission_schema.yaml \
artifacts/nmdc_submission_schema_generated.yaml \
artifacts/nmdc_submission_schema.json \
ditch-unnecessaries

#copy-dist-to-docs

artifacts/nmdc_submission_schema.json: artifacts/nmdc_submission_schema.yaml
	$(RUN) gen-linkml $< --format json --materialize-patterns --materialize-attributes > $@

ditch-unnecessaries:
	rm -rf artifacts/from_sheets2linkml.yaml artifacts/nmdc_submission_schema_generated.yaml artifacts/with_shuttles.yaml

prepare-dh-dist:
	mkdir -p nmdc_dh/schemas
	$(RUN) gen-linkml artifacts/nmdc_submission_schema.yaml --format json > nmdc_dh/schemas/nmdc_submission_schema.json
	npm init data-harmonizer artifacts/nmdc_submission_schema.yaml


copy-dist-to-docs:
	cd nmdc_dh ; echo "export default { base: '/sheets_and_friends/' }" > vite.config.js ; npm run build
	cp -R nmdc_dh/dist/* docs

.cogs:
	$(RUN) cogs connect -k $(nmdc_schemasheet_key) -c $(credentials_file)

# requires fetch step for satisfying dependencies?
.cogs/tracked/%: .cogs
	$(RUN) cogs add $(subst .tsv,,$(subst .cogs/tracked/,,$@))
	$(RUN) cogs fetch
	sleep 10

cogs_fetch: .cogs
	$(RUN) cogs fetch

artifacts/from_sheets2linkml.yaml: .cogs/tracked/schema_boilerplate.tsv .cogs/tracked/dh_interfaces.tsv \
.cogs/tracked/mixins.tsv .cogs/tracked/mixin_slots.tsv .cogs/tracked/enums.tsv .cogs/tracked/sections_as_slots.tsv
	$(RUN) cogs fetch
	$(RUN) sheets2linkml -o $@ $^ 2>> logs/sheets2linkml.log

# was >>
artifacts/with_shuttles.yaml: .cogs/tracked/import_slots_regardless.tsv artifacts/from_sheets2linkml.yaml
	$(RUN) do_shuttle --config_tsv $< --yaml_output $@ --recipient_model $(word 2,$^) 2> logs/do_shuttle.log

# clean? cogs_fetch?
artifacts/nmdc_submission_schema.yaml: .cogs/tracked/modifications_long.tsv .cogs/tracked/validation_converter.tsv artifacts/with_shuttles.yaml
	$(RUN) modifications_and_validation \
		--yaml_input $(word 3,$^) \
		--modifications_config_tsv $< \
		--validation_config_tsv $(word 2,$^) \
		--yaml_output $@ 2>> logs/modifications_and_validation.log

clean:
	rm -rf artifacts/*yaml
	rm -rf artifacts/*tsv
	rm -rf artifacts/*txt
	rm -rf docs/*
	rm -rf logs/*log

squeaky_clean: clean
	rm -rf .cogs
	rm -rf bin/*
	rm -rf downloads/*

# todo these last two steps do QC
artifacts/nmdc_submission_schema_generated.yaml: artifacts/nmdc_submission_schema.yaml
	$(RUN) gen-linkml --format yaml $< > $@

# todo add enum_name when ready
artifacts/nmdc_submission_schema_vs_mixs_enums.yaml: artifacts/nmdc_submission_schema.yaml
	$(RUN) compare_enums \
		--left_model $< \
		--right_model $(mixs_schema_path) \
		--yaml_output $@

# ---

# todo undo pipe separation of packages_consensus column from envo_terms_for_mixs_env_triad tab in
#   sheets-for-nmdc-submission-schema
#   https://docs.google.com/spreadsheets/d/1cMlPKgjZh-v21aMYCm9x1TxzE5BwGQptBQcvuaYAtC8/edit#gid=993240342

 artifacts/triad_restacked.tsv: .cogs/tracked/envo_terms_for_mixs_env_triad.tsv
 	# where did I source envo_terms_for_mixs_env_triad ?
	$(RUN) python sheets_and_friends/restack.py \
		--tsv_in $< \
		--tsv_out $@ \
		--stacked_col packages_consensus \
		--sort_key slot \
		--sort_key packages_consensus \
		--sort_key label

oak_stuff:  artifacts/triad_restacked.tsv
	# todo break this up into smaller rules
	# todo better name = triad stuff?
	# allowed packages from mixs spreadsheet (or yaml?)
	curl -o artifacts/mixs6_packages_final_clean.tsv \
		-L "https://docs.google.com/spreadsheets/d/1QDeeUcDqXes69Y2RjU2aWgOpCVWo5OVsBX9MKmMqi_o/export?gid=750683809&format=tsv"
	tail -n +2 artifacts/mixs6_packages_final_clean.tsv | cut -f1 | sort | uniq > artifacts/mixs6_sheet_env_packages.txt

	# also check mixs and submission portal schemas (classes done, don't see a relevant enum ny more) or sheets?
	$(RUN) python sheets_and_friends/envs_from_schema.py > artifacts/mixs6_yaml_env_package_classes.txt

	# observed
	$(RUN) sqlite3 $(bisample_sqlite) < sql/observed_env_packages.sql >  artifacts/observed_env_packages.tsv

	# ontologically suggested ebs values
	# https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS
		# env_broad_scale
		# We recommend using subclasses of ENVO’s biome class: http://purl.obolibrary.org/obo/ENVO_00000428
#	$(RUN) runoak --help
#	$(RUN) runoak tree --help
	$(RUN) runoak \
		--input sqlite:obo:envo descendants \
		--predicates i ENVO:00000428 | runoak \
		--input sqlite:obo:envo tree \
		--gap-fill \
		--predicates i - > artifacts/suggested_broad_scales.txt

	# are there any terms whose label contains 'biome' but aren't subclasses of ENVO:00000428 ?
	$(RUN) runoak \
		--input sqlite:obo:envo descendants \
		--predicates i ENVO:00000428 | sort > artifacts/biome_subclasses.txt
	$(RUN) runoak --input sqlite:obo:envo search 't~biome' | grep -v obsolete | sort > artifacts/biome_label.txt
	- diff \
 		--new-line-format="" \
 		--unchanged-line-format="" artifacts/biome_subclasses.txt artifacts/biome_label.txt > artifacts/biome_subclasses_vs_label.txt
	- diff \
		--new-line-format="" \
		--unchanged-line-format=""  artifacts/biome_label.txt artifacts/biome_subclasses.txt > artifacts/biome_label_vs_subclasses.txt
	cat artifacts/biome_label.txt artifacts/biome_subclasses.txt | sort | uniq > artifacts/biome_label_and_subclasses.txt

	# NMDC curated suggestions for soil
	# make sure env package value are legal
	# make sure envo ids and labels match
	$(RUN) runoak \
		--input sqlite:obo:envo tree \
		--predicates i \
		--gap-fill `grep soil artifacts/triad_restacked.tsv | grep env_broad_scale | cut -f2 | tr '\n' ' '` \
		--output  artifacts/gapfilled_curated_soil_ebs_tree.txt

	# also run without gap fill to suggest additional terms
	$(RUN) runoak \
		--input sqlite:obo:envo tree \
		--predicates i \
		--no-gap-fill `grep soil artifacts/triad_restacked.tsv | grep env_broad_scale | cut -f2 | tr '\n' ' '` \
		--output  artifacts/curated_soil_ebs_tree.txt
	cat artifacts/curated_soil_ebs_tree.txt | \
	grep -v '\] \*\*' | \
	grep -v 'BFO:0000001' | \
	grep -v 'BFO:0000002' | \
	grep -v 'BFO:0000004' | \
	grep -v 'BFO:0000040' | \
	grep -v 'ENVO:00000428' | \
	grep -v 'ENVO:01000254' | \
	grep -v 'ENVO:01001110' | \
	grep -v 'RO:0002577' | \
	egrep -v 'environment$$' > artifacts/possible_additions.txt


	# observed
	# -- takes ~ 1 minute
      	#-- masks some error cases without directly solving them
      	#--   (see having statements)
      	#-- also masks large number of blank/null env_broad_scale values
	$(RUN) sqlite3 $(bisample_sqlite) < sql/selected_observed_soil_broad_scales.sql >  artifacts/selected_observed_soil_broad_scales.tsv

	# annotate the observations
	# runoak set-apikey [OPTIONS] KEYVAL
	tail -n +2 artifacts/selected_observed_soil_broad_scales.tsv | cut -f1 > artifacts/soil_broad_scales_to_annotate.txt
	$(RUN) runoak \
		--input bioportal:envo annotate \
		--text-file artifacts/soil_broad_scales_to_annotate.txt \
		--output-type csv | tee artifacts/soil_broad_scales_annotated.tsv

