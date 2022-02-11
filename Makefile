nmdc_schemasheet_key = 1RACmVPhqpfm2ELm152CzmiEy2sDmULmbN9G0qXK8NDs
credentials_file = local/nmdc-dh-sheets-0b754bedc29d.json

.PHONY: all clean cogs_fetch do_shuttle

all: artifacts/soil_emls_jgi_mg_new.yaml

.cogs:
	poetry run cogs connect -k $(nmdc_schemasheet_key) -c $(credentials_file)

clean:
	rm -rf artifacts/*yaml
	rm -rf target/*log

squeaky_clean: clean
	rm -rf .cogs

# these are not getting triggered as dependencies
.cogs/tracked/%: .cogs
	poetry run cogs add $(subst .tsv,,$(subst .cogs/tracked/,,$@))
	poetry run cogs fetch

cogs_fetch: .cogs
	poetry run cogs fetch

artifacts/soil_emls_jgi_mg_new.yaml: .cogs/tracked/cornerstone.tsv .cogs/tracked/new_terms.tsv .cogs/tracked/sections.tsv
	poetry run cogs fetch
	poetry run sheets2linkml -o $@ $^ 2>> target/sheets2linkml.log

do_shuttle: .cogs/tracked/imports_regardless.tsv artifacts/soil_emls_jgi_mg_new.yaml
	poetry run do_shuttle --destination_model artifacts/soil_emls_jgi_mg_new.yaml --config_tsv $<