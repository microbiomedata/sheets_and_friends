nmdc_schemasheet_key = 1RACmVPhqpfm2ELm152CzmiEy2sDmULmbN9G0qXK8NDs
credentials_file = local/felix-sheets-4d1f37aa312b.json

artifacts/cogs_help.txt:
	cogs -h > $@

.cogs:
	cogs connect -k $(nmdc_schemasheet_key) -c $(credentials_file)

.PHONY: get_tsvs
get_tsvs:
	cogs fetch

clean:
	sleep 1

squeaky_clean: clean
	rm -rf .cogs

cornerstone:
	cogs add $@
	cogs fetch

