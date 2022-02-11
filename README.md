# sheets_and_friends
Create a LinkML model with newly minted slots (via [schemasheets](https://github.com/linkml/schemasheets)), as-is imported slots (with [SchemaView](https://linkml.io/linkml/developers/manipulating-schemas.html)), or imported but modified slots (via [Mike Farah's yq](https://github.com/mikefarah/yq))

The schemsheets content comes from [nmdc-dh-sheets](docs.google.com/spreadsheets/d/1RACmVPhqpfm2ELm152CzmiEy2sDmULmbN9G0qXK8NDs) (as opposed to [Soil-NMDC-Template_Compiled](docs.google.com/spreadsheets/d/1pSmxX6XGOxmoA7S7rKyj5OaEl3PmAl4jAOlROuNHrU0))

When combined with [cidgoh/DataHarmonizer's linkml-datastructure branch](https://github.com/cidgoh/DataHarmonizer/tree/linkml-datastructure), this will largely replace [microbiomedata/DataHarmonizer](https://github.com/microbiomedata/DataHarmonizer)

## dependencies
- python 3.9
- poetry
- schemasheets and cogs (which are pulled durring `poetry install`)
- a Google Sheets server account credientials file
  - ask a friend
  - put it in `local/`
  - update the `credentials_file` in the [Makefile](Makefile) if necessary

## setup
- [install the poetry **application**](https://python-poetry.org/docs/#installation) if necessary
- `poetry install` (for installing **dependencies**)

## running
- `make all`
  - you should get a [`artifacts/soil_emls_jgi_mg_new.yaml`](artifacts/soil_emls_jgi_mg_new.yaml). In phase one, it just contains the EMSL and JGI terms.

## Development phases
1. define EMSL, JGI (and general biosample idnetification?) terms via schemasheets
2. import any terms from other schemas like mixs-source and nmdc-schema
3. override some imported terms with yq
