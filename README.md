# sheets_and_friends
Create a LinkML model with as-is imported slots, imported but modified slots (via yq), or newly minted slots (via schemasheets)

## dependencies
- python 3.9
- poetry
- schemasheets and cogs (which are pulled durring `poetry install`)
- a Google Sheets server account credientials file
  - ask a friend
  - put it in `local/`
  - update the `credentials_file` in the [Makefile](Makefile) if necessary

## setup
- install the poetry **application** if necessary
- `poetry install` (for installing **dependencies**)

## running
- `make all`
  - you should get a [`artifacts/soil_emls_jgi_mg_new.yaml`](artifacts/soil_emls_jgi_mg_new.yaml). In phase one, it just contains the EMSL and JGI terms.

## Development phases
1. define EMSL, JGI (and general biosample idnetification?) terms via schemasheets
2. import any terms from other schemas like mixs-source and nmdc-schema
3. override some imported terms with yq
