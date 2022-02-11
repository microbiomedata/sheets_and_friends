nmdc_schemasheet_key = 1RACmVPhqpfm2ELm152CzmiEy2sDmULmbN9G0qXK8NDs
credentials_file = local/felix-sheets-4d1f37aa312b.json

.cogs:
	cogs connect -k $(nmdc_schemasheet_key) -c $(credentials_file)

clean:
	rm -rf artifacts/*yaml

squeaky_clean: clean
	rm -rf .cogs

.cogs/tracked/%: .cogs
	cogs add $(subst .tsv,,$(subst .cogs/tracked/,,$@))

artifacts/soil_emls_jgi_mg_new.yaml: .cogs/tracked/cornerstone.tsv .cogs/tracked/new_terms.tsv
	cogs fetch
	poetry run sheets2linkml -o $@ .cogs/tracked/*.tsv