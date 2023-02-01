nmdc_schemasheet_key = 1PTioN6VJl52JXOpmoHFIMRS8Nf6NaC5hS5ZWn7_vkS4
credentials_file = local/nmdc-dh-sheets-0b754bedc29d.json
RUN = poetry run

.PHONY: all clean cogs_fetch squeaky_clean

all: clean artifacts/mixs_subset.yaml
	rm -rf artifacts/from_sheets2linkml.yaml
	yq -i 'del(.classes.placeholder_class)' $(word 2,$^)

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
	$(RUN) do_shuttle --config_tsv $< --yaml_output $@ --recipient_model $(word 2,$^) 2> logs/do_shuttle.log

squeaky_clean: clean
	rm -rf .cogs

clean:
	rm -rf artifacts
	rm -rf logs
	mkdir -p artifacts
	mkdir -p logs

