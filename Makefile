nmdc_schemasheet_key = 1PTioN6VJl52JXOpmoHFIMRS8Nf6NaC5hS5ZWn7_vkS4
credentials_file = local/nmdc-dh-sheets-0b754bedc29d.json
RUN = poetry run

.PHONY: all pre_clean post_clean cogs_fetch squeaky_clean

all: pre_clean artifacts/mixs_subset_with_classes_modified_generated.yaml post_clean

.cogs:
	$(RUN) cogs connect -k $(nmdc_schemasheet_key) -c $(credentials_file)

.cogs/tracked/%: .cogs
	$(RUN) cogs add $(subst .tsv,,$(subst .cogs/tracked/,,$@))
	$(RUN) cogs fetch
	sleep 1

cogs_fetch: .cogs
	$(RUN) cogs fetch


artifacts/from_sheets2linkml.yaml: .cogs/tracked/schema_boilerplate.tsv
	$(RUN) cogs fetch
	$(RUN) sheets2linkml -o $@ $^ 2>> logs/sheets2linkml.log

artifacts/mixs_subset.yaml: .cogs/tracked/import_slots_regardless.tsv artifacts/from_sheets2linkml.yaml
	$(RUN) do_shuttle \
		--config_tsv $< \
		--yaml_output $@ \
		--recipient_model $(word 2,$^) 2> logs/do_shuttle.log

artifacts/mixs_subset_brute_force.yaml: artifacts/mixs_subset.yaml
	rm -rf artifacts/from_sheets2linkml.yaml
	sed 's/quantity value/QuantityValue/' $< > $@
	sed -i.bak 's/range: string/range: TextValue/'  $@
	sed -i.bak 's/slot_uri: MIXS:/slot_uri: mixs:/'  $@
	yq -i '.slots.env_broad_scale.range |= "ControlledIdentifiedTermValue"'  $@
	yq -i '.slots.env_local_scale.range |= "ControlledIdentifiedTermValue"'  $@
	yq -i '.slots.env_medium.range |= "ControlledIdentifiedTermValue"'  $@
	yq -i 'del(.classes)'  $@
	yq -i 'del(.enums.[].name)' $@
	yq -i 'del(.slots.[].name)'  $@
	rm -rf  $@.bak

artifacts/mixs_subset_with_classes.yaml: artifacts/mixs_subset_brute_force.yaml
	cat $< artifacts/freestanding_classes.yaml > $@

artifacts/mixs_subset_with_classes_modified_generated.yaml: \
artifacts/mixs_subset_with_classes.yaml \
artifacts/sheets-for-nmdc-submission-schema_MLS-modifications_long.tsv \
artifacts/validation_converter.tsv
	$(RUN) modifications_and_validation \
		--yaml_input $< \
		--modifications_config_tsv $(word 2,$^) \
		--validation_config_tsv $(word 3,$^) \
		--yaml_output $@.tmp 2> logs/modifications_and_validation.log
	$(RUN) gen-linkml \
		--format yaml $@.tmp > artifacts/mixs_subset_with_classes_modified_generated.yaml
	rm -rf $@.tmp

squeaky_clean: clean
	rm -rf .cogs

pre_clean:
	rm -rf artifacts/mixs_subset.yaml
	rm -rf artifacts/mixs_subset_brute_force.yaml
	rm -rf artifacts/mixs_subset_with_classes.yaml
	rm -rf artifacts/mixs_subset_with_classes_modified.yaml
	rm -rf artifacts/mixs_subset_with_classes_modified_generated.yaml
	rm -rf logs
	mkdir -p artifacts
	mkdir -p logs

post_clean:
	rm -rf artifacts/mixs_subset.yaml
	rm -rf artifacts/mixs_subset_brute_force.yaml
	#rm -rf artifacts/mixs_subset_with_classes.yaml
	rm -rf artifacts/mixs_subset_with_classes_modified.yaml

