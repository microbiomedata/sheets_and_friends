# sheets_and_friends
Create a LinkML model with newly minted slots (via [schemasheets](https://github.com/linkml/schemasheets)), as-is imported slots (with [SchemaView](https://linkml.io/linkml/developers/manipulating-schemas.html)), or imported but modified slots (via [glom](https://glom.readthedocs.io/en/latest/index.html)

The schemsheets content comes from [nmdc-dh-sheets](https://docs.google.com/spreadsheets/d/1RACmVPhqpfm2ELm152CzmiEy2sDmULmbN9G0qXK8NDs) (as opposed to [Soil-NMDC-Template_Compiled](docs.google.com/spreadsheets/d/1pSmxX6XGOxmoA7S7rKyj5OaEl3PmAl4jAOlROuNHrU0))

When combined with [cidgoh/DataHarmonizer's linkml-datastructure branch](https://github.com/cidgoh/DataHarmonizer/tree/linkml-datastructure), this will largely replace [microbiomedata/DataHarmonizer](https://github.com/microbiomedata/DataHarmonizer)

This will also provide better support for single LinkML files representing multiple DH iterfaces on a class-by-class basis. For example soil-emls-jgi-metagenimics vs water-jgi-metatranscriptomics.

[Available on PyPI](https://pypi.org/project/sheets-and-friends/)

## dependencies
- python 3.9
- poetry
- schemasheets and cogs (which are pulled durring `poetry install`)
- a Google Sheets server account credientials file
  - ask a friend for `nmdc-dh-sheets-0b754bedc29d.json`
  - put it in `local/`
  - update the `credentials_file` in the [Makefile](Makefile) if necessary

## setup
- [install the poetry **application**](https://python-poetry.org/docs/#installation) if necessary
- `poetry install` (for installing **dependencies**)

This repo uses [turbomam/mixs-source](https://github.com/turbomam/mixs-source) and [microbiomedata/nmdc-schema](https://github.com/microbiomedata/nmdc-schema) as [submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules)

one-time, post-cloning submodule steps:
- `git submodule init`
- `git submodule update`

_TODO: how to keep these up to date?_

## running
- `make all`
  - you should get a [`artifacts/soil_emls_jgi_mg_new.yaml`](artifacts/soil_emls_jgi_mg_new.yaml). In phase one, it just contains the EMSL and JGI terms.

## Development phases
1. define EMSL, JGI (and general biosample idnetification?) terms via schemasheets
2. import any terms from other schemas like mixs-source and nmdc-schema
3. override some imported terms with yq
