# sheets_and_friends
Create a LinkML model with newly minted slots (via [schemasheets](https://github.com/linkml/schemasheets)), as-is imported slots (with [SchemaView](https://linkml.io/linkml/developers/manipulating-schemas.html)), or imported but modified slots (via [glom](https://glom.readthedocs.io/en/latest/index.html))

The schemsheets content comes from [nmdc-dh-sheets](https://docs.google.com/spreadsheets/d/1RACmVPhqpfm2ELm152CzmiEy2sDmULmbN9G0qXK8NDs) (as opposed to [Soil-NMDC-Template_Compiled](docs.google.com/spreadsheets/d/1pSmxX6XGOxmoA7S7rKyj5OaEl3PmAl4jAOlROuNHrU0)) and is intended to replace [microbiomedata/DataHarmonizer](https://github.com/microbiomedata/DataHarmonizer).

This will also provide better support for single LinkML files representing multiple DH iterfaces on a class-by-class basis. For example soil-emls-jgi-metagenimics vs water-jgi-metatranscriptomics.

Also
- provides better distinction between new terms, imports (regardless of modifications) and modifications themselves
  - new terms use [schemasheets](https://github.com/linkml/schemasheets)
- provides a direct solution for making terms in a "required" section required/yellow
- makes programmatic access to the Google Sheet easier by using [cogs](https://github.com/ontodev/cogs) 
- is smaller
- is more object oriented and hopefully follows better software engineering principles

Future:
- use [cidgoh/DataHarmonizer's linkml-datastructure branch](https://github.com/cidgoh/DataHarmonizer/tree/linkml-datastructure) instead of [sheets_and_friends/converters/linkml2dataharmonizer.py](sheets_and_friends/converters/linkml2dataharmonizer.py)
- use [structured patterns](https://github.com/linkml/linkml/issues/176) instead of a [validation_converter sheet](https://docs.google.com/spreadsheets/d/1RACmVPhqpfm2ELm152CzmiEy2sDmULmbN9G0qXK8NDs/edit#gid=928747012)

[Available on PyPI](https://pypi.org/project/sheets-and-friends/)

## dependencies
- python 3.9
- poetry
- java
  - I'm using `OpenJDK 64-Bit Server VM AdoptOpenJDK (build 14.0.2+12, mixed mode, sharing)`
- schemasheets and cogs (which are pulled during `poetry install`)
- a Google Sheets service account credentials file
  - ask a friend for `nmdc-dh-sheets-0b754bedc29d.json`
  - put it in `local/`
  - update the `credentials_file` in the [Makefile](Makefile) _if necessary_

## setup
- [install the poetry **application**](https://python-poetry.org/docs/#installation) if necessary
- `poetry install` (for installing **dependencies**)

This repo uses [cidgoh/DataHarmonizer](https://github.com/cidgoh/DataHarmonizer), [turbomam/mixs-source](https://github.com/turbomam/mixs-source) and [microbiomedata/nmdc-schema](https://github.com/microbiomedata/nmdc-schema) as [submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules)

one-time, post-cloning submodule steps:
- `git submodule init`
- `git submodule update`

_TODO: how to keep these up to date?_

## running
- `make all`
- Navigate to the `DataHarmonizer` directory and double-click on `main.html` to open it in your browser
- Add `?template=soil_emsl_jgi_mg` to the right-hand side of the address bar and hit enter
- Use File->Open in the DataHarmonizer menu to load `DataHarmonizer/template/soil_emsl_jgi_mg/exampleInput/soil_emsl_jgi_mg_export.tsv`
- Click the Validate button
- Play around with the example values and try validating again
- Double-click on a column header for information about the validation requirements
- Create an issue if something isn't behaving the way you expect
- Try the `Save as...` and `Export to...` options from the DataHarmonizer File menu. Note the differences in teh column headers.

