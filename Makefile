nmdc_schemasheet_key = 1cMlPKgjZh-v21aMYCm9x1TxzE5BwGQptBQcvuaYAtC8 # sheets-for-nmdc-submission-schema, was nmdc-dh-sheets-mam-non-anno
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
	$(RUN) gen-linkml $< --format json > $@

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
	https://: