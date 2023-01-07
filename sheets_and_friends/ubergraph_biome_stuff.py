import rdflib

from pandas import DataFrame
from rdflib.plugins.sparql.processor import SPARQLResult


def sparql_results_to_df(results: SPARQLResult) -> DataFrame:
    """
    Export results from a rdflib SPARQL query into a `pandas.DataFrame`,
    using Python types. See https://github.com/RDFLib/rdflib/issues/1179.
    """
    return DataFrame(
        data=([None if x is None else x.toPython() for x in row] for row in results),
        columns=[str(x) for x in results.vars],
    )


print("Creating empty graph...")
g = rdflib.Graph()

print("Submitting query...")
biome_res = g.query(
    """
PREFIX  ENVO: <https://purl.obolibrary.org/obo/ENVO_>
PREFIX  rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT  distinct ?s ?slab ?p ?plab ?o ?olab
WHERE
  { SERVICE <https://ubergraph.apps.renci.org/sparql>
      { {   { ?s  rdfs:subClassOf  ENVO:00000428 }
          UNION
            { ?s  rdfs:label  ?1 }
        }
        ?s  ?p          ?o ;
            rdfs:label  ?slab .
        ?p  rdfs:label  ?plab
        OPTIONAL
          { ?o  rdfs:label  ?olab }
        ?s  rdfs:isDefinedBy  <https://purl.obolibrary.org/obo/envo.owl>
        FILTER strends(?1, "biome")
      }
  }
  order by ?slab ?plab ?olab
    """
)

print("Converting results to DataFrame...")
biome_frame = sparql_results_to_df(biome_res)

print("Saving DataFrame...")

biome_frame.to_csv("../artifacts/biome_statements.tsv", sep="\t", index=False)
