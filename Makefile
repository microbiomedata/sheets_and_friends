nmdc_schemasheet_key = 1RACmVPhqpfm2ELm152CzmiEy2sDmULmbN9G0qXK8NDs
credentials_file = local/nmdc-dh-sheets-0b754bedc29d.json

.PHONY: all clean cogs_fetch mod_by_path temp

all: artifacts/soil_emls_jgi_mg_new.yaml

.cogs:
	poetry run cogs connect -k $(nmdc_schemasheet_key) -c $(credentials_file)

clean:
	rm -rf artifacts/*yaml
	rm -rf target/*log

squeaky_clean: clean
	rm -rf .cogs

# requires fetch step for satisfying dependencies?
.cogs/tracked/%: .cogs
	poetry run cogs add $(subst .tsv,,$(subst .cogs/tracked/,,$@))
	poetry run cogs fetch

cogs_fetch: .cogs
	poetry run cogs fetch

artifacts/soil_emls_jgi_mg_new.yaml: .cogs/tracked/cornerstone.tsv .cogs/tracked/new_terms.tsv .cogs/tracked/sections.tsv .cogs/tracked/enums.tsv
	poetry run cogs fetch
	poetry run sheets2linkml -o $@ $^ 2>> target/sheets2linkml.log

artifacts/soil_emls_jgi_mg_new_shuttled.yaml: .cogs/tracked/imports_regardless.tsv artifacts/soil_emls_jgi_mg_new.yaml
	poetry run do_shuttle --config_tsv $< --yaml_output $@ --recipient_model $(word 2,$^) 2>> target/do_shuttle.log

# clean? cogs_fetch?
artifacts/soil_emls_jgi_mg_new_shuttled_modified.yaml: .cogs/tracked/modifications_long.tsv artifacts/soil_emls_jgi_mg_new_shuttled.yaml
	poetry run mod_by_path \
		--config_tsv $< \
		--yaml_input $(word 2,$^) \
		--yaml_output $@  2>> target/mod_by_path.log
