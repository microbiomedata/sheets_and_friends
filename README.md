# sheets_and_friends
Create a LinkML model with newly minted slots (via [schemasheets](https://github.com/linkml/schemasheets)), as-is imported slots (with [SchemaView](https://linkml.io/linkml/developers/manipulating-schemas.html)), or imported but modified slots (via [glom](https://glom.readthedocs.io/en/latest/index.html))

The schemsheets content comes from [nmdc-dh-sheets](https://docs.google.com/spreadsheets/d/1RACmVPhqpfm2ELm152CzmiEy2sDmULmbN9G0qXK8NDs) (as opposed to [Soil-NMDC-Template_Compiled](https://docs.google.com/spreadsheets/d/1pSmxX6XGOxmoA7S7rKyj5OaEl3PmAl4jAOlROuNHrU0)) and is intended to replace [microbiomedata/DataHarmonizer](https://github.com/microbiomedata/DataHarmonizer).

This will also provide better support for single LinkML files representing multiple DH interfaces on a class-by-class basis. For example soil-emls-jgi-metagenomics vs water-jgi-metatranscriptomics.

Also
- provides better distinction between new terms, imports (regardless of modifications) and modifications themselves
  - new terms use [schemasheets](https://github.com/linkml/schemasheets)
- provides a direct solution for making terms in a "required" section required/yellow
- makes programmatic access to the Google Sheet easier by using [cogs](https://github.com/ontodev/cogs) 
- is smaller
- is more object-oriented and hopefully follows better software engineering principles

Future:
- use [cidgoh/DataHarmonizer's linkml-datastructure branch](https://github.com/cidgoh/DataHarmonizer/tree/linkml-datastructure) instead of [sheets_and_friends/converters/linkml2dataharmonizer.py](sheets_and_friends/converters/linkml2dataharmonizer.py)
- use [structured patterns](https://github.com/linkml/linkml/issues/176) instead of a [validation_converter sheet](https://docs.google.com/spreadsheets/d/1RACmVPhqpfm2ELm152CzmiEy2sDmULmbN9G0qXK8NDs/edit#gid=928747012)

[Available on PyPI](https://pypi.org/project/sheets-and-friends/)

## dependencies
- python 3.9
- poetry
- java
  - if using robot. check makefile.
  - I'm using `OpenJDK 64-Bit Server VM AdoptOpenJDK (build 14.0.2+12, mixed mode, sharing)`
- schemasheets and cogs (which are pulled during `poetry install`)
- a Google Sheets service account credentials file
  - ask a friend for `nmdc-dh-sheets-0b754bedc29d.json`
  - put it in `local/`
  - update the `credentials_file` in the [Makefile](Makefile) _if necessary_
- npm is using the pure javascript deployment

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
- Get a valid data file to start with, either
  - https://microbiomedata.github.io/sheets_and_friends/template/soil_emsl_jgi_mg/exampleInput/soil_emsl_jgi_mg_example_data.tsv
  - `DataHarmonizer/template/soil_emsl_jgi_mg/exampleInput/soil_emsl_jgi_mg_export.tsv`
- Use File->Open in the DataHarmonizer menu to load the valid data
- Click the Validate button
- Play around with the example values and try validating again
- Double-click on a column header for information about the validation requirements
- Create an [issue](https://github.com/microbiomedata/sheets_and_friends/issues) if something isn't behaving the way you expect
- Try the `Save as...` and `Export to...` options from the DataHarmonizer File menu. Note the differences in the column headers.



## Alternative pure-Javascript build process

### Initial setup

From the root of the repo: `npm init data-harmonizer  artifacts/nmdc_submission_schema.yaml`
- What would you like your new project to be called?
- choice of name not important, but don't forget it. `nmdc_dh` suggested.
- follow the directions to select the schema classes that should be included as DH templates.

1. `cd nmdc_dh`
1. `npm run dev`
    - starts a testing web server and displays the local address that should be visited
    - vist, browse, test with some sample data, and then terminate with Control-C
1. cat or copy to `nmdc_dh/vite.config.js`: `export default { base: '/sheets_and_friends/' }`
1. `npm run build`
    - may get some warnings when minifying css
1. `rm -rf ../docs/*`
1. `cp -R dist/* ../docs`
1. git add, commit and push

