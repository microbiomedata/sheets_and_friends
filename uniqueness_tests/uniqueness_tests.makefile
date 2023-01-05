RUN=poetry run

input_files = $(wildcard test_data/in/*.tsv)
output_files = $(patsubst test_data/in/%.tsv,test_data/out/%.yaml,$(input_files))

uniqueness_tests_schema_generated.yaml: uniqueness_tests_schema.yaml
	$(RUN) gen-linkml \
		--format yaml \
		--no-materialize-attributes \
		--output $@ $<

clean:
	rm -rf uniqueness_tests_schema_generated.yaml test_data/out/* test_data/run_examples_output
	mkdir -p test_data/out
	#mkdir -p test_data/run_examples_output

test_data/out/%.yaml: uniqueness_tests_schema_generated.yaml test_data/in/%.tsv
	$(RUN) linkml-convert \
		--output $@ \
		--target-class NamedThingContainer \
		--index-slot named_things \
		--schema $^

test_data/run_examples_output: uniqueness_tests_schema_generated.yaml
	$(RUN) linkml-run-examples \
		--schema $< \
		--input-directory test_data/valids_for_run_examples \
		--counter-example-input-directory test_data/counterexamples_for_run_examples \
		--output-directory $@

all: clean uniqueness_tests_schema_generated.yaml $(output_files)
