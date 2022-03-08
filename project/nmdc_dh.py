# Auto generated from nmdc_dh.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-03-08T15:18:23
# Schema: nmdc_dh
#
# id: https://example.com/nmdc_dh
# description: Schema for creating Data Harmonizer interfaces for biosamples based on MIxS and other standards
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Date, Double, String
from linkml_runtime.utils.metamodelcore import XSDDate

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
MIXS = CurieNamespace('MIXS', 'http://example.org/UNKNOWN/MIXS/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MIXS_VOCAB = CurieNamespace('mixs_vocab', 'https://genomicsstandardsconsortium.github.io/mixs/')
NMDC_DH = CurieNamespace('nmdc_dh', 'https://example.com/nmdc_dh/')
DEFAULT_ = NMDC_DH


# Types

# Class references
class SoilEmslJgiMgSourceMatId(extended_str):
    pass


class NmdcDhSection(YAMLRoot):
    """
    A section (ie group if columns) within a DataHarmonizer interface
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_DH.NmdcDhSection
    class_class_curie: ClassVar[str] = "nmdc_dh:NmdcDhSection"
    class_name: ClassVar[str] = "nmdc_dh_section"
    class_model_uri: ClassVar[URIRef] = NMDC_DH.NmdcDhSection


class NmdcDhInterface(YAMLRoot):
    """
    One DataHarmonizer interface, for the specified combination of a checklist, enviornmental_package, and various
    standards, user facilities or analysis types
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_DH.NmdcDhInterface
    class_class_curie: ClassVar[str] = "nmdc_dh:NmdcDhInterface"
    class_name: ClassVar[str] = "nmdc_dh_interface"
    class_model_uri: ClassVar[URIRef] = NMDC_DH.NmdcDhInterface


@dataclass
class SoilEmslJgiMg(NmdcDhInterface):
    """
    A nmdc_dh_section, with metadata in compliance with the MIxS MIMS standard for metagenomes, EMSL biosample
    expectations, and JGI expectations for JGI metagenomics studies
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_DH.SoilEmslJgiMg
    class_class_curie: ClassVar[str] = "nmdc_dh:SoilEmslJgiMg"
    class_name: ClassVar[str] = "soil_emsl_jgi_mg"
    class_model_uri: ClassVar[URIRef] = NMDC_DH.SoilEmslJgiMg

    project_ID: str = None
    sample_type: Union[str, "SampleTypeEnum"] = None
    sample_shipped: str = None
    EMSL_store_temp: str = None
    dna_seq_project: str = None
    dna_seq_project_name: str = None
    dna_samp_ID: str = None
    dna_sample_name: str = None
    dna_concentration: str = None
    dna_volume: str = None
    dna_container_ID: str = None
    dna_cont_type: Union[str, "DnaContTypeEnum"] = None
    dna_cont_well: str = None
    dna_sample_format: Union[str, "DnaSampleFormatEnum"] = None
    dna_dnase: Union[str, "DnaDnaseEnum"] = None
    dna_collect_site: str = None
    dna_isolate_meth: str = None
    dna_seq_project_PI: str = None
    dna_project_contact: str = None
    proposal_dna: str = None
    analysis_type: Union[Union[str, "AnalysisTypeEnum"], List[Union[str, "AnalysisTypeEnum"]]] = None
    env_package: Union[str, "EnvPackageEnum"] = None
    collection_date: Union[str, XSDDate] = None
    depth: Union[dict, "QuantityValue"] = None
    elev: Union[dict, "QuantityValue"] = None
    env_broad_scale: str = None
    env_local_scale: str = None
    env_medium: str = None
    geo_loc_name: str = None
    lat_lon: str = None
    samp_name: str = None
    technical_reps: Optional[str] = None
    replicate_number: Optional[str] = None
    dna_absorb1: Optional[str] = None
    dna_absorb2: Optional[str] = None
    dna_organisms: Optional[str] = None
    collection_time: Optional[str] = None
    collection_date_inc: Optional[str] = None
    collection_time_inc: Optional[str] = None
    start_date_inc: Optional[str] = None
    start_time_inc: Optional[str] = None
    filter_method: Optional[str] = None
    experimental_factor_other: Optional[str] = None
    non_microb_biomass: Optional[str] = None
    non_microb_biomass_method: Optional[str] = None
    microbial_biomass_C: Optional[str] = None
    micro_biomass_C_meth: Optional[str] = None
    microbial_biomass_N: Optional[str] = None
    micro_biomass_N_meth: Optional[str] = None
    org_nitro_method: Optional[str] = None
    other_treatment: Optional[str] = None
    isotope_exposure: Optional[str] = None
    sample_link: Optional[str] = None
    ecosystem: Optional[str] = None
    ecosystem_category: Optional[str] = None
    ecosystem_subtype: Optional[str] = None
    ecosystem_type: Optional[str] = None
    specific_ecosystem: Optional[str] = None
    agrochem_addition: Optional[Union[str, List[str]]] = empty_list()
    air_temp_regm: Optional[Union[str, List[str]]] = empty_list()
    al_sat: Optional[Union[dict, "QuantityValue"]] = None
    al_sat_meth: Optional[str] = None
    alt: Optional[Union[dict, "QuantityValue"]] = None
    annual_precpt: Optional[Union[dict, "QuantityValue"]] = None
    annual_temp: Optional[Union[dict, "QuantityValue"]] = None
    biotic_regm: Optional[str] = None
    biotic_relationship: Optional[Union[str, "BioticRelationshipEnum"]] = None
    carb_nitro_ratio: Optional[Union[dict, "QuantityValue"]] = None
    chem_administration: Optional[Union[str, List[str]]] = empty_list()
    climate_environment: Optional[Union[str, List[str]]] = empty_list()
    crop_rotation: Optional[str] = None
    cur_land_use: Optional[Union[str, "CurLandUseEnum"]] = None
    cur_vegetation: Optional[str] = None
    cur_vegetation_meth: Optional[str] = None
    drainage_class: Optional[Union[str, "DrainageClassEnum"]] = None
    experimental_factor: Optional[str] = None
    extreme_event: Optional[Union[str, XSDDate]] = None
    fao_class: Optional[Union[str, "FaoClassEnum"]] = None
    fire: Optional[Union[str, XSDDate]] = None
    flooding: Optional[Union[str, XSDDate]] = None
    gaseous_environment: Optional[Union[str, List[str]]] = empty_list()
    growth_facil: Optional[str] = None
    heavy_metals: Optional[Union[str, List[str]]] = empty_list()
    heavy_metals_meth: Optional[str] = None
    horizon_meth: Optional[str] = None
    humidity_regm: Optional[Union[str, List[str]]] = empty_list()
    light_regm: Optional[str] = None
    link_class_info: Optional[str] = None
    link_climate_info: Optional[str] = None
    local_class: Optional[str] = None
    local_class_meth: Optional[str] = None
    micro_biomass_meth: Optional[str] = None
    microbial_biomass: Optional[Union[dict, "QuantityValue"]] = None
    misc_param: Optional[Union[str, List[str]]] = empty_list()
    org_matter: Optional[Union[dict, "QuantityValue"]] = None
    org_nitro: Optional[Union[dict, "QuantityValue"]] = None
    oxy_stat_samp: Optional[Union[str, "OxyStatSampEnum"]] = None
    ph: Optional[float] = None
    ph_meth: Optional[str] = None
    phosphate: Optional[Union[dict, "QuantityValue"]] = None
    prev_land_use_meth: Optional[str] = None
    previous_land_use: Optional[str] = None
    profile_position: Optional[Union[str, "ProfilePositionEnum"]] = None
    rel_to_oxygen: Optional[Union[str, "RelToOxygenEnum"]] = None
    salinity: Optional[Union[dict, "QuantityValue"]] = None
    salinity_meth: Optional[str] = None
    samp_collec_device: Optional[str] = None
    samp_collec_method: Optional[str] = None
    samp_mat_process: Optional[str] = None
    samp_size: Optional[Union[dict, "QuantityValue"]] = None
    samp_store_temp: Optional[Union[dict, "QuantityValue"]] = None
    season_precpt: Optional[Union[dict, "QuantityValue"]] = None
    season_temp: Optional[Union[dict, "QuantityValue"]] = None
    sieving: Optional[str] = None
    size_frac_low: Optional[Union[dict, "QuantityValue"]] = None
    size_frac_up: Optional[Union[dict, "QuantityValue"]] = None
    slope_aspect: Optional[Union[dict, "QuantityValue"]] = None
    slope_gradient: Optional[Union[dict, "QuantityValue"]] = None
    soil_horizon: Optional[Union[str, "SoilHorizonEnum"]] = None
    soil_text_measure: Optional[Union[dict, "QuantityValue"]] = None
    soil_texture_meth: Optional[str] = None
    soil_type: Optional[str] = None
    soil_type_meth: Optional[str] = None
    source_mat_id: Optional[str] = None
    store_cond: Optional[str] = None
    temp: Optional[Union[dict, "QuantityValue"]] = None
    tillage: Optional[Union[Union[str, "TillageEnum"], List[Union[str, "TillageEnum"]]]] = empty_list()
    tot_carb: Optional[Union[dict, "QuantityValue"]] = None
    tot_nitro_cont_meth: Optional[str] = None
    tot_nitro_content: Optional[Union[dict, "QuantityValue"]] = None
    tot_org_c_meth: Optional[str] = None
    tot_org_carb: Optional[Union[dict, "QuantityValue"]] = None
    tot_phosp: Optional[Union[dict, "QuantityValue"]] = None
    water_cont_soil_meth: Optional[str] = None
    water_content: Optional[Union[dict, "QuantityValue"]] = None
    watering_regm: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.source_mat_id):
            self.MissingRequiredField("source_mat_id")
        if not isinstance(self.source_mat_id, SoilEmslJgiMgSourceMatId):
            self.source_mat_id = SoilEmslJgiMgSourceMatId(self.source_mat_id)

        if self._is_empty(self.project_ID):
            self.MissingRequiredField("project_ID")
        if not isinstance(self.project_ID, str):
            self.project_ID = str(self.project_ID)

        if self._is_empty(self.sample_type):
            self.MissingRequiredField("sample_type")
        if not isinstance(self.sample_type, SampleTypeEnum):
            self.sample_type = SampleTypeEnum(self.sample_type)

        if self._is_empty(self.sample_shipped):
            self.MissingRequiredField("sample_shipped")
        if not isinstance(self.sample_shipped, str):
            self.sample_shipped = str(self.sample_shipped)

        if self._is_empty(self.EMSL_store_temp):
            self.MissingRequiredField("EMSL_store_temp")
        if not isinstance(self.EMSL_store_temp, str):
            self.EMSL_store_temp = str(self.EMSL_store_temp)

        if self._is_empty(self.dna_seq_project):
            self.MissingRequiredField("dna_seq_project")
        if not isinstance(self.dna_seq_project, str):
            self.dna_seq_project = str(self.dna_seq_project)

        if self._is_empty(self.dna_seq_project_name):
            self.MissingRequiredField("dna_seq_project_name")
        if not isinstance(self.dna_seq_project_name, str):
            self.dna_seq_project_name = str(self.dna_seq_project_name)

        if self._is_empty(self.dna_samp_ID):
            self.MissingRequiredField("dna_samp_ID")
        if not isinstance(self.dna_samp_ID, str):
            self.dna_samp_ID = str(self.dna_samp_ID)

        if self._is_empty(self.dna_sample_name):
            self.MissingRequiredField("dna_sample_name")
        if not isinstance(self.dna_sample_name, str):
            self.dna_sample_name = str(self.dna_sample_name)

        if self._is_empty(self.dna_concentration):
            self.MissingRequiredField("dna_concentration")
        if not isinstance(self.dna_concentration, str):
            self.dna_concentration = str(self.dna_concentration)

        if self._is_empty(self.dna_volume):
            self.MissingRequiredField("dna_volume")
        if not isinstance(self.dna_volume, str):
            self.dna_volume = str(self.dna_volume)

        if self._is_empty(self.dna_container_ID):
            self.MissingRequiredField("dna_container_ID")
        if not isinstance(self.dna_container_ID, str):
            self.dna_container_ID = str(self.dna_container_ID)

        if self._is_empty(self.dna_cont_type):
            self.MissingRequiredField("dna_cont_type")
        if not isinstance(self.dna_cont_type, DnaContTypeEnum):
            self.dna_cont_type = DnaContTypeEnum(self.dna_cont_type)

        if self._is_empty(self.dna_cont_well):
            self.MissingRequiredField("dna_cont_well")
        if not isinstance(self.dna_cont_well, str):
            self.dna_cont_well = str(self.dna_cont_well)

        if self._is_empty(self.dna_sample_format):
            self.MissingRequiredField("dna_sample_format")
        if not isinstance(self.dna_sample_format, DnaSampleFormatEnum):
            self.dna_sample_format = DnaSampleFormatEnum(self.dna_sample_format)

        if self._is_empty(self.dna_dnase):
            self.MissingRequiredField("dna_dnase")
        if not isinstance(self.dna_dnase, DnaDnaseEnum):
            self.dna_dnase = DnaDnaseEnum(self.dna_dnase)

        if self._is_empty(self.dna_collect_site):
            self.MissingRequiredField("dna_collect_site")
        if not isinstance(self.dna_collect_site, str):
            self.dna_collect_site = str(self.dna_collect_site)

        if self._is_empty(self.dna_isolate_meth):
            self.MissingRequiredField("dna_isolate_meth")
        if not isinstance(self.dna_isolate_meth, str):
            self.dna_isolate_meth = str(self.dna_isolate_meth)

        if self._is_empty(self.dna_seq_project_PI):
            self.MissingRequiredField("dna_seq_project_PI")
        if not isinstance(self.dna_seq_project_PI, str):
            self.dna_seq_project_PI = str(self.dna_seq_project_PI)

        if self._is_empty(self.dna_project_contact):
            self.MissingRequiredField("dna_project_contact")
        if not isinstance(self.dna_project_contact, str):
            self.dna_project_contact = str(self.dna_project_contact)

        if self._is_empty(self.proposal_dna):
            self.MissingRequiredField("proposal_dna")
        if not isinstance(self.proposal_dna, str):
            self.proposal_dna = str(self.proposal_dna)

        if self._is_empty(self.analysis_type):
            self.MissingRequiredField("analysis_type")
        if not isinstance(self.analysis_type, list):
            self.analysis_type = [self.analysis_type] if self.analysis_type is not None else []
        self.analysis_type = [v if isinstance(v, AnalysisTypeEnum) else AnalysisTypeEnum(v) for v in self.analysis_type]

        if self._is_empty(self.env_package):
            self.MissingRequiredField("env_package")
        if not isinstance(self.env_package, EnvPackageEnum):
            self.env_package = EnvPackageEnum(self.env_package)

        if self._is_empty(self.collection_date):
            self.MissingRequiredField("collection_date")
        if not isinstance(self.collection_date, XSDDate):
            self.collection_date = XSDDate(self.collection_date)

        if self._is_empty(self.depth):
            self.MissingRequiredField("depth")
        if not isinstance(self.depth, QuantityValue):
            self.depth = QuantityValue(**as_dict(self.depth))

        if self._is_empty(self.elev):
            self.MissingRequiredField("elev")
        if not isinstance(self.elev, QuantityValue):
            self.elev = QuantityValue(**as_dict(self.elev))

        if self._is_empty(self.env_broad_scale):
            self.MissingRequiredField("env_broad_scale")
        if not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self._is_empty(self.env_local_scale):
            self.MissingRequiredField("env_local_scale")
        if not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self._is_empty(self.env_medium):
            self.MissingRequiredField("env_medium")
        if not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self._is_empty(self.geo_loc_name):
            self.MissingRequiredField("geo_loc_name")
        if not isinstance(self.geo_loc_name, str):
            self.geo_loc_name = str(self.geo_loc_name)

        if self._is_empty(self.lat_lon):
            self.MissingRequiredField("lat_lon")
        if not isinstance(self.lat_lon, str):
            self.lat_lon = str(self.lat_lon)

        if self._is_empty(self.samp_name):
            self.MissingRequiredField("samp_name")
        if not isinstance(self.samp_name, str):
            self.samp_name = str(self.samp_name)

        if self._is_empty(self.ecosystem):
            self.MissingRequiredField("ecosystem")
        if not isinstance(self.ecosystem, EcosystemEnum):
            self.ecosystem = EcosystemEnum(self.ecosystem)

        if self._is_empty(self.ecosystem_category):
            self.MissingRequiredField("ecosystem_category")
        if not isinstance(self.ecosystem_category, EcosystemCategoryEnum):
            self.ecosystem_category = EcosystemCategoryEnum(self.ecosystem_category)

        if self._is_empty(self.ecosystem_subtype):
            self.MissingRequiredField("ecosystem_subtype")
        if not isinstance(self.ecosystem_subtype, EcosystemSubtypeEnum):
            self.ecosystem_subtype = EcosystemSubtypeEnum(self.ecosystem_subtype)

        if self._is_empty(self.ecosystem_type):
            self.MissingRequiredField("ecosystem_type")
        if not isinstance(self.ecosystem_type, EcosystemTypeEnum):
            self.ecosystem_type = EcosystemTypeEnum(self.ecosystem_type)

        if self._is_empty(self.specific_ecosystem):
            self.MissingRequiredField("specific_ecosystem")
        if not isinstance(self.specific_ecosystem, SpecificEcosystemEnum):
            self.specific_ecosystem = SpecificEcosystemEnum(self.specific_ecosystem)

        if self._is_empty(self.collection_date):
            self.MissingRequiredField("collection_date")
        if not isinstance(self.collection_date, str):
            self.collection_date = str(self.collection_date)

        if self._is_empty(self.depth):
            self.MissingRequiredField("depth")
        if not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self._is_empty(self.elev):
            self.MissingRequiredField("elev")
        if not isinstance(self.elev, QuantityValue):
            self.elev = QuantityValue(**as_dict(self.elev))

        if self._is_empty(self.env_broad_scale):
            self.MissingRequiredField("env_broad_scale")
        if not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self._is_empty(self.env_local_scale):
            self.MissingRequiredField("env_local_scale")
        if not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self._is_empty(self.env_medium):
            self.MissingRequiredField("env_medium")
        if not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self._is_empty(self.geo_loc_name):
            self.MissingRequiredField("geo_loc_name")
        if not isinstance(self.geo_loc_name, str):
            self.geo_loc_name = str(self.geo_loc_name)

        if self._is_empty(self.growth_facil):
            self.MissingRequiredField("growth_facil")
        if not isinstance(self.growth_facil, GrowthFacilEnum):
            self.growth_facil = GrowthFacilEnum(self.growth_facil)

        if self._is_empty(self.lat_lon):
            self.MissingRequiredField("lat_lon")
        if not isinstance(self.lat_lon, str):
            self.lat_lon = str(self.lat_lon)

        if self._is_empty(self.samp_name):
            self.MissingRequiredField("samp_name")
        if not isinstance(self.samp_name, str):
            self.samp_name = str(self.samp_name)

        if self._is_empty(self.samp_store_temp):
            self.MissingRequiredField("samp_store_temp")
        if not isinstance(self.samp_store_temp, QuantityValue):
            self.samp_store_temp = QuantityValue(**as_dict(self.samp_store_temp))

        if self._is_empty(self.store_cond):
            self.MissingRequiredField("store_cond")
        if not isinstance(self.store_cond, StoreCondEnum):
            self.store_cond = StoreCondEnum(self.store_cond)

        if self.technical_reps is not None and not isinstance(self.technical_reps, str):
            self.technical_reps = str(self.technical_reps)

        if self.replicate_number is not None and not isinstance(self.replicate_number, str):
            self.replicate_number = str(self.replicate_number)

        if self.dna_absorb1 is not None and not isinstance(self.dna_absorb1, str):
            self.dna_absorb1 = str(self.dna_absorb1)

        if self.dna_absorb2 is not None and not isinstance(self.dna_absorb2, str):
            self.dna_absorb2 = str(self.dna_absorb2)

        if self.dna_organisms is not None and not isinstance(self.dna_organisms, str):
            self.dna_organisms = str(self.dna_organisms)

        if self.collection_time is not None and not isinstance(self.collection_time, str):
            self.collection_time = str(self.collection_time)

        if self.collection_date_inc is not None and not isinstance(self.collection_date_inc, str):
            self.collection_date_inc = str(self.collection_date_inc)

        if self.collection_time_inc is not None and not isinstance(self.collection_time_inc, str):
            self.collection_time_inc = str(self.collection_time_inc)

        if self.start_date_inc is not None and not isinstance(self.start_date_inc, str):
            self.start_date_inc = str(self.start_date_inc)

        if self.start_time_inc is not None and not isinstance(self.start_time_inc, str):
            self.start_time_inc = str(self.start_time_inc)

        if self.filter_method is not None and not isinstance(self.filter_method, str):
            self.filter_method = str(self.filter_method)

        if self.experimental_factor_other is not None and not isinstance(self.experimental_factor_other, str):
            self.experimental_factor_other = str(self.experimental_factor_other)

        if self.non_microb_biomass is not None and not isinstance(self.non_microb_biomass, str):
            self.non_microb_biomass = str(self.non_microb_biomass)

        if self.non_microb_biomass_method is not None and not isinstance(self.non_microb_biomass_method, str):
            self.non_microb_biomass_method = str(self.non_microb_biomass_method)

        if self.microbial_biomass_C is not None and not isinstance(self.microbial_biomass_C, str):
            self.microbial_biomass_C = str(self.microbial_biomass_C)

        if self.micro_biomass_C_meth is not None and not isinstance(self.micro_biomass_C_meth, str):
            self.micro_biomass_C_meth = str(self.micro_biomass_C_meth)

        if self.microbial_biomass_N is not None and not isinstance(self.microbial_biomass_N, str):
            self.microbial_biomass_N = str(self.microbial_biomass_N)

        if self.micro_biomass_N_meth is not None and not isinstance(self.micro_biomass_N_meth, str):
            self.micro_biomass_N_meth = str(self.micro_biomass_N_meth)

        if self.org_nitro_method is not None and not isinstance(self.org_nitro_method, str):
            self.org_nitro_method = str(self.org_nitro_method)

        if self.other_treatment is not None and not isinstance(self.other_treatment, str):
            self.other_treatment = str(self.other_treatment)

        if self.isotope_exposure is not None and not isinstance(self.isotope_exposure, str):
            self.isotope_exposure = str(self.isotope_exposure)

        if self.sample_link is not None and not isinstance(self.sample_link, str):
            self.sample_link = str(self.sample_link)

        if self.ecosystem is not None and not isinstance(self.ecosystem, str):
            self.ecosystem = str(self.ecosystem)

        if self.ecosystem_category is not None and not isinstance(self.ecosystem_category, str):
            self.ecosystem_category = str(self.ecosystem_category)

        if self.ecosystem_subtype is not None and not isinstance(self.ecosystem_subtype, str):
            self.ecosystem_subtype = str(self.ecosystem_subtype)

        if self.ecosystem_type is not None and not isinstance(self.ecosystem_type, str):
            self.ecosystem_type = str(self.ecosystem_type)

        if self.specific_ecosystem is not None and not isinstance(self.specific_ecosystem, str):
            self.specific_ecosystem = str(self.specific_ecosystem)

        if not isinstance(self.agrochem_addition, list):
            self.agrochem_addition = [self.agrochem_addition] if self.agrochem_addition is not None else []
        self.agrochem_addition = [v if isinstance(v, str) else str(v) for v in self.agrochem_addition]

        if not isinstance(self.air_temp_regm, list):
            self.air_temp_regm = [self.air_temp_regm] if self.air_temp_regm is not None else []
        self.air_temp_regm = [v if isinstance(v, str) else str(v) for v in self.air_temp_regm]

        if self.al_sat is not None and not isinstance(self.al_sat, QuantityValue):
            self.al_sat = QuantityValue(**as_dict(self.al_sat))

        if self.al_sat_meth is not None and not isinstance(self.al_sat_meth, str):
            self.al_sat_meth = str(self.al_sat_meth)

        if self.alt is not None and not isinstance(self.alt, QuantityValue):
            self.alt = QuantityValue(**as_dict(self.alt))

        if self.annual_precpt is not None and not isinstance(self.annual_precpt, QuantityValue):
            self.annual_precpt = QuantityValue(**as_dict(self.annual_precpt))

        if self.annual_temp is not None and not isinstance(self.annual_temp, QuantityValue):
            self.annual_temp = QuantityValue(**as_dict(self.annual_temp))

        if self.biotic_regm is not None and not isinstance(self.biotic_regm, str):
            self.biotic_regm = str(self.biotic_regm)

        if self.biotic_relationship is not None and not isinstance(self.biotic_relationship, BioticRelationshipEnum):
            self.biotic_relationship = BioticRelationshipEnum(self.biotic_relationship)

        if self.carb_nitro_ratio is not None and not isinstance(self.carb_nitro_ratio, QuantityValue):
            self.carb_nitro_ratio = QuantityValue(**as_dict(self.carb_nitro_ratio))

        if not isinstance(self.chem_administration, list):
            self.chem_administration = [self.chem_administration] if self.chem_administration is not None else []
        self.chem_administration = [v if isinstance(v, str) else str(v) for v in self.chem_administration]

        if not isinstance(self.climate_environment, list):
            self.climate_environment = [self.climate_environment] if self.climate_environment is not None else []
        self.climate_environment = [v if isinstance(v, str) else str(v) for v in self.climate_environment]

        if self.crop_rotation is not None and not isinstance(self.crop_rotation, str):
            self.crop_rotation = str(self.crop_rotation)

        if self.cur_land_use is not None and not isinstance(self.cur_land_use, CurLandUseEnum):
            self.cur_land_use = CurLandUseEnum(self.cur_land_use)

        if self.cur_vegetation is not None and not isinstance(self.cur_vegetation, str):
            self.cur_vegetation = str(self.cur_vegetation)

        if self.cur_vegetation_meth is not None and not isinstance(self.cur_vegetation_meth, str):
            self.cur_vegetation_meth = str(self.cur_vegetation_meth)

        if self.drainage_class is not None and not isinstance(self.drainage_class, DrainageClassEnum):
            self.drainage_class = DrainageClassEnum(self.drainage_class)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.extreme_event is not None and not isinstance(self.extreme_event, XSDDate):
            self.extreme_event = XSDDate(self.extreme_event)

        if self.fao_class is not None and not isinstance(self.fao_class, FaoClassEnum):
            self.fao_class = FaoClassEnum(self.fao_class)

        if self.fire is not None and not isinstance(self.fire, XSDDate):
            self.fire = XSDDate(self.fire)

        if self.flooding is not None and not isinstance(self.flooding, XSDDate):
            self.flooding = XSDDate(self.flooding)

        if not isinstance(self.gaseous_environment, list):
            self.gaseous_environment = [self.gaseous_environment] if self.gaseous_environment is not None else []
        self.gaseous_environment = [v if isinstance(v, str) else str(v) for v in self.gaseous_environment]

        if self.growth_facil is not None and not isinstance(self.growth_facil, str):
            self.growth_facil = str(self.growth_facil)

        if not isinstance(self.heavy_metals, list):
            self.heavy_metals = [self.heavy_metals] if self.heavy_metals is not None else []
        self.heavy_metals = [v if isinstance(v, str) else str(v) for v in self.heavy_metals]

        if self.heavy_metals_meth is not None and not isinstance(self.heavy_metals_meth, str):
            self.heavy_metals_meth = str(self.heavy_metals_meth)

        if self.horizon_meth is not None and not isinstance(self.horizon_meth, str):
            self.horizon_meth = str(self.horizon_meth)

        if not isinstance(self.humidity_regm, list):
            self.humidity_regm = [self.humidity_regm] if self.humidity_regm is not None else []
        self.humidity_regm = [v if isinstance(v, str) else str(v) for v in self.humidity_regm]

        if self.light_regm is not None and not isinstance(self.light_regm, str):
            self.light_regm = str(self.light_regm)

        if self.link_class_info is not None and not isinstance(self.link_class_info, str):
            self.link_class_info = str(self.link_class_info)

        if self.link_climate_info is not None and not isinstance(self.link_climate_info, str):
            self.link_climate_info = str(self.link_climate_info)

        if self.local_class is not None and not isinstance(self.local_class, str):
            self.local_class = str(self.local_class)

        if self.local_class_meth is not None and not isinstance(self.local_class_meth, str):
            self.local_class_meth = str(self.local_class_meth)

        if self.micro_biomass_meth is not None and not isinstance(self.micro_biomass_meth, str):
            self.micro_biomass_meth = str(self.micro_biomass_meth)

        if self.microbial_biomass is not None and not isinstance(self.microbial_biomass, QuantityValue):
            self.microbial_biomass = QuantityValue(**as_dict(self.microbial_biomass))

        if not isinstance(self.misc_param, list):
            self.misc_param = [self.misc_param] if self.misc_param is not None else []
        self.misc_param = [v if isinstance(v, str) else str(v) for v in self.misc_param]

        if self.org_matter is not None and not isinstance(self.org_matter, QuantityValue):
            self.org_matter = QuantityValue(**as_dict(self.org_matter))

        if self.org_nitro is not None and not isinstance(self.org_nitro, QuantityValue):
            self.org_nitro = QuantityValue(**as_dict(self.org_nitro))

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, OxyStatSampEnum):
            self.oxy_stat_samp = OxyStatSampEnum(self.oxy_stat_samp)

        if self.ph is not None and not isinstance(self.ph, float):
            self.ph = float(self.ph)

        if self.ph_meth is not None and not isinstance(self.ph_meth, str):
            self.ph_meth = str(self.ph_meth)

        if self.phosphate is not None and not isinstance(self.phosphate, QuantityValue):
            self.phosphate = QuantityValue(**as_dict(self.phosphate))

        if self.prev_land_use_meth is not None and not isinstance(self.prev_land_use_meth, str):
            self.prev_land_use_meth = str(self.prev_land_use_meth)

        if self.previous_land_use is not None and not isinstance(self.previous_land_use, str):
            self.previous_land_use = str(self.previous_land_use)

        if self.profile_position is not None and not isinstance(self.profile_position, ProfilePositionEnum):
            self.profile_position = ProfilePositionEnum(self.profile_position)

        if self.rel_to_oxygen is not None and not isinstance(self.rel_to_oxygen, RelToOxygenEnum):
            self.rel_to_oxygen = RelToOxygenEnum(self.rel_to_oxygen)

        if self.salinity is not None and not isinstance(self.salinity, QuantityValue):
            self.salinity = QuantityValue(**as_dict(self.salinity))

        if self.salinity_meth is not None and not isinstance(self.salinity_meth, str):
            self.salinity_meth = str(self.salinity_meth)

        if self.samp_collec_device is not None and not isinstance(self.samp_collec_device, str):
            self.samp_collec_device = str(self.samp_collec_device)

        if self.samp_collec_method is not None and not isinstance(self.samp_collec_method, str):
            self.samp_collec_method = str(self.samp_collec_method)

        if self.samp_mat_process is not None and not isinstance(self.samp_mat_process, str):
            self.samp_mat_process = str(self.samp_mat_process)

        if self.samp_size is not None and not isinstance(self.samp_size, QuantityValue):
            self.samp_size = QuantityValue(**as_dict(self.samp_size))

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, QuantityValue):
            self.samp_store_temp = QuantityValue(**as_dict(self.samp_store_temp))

        if self.season_precpt is not None and not isinstance(self.season_precpt, QuantityValue):
            self.season_precpt = QuantityValue(**as_dict(self.season_precpt))

        if self.season_temp is not None and not isinstance(self.season_temp, QuantityValue):
            self.season_temp = QuantityValue(**as_dict(self.season_temp))

        if self.sieving is not None and not isinstance(self.sieving, str):
            self.sieving = str(self.sieving)

        if self.size_frac_low is not None and not isinstance(self.size_frac_low, QuantityValue):
            self.size_frac_low = QuantityValue(**as_dict(self.size_frac_low))

        if self.size_frac_up is not None and not isinstance(self.size_frac_up, QuantityValue):
            self.size_frac_up = QuantityValue(**as_dict(self.size_frac_up))

        if self.slope_aspect is not None and not isinstance(self.slope_aspect, QuantityValue):
            self.slope_aspect = QuantityValue(**as_dict(self.slope_aspect))

        if self.slope_gradient is not None and not isinstance(self.slope_gradient, QuantityValue):
            self.slope_gradient = QuantityValue(**as_dict(self.slope_gradient))

        if self.soil_horizon is not None and not isinstance(self.soil_horizon, SoilHorizonEnum):
            self.soil_horizon = SoilHorizonEnum(self.soil_horizon)

        if self.soil_text_measure is not None and not isinstance(self.soil_text_measure, QuantityValue):
            self.soil_text_measure = QuantityValue(**as_dict(self.soil_text_measure))

        if self.soil_texture_meth is not None and not isinstance(self.soil_texture_meth, str):
            self.soil_texture_meth = str(self.soil_texture_meth)

        if self.soil_type is not None and not isinstance(self.soil_type, str):
            self.soil_type = str(self.soil_type)

        if self.soil_type_meth is not None and not isinstance(self.soil_type_meth, str):
            self.soil_type_meth = str(self.soil_type_meth)

        if self.source_mat_id is not None and not isinstance(self.source_mat_id, str):
            self.source_mat_id = str(self.source_mat_id)

        if self.store_cond is not None and not isinstance(self.store_cond, str):
            self.store_cond = str(self.store_cond)

        if self.temp is not None and not isinstance(self.temp, QuantityValue):
            self.temp = QuantityValue(**as_dict(self.temp))

        if not isinstance(self.tillage, list):
            self.tillage = [self.tillage] if self.tillage is not None else []
        self.tillage = [v if isinstance(v, TillageEnum) else TillageEnum(v) for v in self.tillage]

        if self.tot_carb is not None and not isinstance(self.tot_carb, QuantityValue):
            self.tot_carb = QuantityValue(**as_dict(self.tot_carb))

        if self.tot_nitro_cont_meth is not None and not isinstance(self.tot_nitro_cont_meth, str):
            self.tot_nitro_cont_meth = str(self.tot_nitro_cont_meth)

        if self.tot_nitro_content is not None and not isinstance(self.tot_nitro_content, QuantityValue):
            self.tot_nitro_content = QuantityValue(**as_dict(self.tot_nitro_content))

        if self.tot_org_c_meth is not None and not isinstance(self.tot_org_c_meth, str):
            self.tot_org_c_meth = str(self.tot_org_c_meth)

        if self.tot_org_carb is not None and not isinstance(self.tot_org_carb, QuantityValue):
            self.tot_org_carb = QuantityValue(**as_dict(self.tot_org_carb))

        if self.tot_phosp is not None and not isinstance(self.tot_phosp, QuantityValue):
            self.tot_phosp = QuantityValue(**as_dict(self.tot_phosp))

        if self.water_cont_soil_meth is not None and not isinstance(self.water_cont_soil_meth, str):
            self.water_cont_soil_meth = str(self.water_cont_soil_meth)

        if self.water_content is not None and not isinstance(self.water_content, QuantityValue):
            self.water_content = QuantityValue(**as_dict(self.water_content))

        if not isinstance(self.watering_regm, list):
            self.watering_regm = [self.watering_regm] if self.watering_regm is not None else []
        self.watering_regm = [v if isinstance(v, str) else str(v) for v in self.watering_regm]

        if not isinstance(self.agrochem_addition, list):
            self.agrochem_addition = [self.agrochem_addition] if self.agrochem_addition is not None else []
        self.agrochem_addition = [v if isinstance(v, str) else str(v) for v in self.agrochem_addition]

        if not isinstance(self.air_temp_regm, list):
            self.air_temp_regm = [self.air_temp_regm] if self.air_temp_regm is not None else []
        self.air_temp_regm = [v if isinstance(v, str) else str(v) for v in self.air_temp_regm]

        if self.al_sat is not None and not isinstance(self.al_sat, QuantityValue):
            self.al_sat = QuantityValue(**as_dict(self.al_sat))

        if self.al_sat_meth is not None and not isinstance(self.al_sat_meth, str):
            self.al_sat_meth = str(self.al_sat_meth)

        if self.alt is not None and not isinstance(self.alt, QuantityValue):
            self.alt = QuantityValue(**as_dict(self.alt))

        if self.annual_precpt is not None and not isinstance(self.annual_precpt, QuantityValue):
            self.annual_precpt = QuantityValue(**as_dict(self.annual_precpt))

        if self.annual_temp is not None and not isinstance(self.annual_temp, QuantityValue):
            self.annual_temp = QuantityValue(**as_dict(self.annual_temp))

        if self.biotic_regm is not None and not isinstance(self.biotic_regm, str):
            self.biotic_regm = str(self.biotic_regm)

        if self.biotic_relationship is not None and not isinstance(self.biotic_relationship, BioticRelationshipEnum):
            self.biotic_relationship = BioticRelationshipEnum(self.biotic_relationship)

        if self.carb_nitro_ratio is not None and not isinstance(self.carb_nitro_ratio, QuantityValue):
            self.carb_nitro_ratio = QuantityValue(**as_dict(self.carb_nitro_ratio))

        if not isinstance(self.chem_administration, list):
            self.chem_administration = [self.chem_administration] if self.chem_administration is not None else []
        self.chem_administration = [v if isinstance(v, str) else str(v) for v in self.chem_administration]

        if not isinstance(self.climate_environment, list):
            self.climate_environment = [self.climate_environment] if self.climate_environment is not None else []
        self.climate_environment = [v if isinstance(v, str) else str(v) for v in self.climate_environment]

        if self.crop_rotation is not None and not isinstance(self.crop_rotation, str):
            self.crop_rotation = str(self.crop_rotation)

        if self.cur_land_use is not None and not isinstance(self.cur_land_use, CurLandUseEnum):
            self.cur_land_use = CurLandUseEnum(self.cur_land_use)

        if self.cur_vegetation is not None and not isinstance(self.cur_vegetation, str):
            self.cur_vegetation = str(self.cur_vegetation)

        if self.cur_vegetation_meth is not None and not isinstance(self.cur_vegetation_meth, str):
            self.cur_vegetation_meth = str(self.cur_vegetation_meth)

        if self.drainage_class is not None and not isinstance(self.drainage_class, DrainageClassEnum):
            self.drainage_class = DrainageClassEnum(self.drainage_class)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.extreme_event is not None and not isinstance(self.extreme_event, XSDDate):
            self.extreme_event = XSDDate(self.extreme_event)

        if self.fao_class is not None and not isinstance(self.fao_class, FaoClassEnum):
            self.fao_class = FaoClassEnum(self.fao_class)

        if self.fire is not None and not isinstance(self.fire, XSDDate):
            self.fire = XSDDate(self.fire)

        if self.flooding is not None and not isinstance(self.flooding, XSDDate):
            self.flooding = XSDDate(self.flooding)

        if not isinstance(self.gaseous_environment, list):
            self.gaseous_environment = [self.gaseous_environment] if self.gaseous_environment is not None else []
        self.gaseous_environment = [v if isinstance(v, str) else str(v) for v in self.gaseous_environment]

        if not isinstance(self.heavy_metals, list):
            self.heavy_metals = [self.heavy_metals] if self.heavy_metals is not None else []
        self.heavy_metals = [v if isinstance(v, str) else str(v) for v in self.heavy_metals]

        if self.heavy_metals_meth is not None and not isinstance(self.heavy_metals_meth, str):
            self.heavy_metals_meth = str(self.heavy_metals_meth)

        if self.horizon_meth is not None and not isinstance(self.horizon_meth, str):
            self.horizon_meth = str(self.horizon_meth)

        if not isinstance(self.humidity_regm, list):
            self.humidity_regm = [self.humidity_regm] if self.humidity_regm is not None else []
        self.humidity_regm = [v if isinstance(v, str) else str(v) for v in self.humidity_regm]

        if self.light_regm is not None and not isinstance(self.light_regm, str):
            self.light_regm = str(self.light_regm)

        if self.link_class_info is not None and not isinstance(self.link_class_info, str):
            self.link_class_info = str(self.link_class_info)

        if self.link_climate_info is not None and not isinstance(self.link_climate_info, str):
            self.link_climate_info = str(self.link_climate_info)

        if self.local_class is not None and not isinstance(self.local_class, str):
            self.local_class = str(self.local_class)

        if self.local_class_meth is not None and not isinstance(self.local_class_meth, str):
            self.local_class_meth = str(self.local_class_meth)

        if self.micro_biomass_meth is not None and not isinstance(self.micro_biomass_meth, str):
            self.micro_biomass_meth = str(self.micro_biomass_meth)

        if self.microbial_biomass is not None and not isinstance(self.microbial_biomass, QuantityValue):
            self.microbial_biomass = QuantityValue(**as_dict(self.microbial_biomass))

        if not isinstance(self.misc_param, list):
            self.misc_param = [self.misc_param] if self.misc_param is not None else []
        self.misc_param = [v if isinstance(v, str) else str(v) for v in self.misc_param]

        if self.org_matter is not None and not isinstance(self.org_matter, QuantityValue):
            self.org_matter = QuantityValue(**as_dict(self.org_matter))

        if self.org_nitro is not None and not isinstance(self.org_nitro, QuantityValue):
            self.org_nitro = QuantityValue(**as_dict(self.org_nitro))

        if self.oxy_stat_samp is not None and not isinstance(self.oxy_stat_samp, OxyStatSampEnum):
            self.oxy_stat_samp = OxyStatSampEnum(self.oxy_stat_samp)

        if self.ph is not None and not isinstance(self.ph, str):
            self.ph = str(self.ph)

        if self.ph_meth is not None and not isinstance(self.ph_meth, str):
            self.ph_meth = str(self.ph_meth)

        if self.phosphate is not None and not isinstance(self.phosphate, QuantityValue):
            self.phosphate = QuantityValue(**as_dict(self.phosphate))

        if self.prev_land_use_meth is not None and not isinstance(self.prev_land_use_meth, str):
            self.prev_land_use_meth = str(self.prev_land_use_meth)

        if self.previous_land_use is not None and not isinstance(self.previous_land_use, str):
            self.previous_land_use = str(self.previous_land_use)

        if self.profile_position is not None and not isinstance(self.profile_position, ProfilePositionEnum):
            self.profile_position = ProfilePositionEnum(self.profile_position)

        if self.rel_to_oxygen is not None and not isinstance(self.rel_to_oxygen, RelToOxygenEnum):
            self.rel_to_oxygen = RelToOxygenEnum(self.rel_to_oxygen)

        if self.salinity is not None and not isinstance(self.salinity, QuantityValue):
            self.salinity = QuantityValue(**as_dict(self.salinity))

        if self.salinity_meth is not None and not isinstance(self.salinity_meth, str):
            self.salinity_meth = str(self.salinity_meth)

        if self.samp_collec_device is not None and not isinstance(self.samp_collec_device, str):
            self.samp_collec_device = str(self.samp_collec_device)

        if self.samp_collec_method is not None and not isinstance(self.samp_collec_method, str):
            self.samp_collec_method = str(self.samp_collec_method)

        if self.samp_mat_process is not None and not isinstance(self.samp_mat_process, str):
            self.samp_mat_process = str(self.samp_mat_process)

        if self.samp_size is not None and not isinstance(self.samp_size, str):
            self.samp_size = str(self.samp_size)

        if self.season_precpt is not None and not isinstance(self.season_precpt, QuantityValue):
            self.season_precpt = QuantityValue(**as_dict(self.season_precpt))

        if self.season_temp is not None and not isinstance(self.season_temp, QuantityValue):
            self.season_temp = QuantityValue(**as_dict(self.season_temp))

        if self.sieving is not None and not isinstance(self.sieving, str):
            self.sieving = str(self.sieving)

        if self.size_frac_low is not None and not isinstance(self.size_frac_low, QuantityValue):
            self.size_frac_low = QuantityValue(**as_dict(self.size_frac_low))

        if self.size_frac_up is not None and not isinstance(self.size_frac_up, QuantityValue):
            self.size_frac_up = QuantityValue(**as_dict(self.size_frac_up))

        if self.slope_aspect is not None and not isinstance(self.slope_aspect, QuantityValue):
            self.slope_aspect = QuantityValue(**as_dict(self.slope_aspect))

        if self.slope_gradient is not None and not isinstance(self.slope_gradient, QuantityValue):
            self.slope_gradient = QuantityValue(**as_dict(self.slope_gradient))

        if self.soil_horizon is not None and not isinstance(self.soil_horizon, SoilHorizonEnum):
            self.soil_horizon = SoilHorizonEnum(self.soil_horizon)

        if self.soil_text_measure is not None and not isinstance(self.soil_text_measure, QuantityValue):
            self.soil_text_measure = QuantityValue(**as_dict(self.soil_text_measure))

        if self.soil_texture_meth is not None and not isinstance(self.soil_texture_meth, str):
            self.soil_texture_meth = str(self.soil_texture_meth)

        if self.soil_type is not None and not isinstance(self.soil_type, str):
            self.soil_type = str(self.soil_type)

        if self.soil_type_meth is not None and not isinstance(self.soil_type_meth, str):
            self.soil_type_meth = str(self.soil_type_meth)

        if self.temp is not None and not isinstance(self.temp, QuantityValue):
            self.temp = QuantityValue(**as_dict(self.temp))

        if not isinstance(self.tillage, list):
            self.tillage = [self.tillage] if self.tillage is not None else []
        self.tillage = [v if isinstance(v, TillageEnum) else TillageEnum(v) for v in self.tillage]

        if self.tot_carb is not None and not isinstance(self.tot_carb, QuantityValue):
            self.tot_carb = QuantityValue(**as_dict(self.tot_carb))

        if self.tot_nitro_cont_meth is not None and not isinstance(self.tot_nitro_cont_meth, str):
            self.tot_nitro_cont_meth = str(self.tot_nitro_cont_meth)

        if self.tot_nitro_content is not None and not isinstance(self.tot_nitro_content, QuantityValue):
            self.tot_nitro_content = QuantityValue(**as_dict(self.tot_nitro_content))

        if self.tot_org_c_meth is not None and not isinstance(self.tot_org_c_meth, str):
            self.tot_org_c_meth = str(self.tot_org_c_meth)

        if self.tot_org_carb is not None and not isinstance(self.tot_org_carb, QuantityValue):
            self.tot_org_carb = QuantityValue(**as_dict(self.tot_org_carb))

        if self.tot_phosp is not None and not isinstance(self.tot_phosp, QuantityValue):
            self.tot_phosp = QuantityValue(**as_dict(self.tot_phosp))

        if self.water_cont_soil_meth is not None and not isinstance(self.water_cont_soil_meth, str):
            self.water_cont_soil_meth = str(self.water_cont_soil_meth)

        if self.water_content is not None and not isinstance(self.water_content, QuantityValue):
            self.water_content = QuantityValue(**as_dict(self.water_content))

        if not isinstance(self.watering_regm, list):
            self.watering_regm = [self.watering_regm] if self.watering_regm is not None else []
        self.watering_regm = [v if isinstance(v, str) else str(v) for v in self.watering_regm]

        super().__post_init__(**kwargs)


@dataclass
class SoilEmslJgiMt(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_DH.SoilEmslJgiMt
    class_class_curie: ClassVar[str] = "nmdc_dh:SoilEmslJgiMt"
    class_name: ClassVar[str] = "soil_emsl_jgi_mt"
    class_model_uri: ClassVar[URIRef] = NMDC_DH.SoilEmslJgiMt

    rna_seq_project: str = None
    rna_seq_project_name: str = None
    rna_samp_ID: str = None
    rna_sample_name: str = None
    rna_concentration: str = None
    rna_volume: str = None
    rna_container_ID: str = None
    rna_cont_type: Union[str, "RnaContTypeEnum"] = None
    rna_cont_well: str = None
    rna_sample_format: Union[str, "RnaSampleFormatEnum"] = None
    dnase_rna: Union[str, "DnaseRnaEnum"] = None
    rna_collect_site: str = None
    rna_isolate_meth: str = None
    rna_seq_project_PI: str = None
    rna_project_contact: str = None
    proposal_rna: str = None
    rna_absorb1: Optional[str] = None
    rna_absorb2: Optional[str] = None
    rna_organisms: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.rna_seq_project):
            self.MissingRequiredField("rna_seq_project")
        if not isinstance(self.rna_seq_project, str):
            self.rna_seq_project = str(self.rna_seq_project)

        if self._is_empty(self.rna_seq_project_name):
            self.MissingRequiredField("rna_seq_project_name")
        if not isinstance(self.rna_seq_project_name, str):
            self.rna_seq_project_name = str(self.rna_seq_project_name)

        if self._is_empty(self.rna_samp_ID):
            self.MissingRequiredField("rna_samp_ID")
        if not isinstance(self.rna_samp_ID, str):
            self.rna_samp_ID = str(self.rna_samp_ID)

        if self._is_empty(self.rna_sample_name):
            self.MissingRequiredField("rna_sample_name")
        if not isinstance(self.rna_sample_name, str):
            self.rna_sample_name = str(self.rna_sample_name)

        if self._is_empty(self.rna_concentration):
            self.MissingRequiredField("rna_concentration")
        if not isinstance(self.rna_concentration, str):
            self.rna_concentration = str(self.rna_concentration)

        if self._is_empty(self.rna_volume):
            self.MissingRequiredField("rna_volume")
        if not isinstance(self.rna_volume, str):
            self.rna_volume = str(self.rna_volume)

        if self._is_empty(self.rna_container_ID):
            self.MissingRequiredField("rna_container_ID")
        if not isinstance(self.rna_container_ID, str):
            self.rna_container_ID = str(self.rna_container_ID)

        if self._is_empty(self.rna_cont_type):
            self.MissingRequiredField("rna_cont_type")
        if not isinstance(self.rna_cont_type, RnaContTypeEnum):
            self.rna_cont_type = RnaContTypeEnum(self.rna_cont_type)

        if self._is_empty(self.rna_cont_well):
            self.MissingRequiredField("rna_cont_well")
        if not isinstance(self.rna_cont_well, str):
            self.rna_cont_well = str(self.rna_cont_well)

        if self._is_empty(self.rna_sample_format):
            self.MissingRequiredField("rna_sample_format")
        if not isinstance(self.rna_sample_format, RnaSampleFormatEnum):
            self.rna_sample_format = RnaSampleFormatEnum(self.rna_sample_format)

        if self._is_empty(self.dnase_rna):
            self.MissingRequiredField("dnase_rna")
        if not isinstance(self.dnase_rna, DnaseRnaEnum):
            self.dnase_rna = DnaseRnaEnum(self.dnase_rna)

        if self._is_empty(self.rna_collect_site):
            self.MissingRequiredField("rna_collect_site")
        if not isinstance(self.rna_collect_site, str):
            self.rna_collect_site = str(self.rna_collect_site)

        if self._is_empty(self.rna_isolate_meth):
            self.MissingRequiredField("rna_isolate_meth")
        if not isinstance(self.rna_isolate_meth, str):
            self.rna_isolate_meth = str(self.rna_isolate_meth)

        if self._is_empty(self.rna_seq_project_PI):
            self.MissingRequiredField("rna_seq_project_PI")
        if not isinstance(self.rna_seq_project_PI, str):
            self.rna_seq_project_PI = str(self.rna_seq_project_PI)

        if self._is_empty(self.rna_project_contact):
            self.MissingRequiredField("rna_project_contact")
        if not isinstance(self.rna_project_contact, str):
            self.rna_project_contact = str(self.rna_project_contact)

        if self._is_empty(self.proposal_rna):
            self.MissingRequiredField("proposal_rna")
        if not isinstance(self.proposal_rna, str):
            self.proposal_rna = str(self.proposal_rna)

        if self.rna_absorb1 is not None and not isinstance(self.rna_absorb1, str):
            self.rna_absorb1 = str(self.rna_absorb1)

        if self.rna_absorb2 is not None and not isinstance(self.rna_absorb2, str):
            self.rna_absorb2 = str(self.rna_absorb2)

        if self.rna_organisms is not None and not isinstance(self.rna_organisms, str):
            self.rna_organisms = str(self.rna_organisms)

        super().__post_init__(**kwargs)


class SampleID(NmdcDhSection):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_DH.SampleID
    class_class_curie: ClassVar[str] = "nmdc_dh:SampleID"
    class_name: ClassVar[str] = "Sample ID"
    class_model_uri: ClassVar[URIRef] = NMDC_DH.SampleID


class GOLDEcosystemPath(NmdcDhSection):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_DH.GOLDEcosystemPath
    class_class_curie: ClassVar[str] = "nmdc_dh:GOLDEcosystemPath"
    class_name: ClassVar[str] = "GOLD ecosystem path"
    class_model_uri: ClassVar[URIRef] = NMDC_DH.GOLDEcosystemPath


class EMSL(NmdcDhSection):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_DH.EMSL
    class_class_curie: ClassVar[str] = "nmdc_dh:EMSL"
    class_name: ClassVar[str] = "EMSL"
    class_model_uri: ClassVar[URIRef] = NMDC_DH.EMSL


class JGI-Metagenomics(NmdcDhSection):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_DH["JGI-Metagenomics"]
    class_class_curie: ClassVar[str] = "nmdc_dh:JGI-Metagenomics"
    class_name: ClassVar[str] = "JGI-Metagenomics"
    class_model_uri: ClassVar[URIRef] = NMDC_DH.JGI-Metagenomics


class JGI-Metatranscriptomics(NmdcDhSection):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_DH["JGI-Metatranscriptomics"]
    class_class_curie: ClassVar[str] = "nmdc_dh:JGI-Metatranscriptomics"
    class_name: ClassVar[str] = "JGI-Metatranscriptomics"
    class_model_uri: ClassVar[URIRef] = NMDC_DH.JGI-Metatranscriptomics


class Metadata-MIxSModifiedRequired(NmdcDhSection):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_DH["Metadata-MIxSModifiedRequired"]
    class_class_curie: ClassVar[str] = "nmdc_dh:Metadata-MIxSModifiedRequired"
    class_name: ClassVar[str] = "Metadata- MIxS Modified Required"
    class_model_uri: ClassVar[URIRef] = NMDC_DH.Metadata-MIxSModifiedRequired


class Metadata-MIxSRequired(NmdcDhSection):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_DH["Metadata-MIxSRequired"]
    class_class_curie: ClassVar[str] = "nmdc_dh:Metadata-MIxSRequired"
    class_name: ClassVar[str] = "Metadata- MIxS Required"
    class_model_uri: ClassVar[URIRef] = NMDC_DH.Metadata-MIxSRequired


class Metadata-MIxSModifiedRequiredWhereApplicable(NmdcDhSection):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_DH["Metadata-MIxSModifiedRequiredWhereApplicable"]
    class_class_curie: ClassVar[str] = "nmdc_dh:Metadata-MIxSModifiedRequiredWhereApplicable"
    class_name: ClassVar[str] = "Metadata- MIxS Modified Required Where Applicable"
    class_model_uri: ClassVar[URIRef] = NMDC_DH.Metadata-MIxSModifiedRequiredWhereApplicable


class Metadata-MIxSRequiredWhereApplicable(NmdcDhSection):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_DH["Metadata-MIxSRequiredWhereApplicable"]
    class_class_curie: ClassVar[str] = "nmdc_dh:Metadata-MIxSRequiredWhereApplicable"
    class_name: ClassVar[str] = "Metadata- MIxS Required Where Applicable"
    class_model_uri: ClassVar[URIRef] = NMDC_DH.Metadata-MIxSRequiredWhereApplicable


class Metadata-MIxSModifiedOptional(NmdcDhSection):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_DH["Metadata-MIxSModifiedOptional"]
    class_class_curie: ClassVar[str] = "nmdc_dh:Metadata-MIxSModifiedOptional"
    class_name: ClassVar[str] = "Metadata- MIxS Modified Optional"
    class_model_uri: ClassVar[URIRef] = NMDC_DH.Metadata-MIxSModifiedOptional


class Metadata-MIxSOptional(NmdcDhSection):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_DH["Metadata-MIxSOptional"]
    class_class_curie: ClassVar[str] = "nmdc_dh:Metadata-MIxSOptional"
    class_name: ClassVar[str] = "Metadata- MIxS Optional"
    class_model_uri: ClassVar[URIRef] = NMDC_DH.Metadata-MIxSOptional


@dataclass
class QuantityValue(YAMLRoot):
    """
    used to record a measurement
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_DH.QuantityValue
    class_class_curie: ClassVar[str] = "nmdc_dh:QuantityValue"
    class_name: ClassVar[str] = "quantity value"
    class_model_uri: ClassVar[URIRef] = NMDC_DH.QuantityValue

    has_unit: Optional[str] = None
    has_numeric_value: Optional[float] = None
    has_raw_value: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_unit is not None and not isinstance(self.has_unit, str):
            self.has_unit = str(self.has_unit)

        if self.has_numeric_value is not None and not isinstance(self.has_numeric_value, float):
            self.has_numeric_value = float(self.has_numeric_value)

        if self.has_raw_value is not None and not isinstance(self.has_raw_value, str):
            self.has_raw_value = str(self.has_raw_value)

        super().__post_init__(**kwargs)


@dataclass
class PlaceholderClass(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC_DH.PlaceholderClass
    class_class_curie: ClassVar[str] = "nmdc_dh:PlaceholderClass"
    class_name: ClassVar[str] = "placeholder_class"
    class_model_uri: ClassVar[URIRef] = NMDC_DH.PlaceholderClass

    investigation_field: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.investigation_field is not None and not isinstance(self.investigation_field, str):
            self.investigation_field = str(self.investigation_field)

        super().__post_init__(**kwargs)


# Enumerations
class AnalysisTypeEnum(EnumDefinitionImpl):

    metabolomics = PermissibleValue(text="metabolomics")
    metagenomics = PermissibleValue(text="metagenomics")
    metaproteomics = PermissibleValue(text="metaproteomics")
    metatranscriptomics = PermissibleValue(text="metatranscriptomics")

    _defn = EnumDefinition(
        name="AnalysisTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "natural organic matter",
                PermissibleValue(text="natural organic matter") )

class BioticRelationshipEnum(EnumDefinitionImpl):

    commensalism = PermissibleValue(text="commensalism")
    mutualism = PermissibleValue(text="mutualism")
    parasitism = PermissibleValue(text="parasitism")
    symbiotic = PermissibleValue(text="symbiotic")

    _defn = EnumDefinition(
        name="BioticRelationshipEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "free living",
                PermissibleValue(text="free living") )

class DnaContTypeEnum(EnumDefinitionImpl):

    plate = PermissibleValue(text="plate")
    tube = PermissibleValue(text="tube")

    _defn = EnumDefinition(
        name="DnaContTypeEnum",
    )

class DnaDnaseEnum(EnumDefinitionImpl):

    no = PermissibleValue(text="no")
    yes = PermissibleValue(text="yes")

    _defn = EnumDefinition(
        name="DnaDnaseEnum",
    )

class DnaSampleFormatEnum(EnumDefinitionImpl):

    DNAStable = PermissibleValue(text="DNAStable")
    Ethanol = PermissibleValue(text="Ethanol")
    PBS = PermissibleValue(text="PBS")
    Pellet = PermissibleValue(text="Pellet")
    RNAStable = PermissibleValue(text="RNAStable")
    TE = PermissibleValue(text="TE")
    Water = PermissibleValue(text="Water")

    _defn = EnumDefinition(
        name="DnaSampleFormatEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "10 mM Tris-HCl",
                PermissibleValue(text="10 mM Tris-HCl") )
        setattr(cls, "Low EDTA TE",
                PermissibleValue(text="Low EDTA TE") )
        setattr(cls, "MDA reaction buffer",
                PermissibleValue(text="MDA reaction buffer") )

class DnaseRnaEnum(EnumDefinitionImpl):

    no = PermissibleValue(text="no")
    yes = PermissibleValue(text="yes")

    _defn = EnumDefinition(
        name="DnaseRnaEnum",
    )

class EcosystemCategoryEnum(EnumDefinitionImpl):

    Terrestrial = PermissibleValue(text="Terrestrial")

    _defn = EnumDefinition(
        name="EcosystemCategoryEnum",
    )

class EcosystemEnum(EnumDefinitionImpl):

    Environmental = PermissibleValue(text="Environmental")

    _defn = EnumDefinition(
        name="EcosystemEnum",
    )

class EcosystemSubtypeEnum(EnumDefinitionImpl):

    Biocrust = PermissibleValue(text="Biocrust")
    Biofilm = PermissibleValue(text="Biofilm")
    Clay = PermissibleValue(text="Clay")
    Floodplain = PermissibleValue(text="Floodplain")
    Fossil = PermissibleValue(text="Fossil")
    Glacier = PermissibleValue(text="Glacier")
    Loam = PermissibleValue(text="Loam")
    Pasture = PermissibleValue(text="Pasture")
    Peat = PermissibleValue(text="Peat")
    Ranch = PermissibleValue(text="Ranch")
    Sand = PermissibleValue(text="Sand")
    Silt = PermissibleValue(text="Silt")
    Unclassified = PermissibleValue(text="Unclassified")
    Watershed = PermissibleValue(text="Watershed")
    Wetlands = PermissibleValue(text="Wetlands")

    _defn = EnumDefinition(
        name="EcosystemSubtypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Bulk soil",
                PermissibleValue(text="Bulk soil") )
        setattr(cls, "Mineral horizon",
                PermissibleValue(text="Mineral horizon") )
        setattr(cls, "Nature reserve",
                PermissibleValue(text="Nature reserve") )
        setattr(cls, "Organic layer",
                PermissibleValue(text="Organic layer") )
        setattr(cls, "Paddy field/soil",
                PermissibleValue(text="Paddy field/soil") )
        setattr(cls, "Soil crust",
                PermissibleValue(text="Soil crust") )

class EcosystemTypeEnum(EnumDefinitionImpl):

    Soil = PermissibleValue(text="Soil")

    _defn = EnumDefinition(
        name="EcosystemTypeEnum",
    )

class EnvPackageEnum(EnumDefinitionImpl):

    soil = PermissibleValue(text="soil")

    _defn = EnumDefinition(
        name="EnvPackageEnum",
    )

class GrowthFacilEnum(EnumDefinitionImpl):

    experimental_garden = PermissibleValue(text="experimental_garden")
    field = PermissibleValue(text="field")
    field_incubation = PermissibleValue(text="field_incubation")
    glasshouse = PermissibleValue(text="glasshouse")
    greenhouse = PermissibleValue(text="greenhouse")
    growth_chamber = PermissibleValue(text="growth_chamber")
    lab_incubation = PermissibleValue(text="lab_incubation")
    open_top_chamber = PermissibleValue(text="open_top_chamber")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="GrowthFacilEnum",
    )

class RelToOxygenEnum(EnumDefinitionImpl):

    aerobe = PermissibleValue(text="aerobe")
    anaerobe = PermissibleValue(text="anaerobe")
    facultative = PermissibleValue(text="facultative")
    microaerophilic = PermissibleValue(text="microaerophilic")
    microanaerobe = PermissibleValue(text="microanaerobe")

    _defn = EnumDefinition(
        name="RelToOxygenEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "obligate aerobe",
                PermissibleValue(text="obligate aerobe") )
        setattr(cls, "obligate anaerobe",
                PermissibleValue(text="obligate anaerobe") )

class RnaContTypeEnum(EnumDefinitionImpl):

    plate = PermissibleValue(text="plate")
    tube = PermissibleValue(text="tube")

    _defn = EnumDefinition(
        name="RnaContTypeEnum",
    )

class RnaSampleFormatEnum(EnumDefinitionImpl):

    DNAStable = PermissibleValue(text="DNAStable")
    Ethanol = PermissibleValue(text="Ethanol")
    PBS = PermissibleValue(text="PBS")
    Pellet = PermissibleValue(text="Pellet")
    RNAStable = PermissibleValue(text="RNAStable")
    TE = PermissibleValue(text="TE")
    Water = PermissibleValue(text="Water")

    _defn = EnumDefinition(
        name="RnaSampleFormatEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "10 mM Tris-HCl",
                PermissibleValue(text="10 mM Tris-HCl") )
        setattr(cls, "Low EDTA TE",
                PermissibleValue(text="Low EDTA TE") )
        setattr(cls, "MDA reaction buffer",
                PermissibleValue(text="MDA reaction buffer") )

class SampleTypeEnum(EnumDefinitionImpl):

    soil = PermissibleValue(text="soil")
    water_extract_soil = PermissibleValue(text="water_extract_soil")

    _defn = EnumDefinition(
        name="SampleTypeEnum",
    )

class SpecificEcosystemEnum(EnumDefinitionImpl):

    Agricultural = PermissibleValue(text="Agricultural")
    Alpine = PermissibleValue(text="Alpine")
    Bog = PermissibleValue(text="Bog")
    Contaminated = PermissibleValue(text="Contaminated")
    Desert = PermissibleValue(text="Desert")
    Farm = PermissibleValue(text="Farm")
    Grasslands = PermissibleValue(text="Grasslands")
    Meadow = PermissibleValue(text="Meadow")
    Mine = PermissibleValue(text="Mine")
    Permafrost = PermissibleValue(text="Permafrost")
    River = PermissibleValue(text="River")
    Shrubland = PermissibleValue(text="Shrubland")
    Unclassified = PermissibleValue(text="Unclassified")

    _defn = EnumDefinition(
        name="SpecificEcosystemEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Agricultural land",
                PermissibleValue(text="Agricultural land") )
        setattr(cls, "Agricultural soil",
                PermissibleValue(text="Agricultural soil") )
        setattr(cls, "Boreal forest",
                PermissibleValue(text="Boreal forest") )
        setattr(cls, "Forest soil",
                PermissibleValue(text="Forest soil") )
        setattr(cls, "Forest Soil",
                PermissibleValue(text="Forest Soil") )
        setattr(cls, "Mine drainage",
                PermissibleValue(text="Mine drainage") )
        setattr(cls, "Oil-contaminated",
                PermissibleValue(text="Oil-contaminated") )
        setattr(cls, "Orchard soil",
                PermissibleValue(text="Orchard soil") )
        setattr(cls, "Riparian soil",
                PermissibleValue(text="Riparian soil") )
        setattr(cls, "Tropical rainforest",
                PermissibleValue(text="Tropical rainforest") )
        setattr(cls, "Uranium contaminated",
                PermissibleValue(text="Uranium contaminated") )

class StoreCondEnum(EnumDefinitionImpl):

    fresh = PermissibleValue(text="fresh")
    frozen = PermissibleValue(text="frozen")
    lyophilized = PermissibleValue(text="lyophilized")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="StoreCondEnum",
    )

class CurLandUseEnum(EnumDefinitionImpl):

    badlands = PermissibleValue(text="badlands")
    cities = PermissibleValue(text="cities")
    farmstead = PermissibleValue(text="farmstead")
    gravel = PermissibleValue(text="gravel")
    hayland = PermissibleValue(text="hayland")
    mudflats = PermissibleValue(text="mudflats")
    rangeland = PermissibleValue(text="rangeland")
    rock = PermissibleValue(text="rock")
    sand = PermissibleValue(text="sand")

    _defn = EnumDefinition(
        name="CurLandUseEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "conifers (e.g. pine,spruce,fir,cypress)",
                PermissibleValue(text="conifers (e.g. pine,spruce,fir,cypress)") )
        setattr(cls, "crop trees (nuts,fruit,christmas trees,nursery trees)",
                PermissibleValue(text="crop trees (nuts,fruit,christmas trees,nursery trees)") )
        setattr(cls, "hardwoods (e.g. oak,hickory,elm,aspen)",
                PermissibleValue(text="hardwoods (e.g. oak,hickory,elm,aspen)") )
        setattr(cls, "horticultural plants (e.g. tulips)",
                PermissibleValue(text="horticultural plants (e.g. tulips)") )
        setattr(cls, "industrial areas",
                PermissibleValue(text="industrial areas") )
        setattr(cls, "intermixed hardwood and conifers",
                PermissibleValue(text="intermixed hardwood and conifers") )
        setattr(cls, "marshlands (grass,sedges,rushes)",
                PermissibleValue(text="marshlands (grass,sedges,rushes)") )
        setattr(cls, "meadows (grasses,alfalfa,fescue,bromegrass,timothy)",
                PermissibleValue(text="meadows (grasses,alfalfa,fescue,bromegrass,timothy)") )
        setattr(cls, "mines/quarries",
                PermissibleValue(text="mines/quarries") )
        setattr(cls, "oil waste areas",
                PermissibleValue(text="oil waste areas") )
        setattr(cls, "pastureland (grasslands used for livestock grazing)",
                PermissibleValue(text="pastureland (grasslands used for livestock grazing)") )
        setattr(cls, "permanent snow or ice",
                PermissibleValue(text="permanent snow or ice") )
        setattr(cls, "rainforest (evergreen forest receiving >406 cm annual rainfall)",
                PermissibleValue(text="rainforest (evergreen forest receiving >406 cm annual rainfall)") )
        setattr(cls, "roads/railroads",
                PermissibleValue(text="roads/railroads") )
        setattr(cls, "row crops",
                PermissibleValue(text="row crops") )
        setattr(cls, "saline seeps",
                PermissibleValue(text="saline seeps") )
        setattr(cls, "salt flats",
                PermissibleValue(text="salt flats") )
        setattr(cls, "shrub crops (blueberries,nursery ornamentals,filberts)",
                PermissibleValue(text="shrub crops (blueberries,nursery ornamentals,filberts)") )
        setattr(cls, "shrub land (e.g. mesquite,sage-brush,creosote bush,shrub oak,eucalyptus)",
                PermissibleValue(text="shrub land (e.g. mesquite,sage-brush,creosote bush,shrub oak,eucalyptus)") )
        setattr(cls, "small grains",
                PermissibleValue(text="small grains") )
        setattr(cls, "successional shrub land (tree saplings,hazels,sumacs,chokecherry,shrub dogwoods,blackberries)",
                PermissibleValue(text="successional shrub land (tree saplings,hazels,sumacs,chokecherry,shrub dogwoods,blackberries)") )
        setattr(cls, "swamp (permanent or semi-permanent water body dominated by woody plants)",
                PermissibleValue(text="swamp (permanent or semi-permanent water body dominated by woody plants)") )
        setattr(cls, "tropical (e.g. mangrove,palms)",
                PermissibleValue(text="tropical (e.g. mangrove,palms)") )
        setattr(cls, "tundra (mosses,lichens)",
                PermissibleValue(text="tundra (mosses,lichens)") )
        setattr(cls, "vegetable crops",
                PermissibleValue(text="vegetable crops") )
        setattr(cls, "vine crops (grapes)",
                PermissibleValue(text="vine crops (grapes)") )

class DrainageClassEnum(EnumDefinitionImpl):

    poorly = PermissibleValue(text="poorly")
    well = PermissibleValue(text="well")

    _defn = EnumDefinition(
        name="DrainageClassEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "excessively drained",
                PermissibleValue(text="excessively drained") )
        setattr(cls, "moderately well",
                PermissibleValue(text="moderately well") )
        setattr(cls, "somewhat poorly",
                PermissibleValue(text="somewhat poorly") )
        setattr(cls, "very poorly",
                PermissibleValue(text="very poorly") )

class FaoClassEnum(EnumDefinitionImpl):

    Acrisols = PermissibleValue(text="Acrisols")
    Andosols = PermissibleValue(text="Andosols")
    Arenosols = PermissibleValue(text="Arenosols")
    Cambisols = PermissibleValue(text="Cambisols")
    Chernozems = PermissibleValue(text="Chernozems")
    Ferralsols = PermissibleValue(text="Ferralsols")
    Fluvisols = PermissibleValue(text="Fluvisols")
    Gleysols = PermissibleValue(text="Gleysols")
    Greyzems = PermissibleValue(text="Greyzems")
    Gypsisols = PermissibleValue(text="Gypsisols")
    Histosols = PermissibleValue(text="Histosols")
    Kastanozems = PermissibleValue(text="Kastanozems")
    Lithosols = PermissibleValue(text="Lithosols")
    Luvisols = PermissibleValue(text="Luvisols")
    Nitosols = PermissibleValue(text="Nitosols")
    Phaeozems = PermissibleValue(text="Phaeozems")
    Planosols = PermissibleValue(text="Planosols")
    Podzols = PermissibleValue(text="Podzols")
    Podzoluvisols = PermissibleValue(text="Podzoluvisols")
    Rankers = PermissibleValue(text="Rankers")
    Regosols = PermissibleValue(text="Regosols")
    Rendzinas = PermissibleValue(text="Rendzinas")
    Solonchaks = PermissibleValue(text="Solonchaks")
    Solonetz = PermissibleValue(text="Solonetz")
    Vertisols = PermissibleValue(text="Vertisols")
    Yermosols = PermissibleValue(text="Yermosols")

    _defn = EnumDefinition(
        name="FaoClassEnum",
    )

class OxyStatSampEnum(EnumDefinitionImpl):

    aerobic = PermissibleValue(text="aerobic")
    anaerobic = PermissibleValue(text="anaerobic")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="OxyStatSampEnum",
    )

class ProfilePositionEnum(EnumDefinitionImpl):

    backslope = PermissibleValue(text="backslope")
    footslope = PermissibleValue(text="footslope")
    shoulder = PermissibleValue(text="shoulder")
    summit = PermissibleValue(text="summit")
    toeslope = PermissibleValue(text="toeslope")

    _defn = EnumDefinition(
        name="ProfilePositionEnum",
    )

class SoilHorizonEnum(EnumDefinitionImpl):

    Permafrost = PermissibleValue(text="Permafrost")

    _defn = EnumDefinition(
        name="SoilHorizonEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "A horizon",
                PermissibleValue(text="A horizon") )
        setattr(cls, "B horizon",
                PermissibleValue(text="B horizon") )
        setattr(cls, "C horizon",
                PermissibleValue(text="C horizon") )
        setattr(cls, "E horizon",
                PermissibleValue(text="E horizon") )
        setattr(cls, "O horizon",
                PermissibleValue(text="O horizon") )
        setattr(cls, "R layer",
                PermissibleValue(text="R layer") )

class TillageEnum(EnumDefinitionImpl):

    chisel = PermissibleValue(text="chisel")
    drill = PermissibleValue(text="drill")
    mouldboard = PermissibleValue(text="mouldboard")
    tined = PermissibleValue(text="tined")

    _defn = EnumDefinition(
        name="TillageEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "cutting disc",
                PermissibleValue(text="cutting disc") )
        setattr(cls, "disc plough",
                PermissibleValue(text="disc plough") )
        setattr(cls, "ridge till",
                PermissibleValue(text="ridge till") )
        setattr(cls, "strip tillage",
                PermissibleValue(text="strip tillage") )
        setattr(cls, "zonal tillage",
                PermissibleValue(text="zonal tillage") )

# Slots
class slots:
    pass

slots.project_ID = Slot(uri=NMDC_DH.project_ID, name="project_ID", curie=NMDC_DH.curie('project_ID'),
                   model_uri=NMDC_DH.project_ID, domain=None, range=Optional[str])

slots.sample_type = Slot(uri=NMDC_DH.sample_type, name="sample_type", curie=NMDC_DH.curie('sample_type'),
                   model_uri=NMDC_DH.sample_type, domain=None, range=Optional[str])

slots.sample_shipped = Slot(uri=NMDC_DH.sample_shipped, name="sample_shipped", curie=NMDC_DH.curie('sample_shipped'),
                   model_uri=NMDC_DH.sample_shipped, domain=None, range=Optional[str])

slots.EMSL_store_temp = Slot(uri=NMDC_DH.EMSL_store_temp, name="EMSL_store_temp", curie=NMDC_DH.curie('EMSL_store_temp'),
                   model_uri=NMDC_DH.EMSL_store_temp, domain=None, range=Optional[str])

slots.technical_reps = Slot(uri=NMDC_DH.technical_reps, name="technical_reps", curie=NMDC_DH.curie('technical_reps'),
                   model_uri=NMDC_DH.technical_reps, domain=None, range=Optional[str])

slots.replicate_number = Slot(uri=NMDC_DH.replicate_number, name="replicate_number", curie=NMDC_DH.curie('replicate_number'),
                   model_uri=NMDC_DH.replicate_number, domain=None, range=Optional[str])

slots.dna_seq_project = Slot(uri=NMDC_DH.dna_seq_project, name="dna_seq_project", curie=NMDC_DH.curie('dna_seq_project'),
                   model_uri=NMDC_DH.dna_seq_project, domain=None, range=Optional[str])

slots.dna_seq_project_name = Slot(uri=NMDC_DH.dna_seq_project_name, name="dna_seq_project_name", curie=NMDC_DH.curie('dna_seq_project_name'),
                   model_uri=NMDC_DH.dna_seq_project_name, domain=None, range=Optional[str])

slots.dna_samp_ID = Slot(uri=NMDC_DH.dna_samp_ID, name="dna_samp_ID", curie=NMDC_DH.curie('dna_samp_ID'),
                   model_uri=NMDC_DH.dna_samp_ID, domain=None, range=Optional[str])

slots.dna_sample_name = Slot(uri=NMDC_DH.dna_sample_name, name="dna_sample_name", curie=NMDC_DH.curie('dna_sample_name'),
                   model_uri=NMDC_DH.dna_sample_name, domain=None, range=Optional[str])

slots.dna_concentration = Slot(uri=NMDC_DH.dna_concentration, name="dna_concentration", curie=NMDC_DH.curie('dna_concentration'),
                   model_uri=NMDC_DH.dna_concentration, domain=None, range=Optional[str])

slots.dna_volume = Slot(uri=NMDC_DH.dna_volume, name="dna_volume", curie=NMDC_DH.curie('dna_volume'),
                   model_uri=NMDC_DH.dna_volume, domain=None, range=Optional[str])

slots.dna_absorb1 = Slot(uri=NMDC_DH.dna_absorb1, name="dna_absorb1", curie=NMDC_DH.curie('dna_absorb1'),
                   model_uri=NMDC_DH.dna_absorb1, domain=None, range=Optional[str])

slots.dna_absorb2 = Slot(uri=NMDC_DH.dna_absorb2, name="dna_absorb2", curie=NMDC_DH.curie('dna_absorb2'),
                   model_uri=NMDC_DH.dna_absorb2, domain=None, range=Optional[str])

slots.dna_container_ID = Slot(uri=NMDC_DH.dna_container_ID, name="dna_container_ID", curie=NMDC_DH.curie('dna_container_ID'),
                   model_uri=NMDC_DH.dna_container_ID, domain=None, range=Optional[str])

slots.dna_cont_type = Slot(uri=NMDC_DH.dna_cont_type, name="dna_cont_type", curie=NMDC_DH.curie('dna_cont_type'),
                   model_uri=NMDC_DH.dna_cont_type, domain=None, range=Optional[str])

slots.dna_cont_well = Slot(uri=NMDC_DH.dna_cont_well, name="dna_cont_well", curie=NMDC_DH.curie('dna_cont_well'),
                   model_uri=NMDC_DH.dna_cont_well, domain=None, range=Optional[str])

slots.dna_sample_format = Slot(uri=NMDC_DH.dna_sample_format, name="dna_sample_format", curie=NMDC_DH.curie('dna_sample_format'),
                   model_uri=NMDC_DH.dna_sample_format, domain=None, range=Optional[str])

slots.dna_dnase = Slot(uri=NMDC_DH.dna_dnase, name="dna_dnase", curie=NMDC_DH.curie('dna_dnase'),
                   model_uri=NMDC_DH.dna_dnase, domain=None, range=Optional[str])

slots.dna_organisms = Slot(uri=NMDC_DH.dna_organisms, name="dna_organisms", curie=NMDC_DH.curie('dna_organisms'),
                   model_uri=NMDC_DH.dna_organisms, domain=None, range=Optional[str])

slots.dna_collect_site = Slot(uri=NMDC_DH.dna_collect_site, name="dna_collect_site", curie=NMDC_DH.curie('dna_collect_site'),
                   model_uri=NMDC_DH.dna_collect_site, domain=None, range=Optional[str])

slots.dna_isolate_meth = Slot(uri=NMDC_DH.dna_isolate_meth, name="dna_isolate_meth", curie=NMDC_DH.curie('dna_isolate_meth'),
                   model_uri=NMDC_DH.dna_isolate_meth, domain=None, range=Optional[str])

slots.dna_seq_project_PI = Slot(uri=NMDC_DH.dna_seq_project_PI, name="dna_seq_project_PI", curie=NMDC_DH.curie('dna_seq_project_PI'),
                   model_uri=NMDC_DH.dna_seq_project_PI, domain=None, range=Optional[str])

slots.dna_project_contact = Slot(uri=NMDC_DH.dna_project_contact, name="dna_project_contact", curie=NMDC_DH.curie('dna_project_contact'),
                   model_uri=NMDC_DH.dna_project_contact, domain=None, range=Optional[str])

slots.proposal_dna = Slot(uri=NMDC_DH.proposal_dna, name="proposal_dna", curie=NMDC_DH.curie('proposal_dna'),
                   model_uri=NMDC_DH.proposal_dna, domain=None, range=Optional[str])

slots.rna_seq_project = Slot(uri=NMDC_DH.rna_seq_project, name="rna_seq_project", curie=NMDC_DH.curie('rna_seq_project'),
                   model_uri=NMDC_DH.rna_seq_project, domain=None, range=Optional[str])

slots.rna_seq_project_name = Slot(uri=NMDC_DH.rna_seq_project_name, name="rna_seq_project_name", curie=NMDC_DH.curie('rna_seq_project_name'),
                   model_uri=NMDC_DH.rna_seq_project_name, domain=None, range=Optional[str])

slots.rna_samp_ID = Slot(uri=NMDC_DH.rna_samp_ID, name="rna_samp_ID", curie=NMDC_DH.curie('rna_samp_ID'),
                   model_uri=NMDC_DH.rna_samp_ID, domain=None, range=Optional[str])

slots.rna_sample_name = Slot(uri=NMDC_DH.rna_sample_name, name="rna_sample_name", curie=NMDC_DH.curie('rna_sample_name'),
                   model_uri=NMDC_DH.rna_sample_name, domain=None, range=Optional[str])

slots.rna_concentration = Slot(uri=NMDC_DH.rna_concentration, name="rna_concentration", curie=NMDC_DH.curie('rna_concentration'),
                   model_uri=NMDC_DH.rna_concentration, domain=None, range=Optional[str])

slots.rna_volume = Slot(uri=NMDC_DH.rna_volume, name="rna_volume", curie=NMDC_DH.curie('rna_volume'),
                   model_uri=NMDC_DH.rna_volume, domain=None, range=Optional[str])

slots.rna_absorb1 = Slot(uri=NMDC_DH.rna_absorb1, name="rna_absorb1", curie=NMDC_DH.curie('rna_absorb1'),
                   model_uri=NMDC_DH.rna_absorb1, domain=None, range=Optional[str])

slots.rna_absorb2 = Slot(uri=NMDC_DH.rna_absorb2, name="rna_absorb2", curie=NMDC_DH.curie('rna_absorb2'),
                   model_uri=NMDC_DH.rna_absorb2, domain=None, range=Optional[str])

slots.rna_container_ID = Slot(uri=NMDC_DH.rna_container_ID, name="rna_container_ID", curie=NMDC_DH.curie('rna_container_ID'),
                   model_uri=NMDC_DH.rna_container_ID, domain=None, range=Optional[str])

slots.rna_cont_type = Slot(uri=NMDC_DH.rna_cont_type, name="rna_cont_type", curie=NMDC_DH.curie('rna_cont_type'),
                   model_uri=NMDC_DH.rna_cont_type, domain=None, range=Optional[str])

slots.rna_cont_well = Slot(uri=NMDC_DH.rna_cont_well, name="rna_cont_well", curie=NMDC_DH.curie('rna_cont_well'),
                   model_uri=NMDC_DH.rna_cont_well, domain=None, range=Optional[str])

slots.rna_sample_format = Slot(uri=NMDC_DH.rna_sample_format, name="rna_sample_format", curie=NMDC_DH.curie('rna_sample_format'),
                   model_uri=NMDC_DH.rna_sample_format, domain=None, range=Optional[str])

slots.dnase_rna = Slot(uri=NMDC_DH.dnase_rna, name="dnase_rna", curie=NMDC_DH.curie('dnase_rna'),
                   model_uri=NMDC_DH.dnase_rna, domain=None, range=Optional[str])

slots.rna_organisms = Slot(uri=NMDC_DH.rna_organisms, name="rna_organisms", curie=NMDC_DH.curie('rna_organisms'),
                   model_uri=NMDC_DH.rna_organisms, domain=None, range=Optional[str])

slots.rna_collect_site = Slot(uri=NMDC_DH.rna_collect_site, name="rna_collect_site", curie=NMDC_DH.curie('rna_collect_site'),
                   model_uri=NMDC_DH.rna_collect_site, domain=None, range=Optional[str])

slots.rna_isolate_meth = Slot(uri=NMDC_DH.rna_isolate_meth, name="rna_isolate_meth", curie=NMDC_DH.curie('rna_isolate_meth'),
                   model_uri=NMDC_DH.rna_isolate_meth, domain=None, range=Optional[str])

slots.rna_seq_project_PI = Slot(uri=NMDC_DH.rna_seq_project_PI, name="rna_seq_project_PI", curie=NMDC_DH.curie('rna_seq_project_PI'),
                   model_uri=NMDC_DH.rna_seq_project_PI, domain=None, range=Optional[str])

slots.rna_project_contact = Slot(uri=NMDC_DH.rna_project_contact, name="rna_project_contact", curie=NMDC_DH.curie('rna_project_contact'),
                   model_uri=NMDC_DH.rna_project_contact, domain=None, range=Optional[str])

slots.proposal_rna = Slot(uri=NMDC_DH.proposal_rna, name="proposal_rna", curie=NMDC_DH.curie('proposal_rna'),
                   model_uri=NMDC_DH.proposal_rna, domain=None, range=Optional[str])

slots.collection_time = Slot(uri=NMDC_DH.collection_time, name="collection_time", curie=NMDC_DH.curie('collection_time'),
                   model_uri=NMDC_DH.collection_time, domain=None, range=Optional[str])

slots.collection_date_inc = Slot(uri=NMDC_DH.collection_date_inc, name="collection_date_inc", curie=NMDC_DH.curie('collection_date_inc'),
                   model_uri=NMDC_DH.collection_date_inc, domain=None, range=Optional[str])

slots.collection_time_inc = Slot(uri=NMDC_DH.collection_time_inc, name="collection_time_inc", curie=NMDC_DH.curie('collection_time_inc'),
                   model_uri=NMDC_DH.collection_time_inc, domain=None, range=Optional[str])

slots.start_date_inc = Slot(uri=NMDC_DH.start_date_inc, name="start_date_inc", curie=NMDC_DH.curie('start_date_inc'),
                   model_uri=NMDC_DH.start_date_inc, domain=None, range=Optional[str])

slots.start_time_inc = Slot(uri=NMDC_DH.start_time_inc, name="start_time_inc", curie=NMDC_DH.curie('start_time_inc'),
                   model_uri=NMDC_DH.start_time_inc, domain=None, range=Optional[str])

slots.filter_method = Slot(uri=NMDC_DH.filter_method, name="filter_method", curie=NMDC_DH.curie('filter_method'),
                   model_uri=NMDC_DH.filter_method, domain=None, range=Optional[str])

slots.experimental_factor_other = Slot(uri=NMDC_DH.experimental_factor_other, name="experimental_factor_other", curie=NMDC_DH.curie('experimental_factor_other'),
                   model_uri=NMDC_DH.experimental_factor_other, domain=None, range=Optional[str])

slots.non_microb_biomass = Slot(uri=NMDC_DH.non_microb_biomass, name="non_microb_biomass", curie=NMDC_DH.curie('non_microb_biomass'),
                   model_uri=NMDC_DH.non_microb_biomass, domain=None, range=Optional[str])

slots.non_microb_biomass_method = Slot(uri=NMDC_DH.non_microb_biomass_method, name="non_microb_biomass_method", curie=NMDC_DH.curie('non_microb_biomass_method'),
                   model_uri=NMDC_DH.non_microb_biomass_method, domain=None, range=Optional[str])

slots.microbial_biomass_C = Slot(uri=NMDC_DH.microbial_biomass_C, name="microbial_biomass_C", curie=NMDC_DH.curie('microbial_biomass_C'),
                   model_uri=NMDC_DH.microbial_biomass_C, domain=None, range=Optional[str])

slots.micro_biomass_C_meth = Slot(uri=NMDC_DH.micro_biomass_C_meth, name="micro_biomass_C_meth", curie=NMDC_DH.curie('micro_biomass_C_meth'),
                   model_uri=NMDC_DH.micro_biomass_C_meth, domain=None, range=Optional[str])

slots.microbial_biomass_N = Slot(uri=NMDC_DH.microbial_biomass_N, name="microbial_biomass_N", curie=NMDC_DH.curie('microbial_biomass_N'),
                   model_uri=NMDC_DH.microbial_biomass_N, domain=None, range=Optional[str])

slots.micro_biomass_N_meth = Slot(uri=NMDC_DH.micro_biomass_N_meth, name="micro_biomass_N_meth", curie=NMDC_DH.curie('micro_biomass_N_meth'),
                   model_uri=NMDC_DH.micro_biomass_N_meth, domain=None, range=Optional[str])

slots.org_nitro_method = Slot(uri=NMDC_DH.org_nitro_method, name="org_nitro_method", curie=NMDC_DH.curie('org_nitro_method'),
                   model_uri=NMDC_DH.org_nitro_method, domain=None, range=Optional[str])

slots.other_treatment = Slot(uri=NMDC_DH.other_treatment, name="other_treatment", curie=NMDC_DH.curie('other_treatment'),
                   model_uri=NMDC_DH.other_treatment, domain=None, range=Optional[str])

slots.isotope_exposure = Slot(uri=NMDC_DH.isotope_exposure, name="isotope_exposure", curie=NMDC_DH.curie('isotope_exposure'),
                   model_uri=NMDC_DH.isotope_exposure, domain=None, range=Optional[str])

slots.analysis_type = Slot(uri=NMDC_DH.analysis_type, name="analysis_type", curie=NMDC_DH.curie('analysis_type'),
                   model_uri=NMDC_DH.analysis_type, domain=None, range=Optional[str])

slots.env_package = Slot(uri=NMDC_DH.env_package, name="env_package", curie=NMDC_DH.curie('env_package'),
                   model_uri=NMDC_DH.env_package, domain=None, range=Optional[str])

slots.sample_link = Slot(uri=NMDC_DH.sample_link, name="sample_link", curie=NMDC_DH.curie('sample_link'),
                   model_uri=NMDC_DH.sample_link, domain=None, range=Optional[str])

slots.has_unit = Slot(uri=NMDC_DH.has_unit, name="has unit", curie=NMDC_DH.curie('has_unit'),
                   model_uri=NMDC_DH.has_unit, domain=None, range=Optional[str])

slots.has_numeric_value = Slot(uri=NMDC_DH.has_numeric_value, name="has numeric value", curie=NMDC_DH.curie('has_numeric_value'),
                   model_uri=NMDC_DH.has_numeric_value, domain=None, range=Optional[str])

slots.has_raw_value = Slot(uri=NMDC_DH.has_raw_value, name="has raw value", curie=NMDC_DH.curie('has_raw_value'),
                   model_uri=NMDC_DH.has_raw_value, domain=None, range=Optional[str])

slots.ecosystem = Slot(uri=NMDC_DH.ecosystem, name="ecosystem", curie=NMDC_DH.curie('ecosystem'),
                   model_uri=NMDC_DH.ecosystem, domain=None, range=Optional[str])

slots.ecosystem_category = Slot(uri=NMDC_DH.ecosystem_category, name="ecosystem_category", curie=NMDC_DH.curie('ecosystem_category'),
                   model_uri=NMDC_DH.ecosystem_category, domain=None, range=Optional[str])

slots.ecosystem_subtype = Slot(uri=NMDC_DH.ecosystem_subtype, name="ecosystem_subtype", curie=NMDC_DH.curie('ecosystem_subtype'),
                   model_uri=NMDC_DH.ecosystem_subtype, domain=None, range=Optional[str])

slots.ecosystem_type = Slot(uri=NMDC_DH.ecosystem_type, name="ecosystem_type", curie=NMDC_DH.curie('ecosystem_type'),
                   model_uri=NMDC_DH.ecosystem_type, domain=None, range=Optional[str])

slots.specific_ecosystem = Slot(uri=NMDC_DH.specific_ecosystem, name="specific_ecosystem", curie=NMDC_DH.curie('specific_ecosystem'),
                   model_uri=NMDC_DH.specific_ecosystem, domain=None, range=Optional[str])

slots.gold_path_field = Slot(uri=NMDC_DH.gold_path_field, name="gold_path_field", curie=NMDC_DH.curie('gold_path_field'),
                   model_uri=NMDC_DH.gold_path_field, domain=None, range=Optional[str])

slots.attribute = Slot(uri=NMDC_DH.attribute, name="attribute", curie=NMDC_DH.curie('attribute'),
                   model_uri=NMDC_DH.attribute, domain=None, range=Optional[str])

slots.environment_field = Slot(uri=NMDC_DH.environment_field, name="environment field", curie=NMDC_DH.curie('environment_field'),
                   model_uri=NMDC_DH.environment_field, domain=None, range=Optional[str])

slots.core_field = Slot(uri=NMDC_DH.core_field, name="core field", curie=NMDC_DH.curie('core_field'),
                   model_uri=NMDC_DH.core_field, domain=None, range=Optional[str])

slots.nucleic_acid_sequence_source_field = Slot(uri=NMDC_DH.nucleic_acid_sequence_source_field, name="nucleic acid sequence source field", curie=NMDC_DH.curie('nucleic_acid_sequence_source_field'),
                   model_uri=NMDC_DH.nucleic_acid_sequence_source_field, domain=None, range=Optional[str])

slots.investigation_field = Slot(uri=NMDC_DH.investigation_field, name="investigation field", curie=NMDC_DH.curie('investigation_field'),
                   model_uri=NMDC_DH.investigation_field, domain=None, range=Optional[str])

slots.agrochem_addition = Slot(uri=MIXS['0000639'], name="agrochem_addition", curie=MIXS.curie('0000639'),
                   model_uri=NMDC_DH.agrochem_addition, domain=None, range=Optional[Union[str, List[str]]])

slots.air_temp_regm = Slot(uri=MIXS['0000551'], name="air_temp_regm", curie=MIXS.curie('0000551'),
                   model_uri=NMDC_DH.air_temp_regm, domain=None, range=Optional[Union[str, List[str]]])

slots.al_sat = Slot(uri=MIXS['0000607'], name="al_sat", curie=MIXS.curie('0000607'),
                   model_uri=NMDC_DH.al_sat, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.al_sat_meth = Slot(uri=MIXS['0000324'], name="al_sat_meth", curie=MIXS.curie('0000324'),
                   model_uri=NMDC_DH.al_sat_meth, domain=None, range=Optional[str])

slots.alt = Slot(uri=MIXS['0000094'], name="alt", curie=MIXS.curie('0000094'),
                   model_uri=NMDC_DH.alt, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.annual_precpt = Slot(uri=MIXS['0000644'], name="annual_precpt", curie=MIXS.curie('0000644'),
                   model_uri=NMDC_DH.annual_precpt, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.annual_temp = Slot(uri=MIXS['0000642'], name="annual_temp", curie=MIXS.curie('0000642'),
                   model_uri=NMDC_DH.annual_temp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.biotic_regm = Slot(uri=MIXS['0001038'], name="biotic_regm", curie=MIXS.curie('0001038'),
                   model_uri=NMDC_DH.biotic_regm, domain=None, range=Optional[str])

slots.biotic_relationship = Slot(uri=MIXS['0000028'], name="biotic_relationship", curie=MIXS.curie('0000028'),
                   model_uri=NMDC_DH.biotic_relationship, domain=None, range=Optional[Union[str, "BioticRelationshipEnum"]])

slots.carb_nitro_ratio = Slot(uri=MIXS['0000310'], name="carb_nitro_ratio", curie=MIXS.curie('0000310'),
                   model_uri=NMDC_DH.carb_nitro_ratio, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.chem_administration = Slot(uri=MIXS['0000751'], name="chem_administration", curie=MIXS.curie('0000751'),
                   model_uri=NMDC_DH.chem_administration, domain=None, range=Optional[Union[str, List[str]]])

slots.climate_environment = Slot(uri=MIXS['0001040'], name="climate_environment", curie=MIXS.curie('0001040'),
                   model_uri=NMDC_DH.climate_environment, domain=None, range=Optional[Union[str, List[str]]])

slots.collection_date = Slot(uri=MIXS['0000011'], name="collection_date", curie=MIXS.curie('0000011'),
                   model_uri=NMDC_DH.collection_date, domain=None, range=Union[str, XSDDate])

slots.crop_rotation = Slot(uri=MIXS['0000318'], name="crop_rotation", curie=MIXS.curie('0000318'),
                   model_uri=NMDC_DH.crop_rotation, domain=None, range=Optional[str])

slots.cur_land_use = Slot(uri=MIXS['0001080'], name="cur_land_use", curie=MIXS.curie('0001080'),
                   model_uri=NMDC_DH.cur_land_use, domain=None, range=Optional[Union[str, "CurLandUseEnum"]])

slots.cur_vegetation = Slot(uri=MIXS['0000312'], name="cur_vegetation", curie=MIXS.curie('0000312'),
                   model_uri=NMDC_DH.cur_vegetation, domain=None, range=Optional[str])

slots.cur_vegetation_meth = Slot(uri=MIXS['0000314'], name="cur_vegetation_meth", curie=MIXS.curie('0000314'),
                   model_uri=NMDC_DH.cur_vegetation_meth, domain=None, range=Optional[str])

slots.depth = Slot(uri=MIXS['0000018'], name="depth", curie=MIXS.curie('0000018'),
                   model_uri=NMDC_DH.depth, domain=None, range=Union[dict, QuantityValue])

slots.drainage_class = Slot(uri=MIXS['0001085'], name="drainage_class", curie=MIXS.curie('0001085'),
                   model_uri=NMDC_DH.drainage_class, domain=None, range=Optional[Union[str, "DrainageClassEnum"]])

slots.elev = Slot(uri=MIXS['0000093'], name="elev", curie=MIXS.curie('0000093'),
                   model_uri=NMDC_DH.elev, domain=None, range=Union[dict, QuantityValue])

slots.env_broad_scale = Slot(uri=MIXS['0000012'], name="env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=NMDC_DH.env_broad_scale, domain=None, range=str)

slots.env_local_scale = Slot(uri=MIXS['0000013'], name="env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=NMDC_DH.env_local_scale, domain=None, range=str)

slots.env_medium = Slot(uri=MIXS['0000014'], name="env_medium", curie=MIXS.curie('0000014'),
                   model_uri=NMDC_DH.env_medium, domain=None, range=str)

slots.experimental_factor = Slot(uri=MIXS['0000008'], name="experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=NMDC_DH.experimental_factor, domain=None, range=Optional[str])

slots.extreme_event = Slot(uri=MIXS['0000320'], name="extreme_event", curie=MIXS.curie('0000320'),
                   model_uri=NMDC_DH.extreme_event, domain=None, range=Optional[Union[str, XSDDate]])

slots.fao_class = Slot(uri=MIXS['0001083'], name="fao_class", curie=MIXS.curie('0001083'),
                   model_uri=NMDC_DH.fao_class, domain=None, range=Optional[Union[str, "FaoClassEnum"]])

slots.fire = Slot(uri=MIXS['0001086'], name="fire", curie=MIXS.curie('0001086'),
                   model_uri=NMDC_DH.fire, domain=None, range=Optional[Union[str, XSDDate]])

slots.flooding = Slot(uri=MIXS['0000319'], name="flooding", curie=MIXS.curie('0000319'),
                   model_uri=NMDC_DH.flooding, domain=None, range=Optional[Union[str, XSDDate]])

slots.gaseous_environment = Slot(uri=MIXS['0000558'], name="gaseous_environment", curie=MIXS.curie('0000558'),
                   model_uri=NMDC_DH.gaseous_environment, domain=None, range=Optional[Union[str, List[str]]])

slots.geo_loc_name = Slot(uri=MIXS['0000010'], name="geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=NMDC_DH.geo_loc_name, domain=None, range=str)

slots.growth_facil = Slot(uri=MIXS['0001043'], name="growth_facil", curie=MIXS.curie('0001043'),
                   model_uri=NMDC_DH.growth_facil, domain=None, range=Optional[str])

slots.heavy_metals = Slot(uri=MIXS['0000652'], name="heavy_metals", curie=MIXS.curie('0000652'),
                   model_uri=NMDC_DH.heavy_metals, domain=None, range=Optional[Union[str, List[str]]])

slots.heavy_metals_meth = Slot(uri=MIXS['0000343'], name="heavy_metals_meth", curie=MIXS.curie('0000343'),
                   model_uri=NMDC_DH.heavy_metals_meth, domain=None, range=Optional[str])

slots.horizon_meth = Slot(uri=MIXS['0000321'], name="horizon_meth", curie=MIXS.curie('0000321'),
                   model_uri=NMDC_DH.horizon_meth, domain=None, range=Optional[str])

slots.humidity_regm = Slot(uri=MIXS['0000568'], name="humidity_regm", curie=MIXS.curie('0000568'),
                   model_uri=NMDC_DH.humidity_regm, domain=None, range=Optional[Union[str, List[str]]])

slots.lat_lon = Slot(uri=MIXS['0000009'], name="lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=NMDC_DH.lat_lon, domain=None, range=str)

slots.light_regm = Slot(uri=MIXS['0000569'], name="light_regm", curie=MIXS.curie('0000569'),
                   model_uri=NMDC_DH.light_regm, domain=None, range=Optional[str])

slots.link_class_info = Slot(uri=MIXS['0000329'], name="link_class_info", curie=MIXS.curie('0000329'),
                   model_uri=NMDC_DH.link_class_info, domain=None, range=Optional[str])

slots.link_climate_info = Slot(uri=MIXS['0000328'], name="link_climate_info", curie=MIXS.curie('0000328'),
                   model_uri=NMDC_DH.link_climate_info, domain=None, range=Optional[str])

slots.local_class = Slot(uri=MIXS['0000330'], name="local_class", curie=MIXS.curie('0000330'),
                   model_uri=NMDC_DH.local_class, domain=None, range=Optional[str])

slots.local_class_meth = Slot(uri=MIXS['0000331'], name="local_class_meth", curie=MIXS.curie('0000331'),
                   model_uri=NMDC_DH.local_class_meth, domain=None, range=Optional[str])

slots.micro_biomass_meth = Slot(uri=MIXS['0000339'], name="micro_biomass_meth", curie=MIXS.curie('0000339'),
                   model_uri=NMDC_DH.micro_biomass_meth, domain=None, range=Optional[str])

slots.microbial_biomass = Slot(uri=MIXS['0000650'], name="microbial_biomass", curie=MIXS.curie('0000650'),
                   model_uri=NMDC_DH.microbial_biomass, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.misc_param = Slot(uri=MIXS['0000752'], name="misc_param", curie=MIXS.curie('0000752'),
                   model_uri=NMDC_DH.misc_param, domain=None, range=Optional[Union[str, List[str]]])

slots.org_matter = Slot(uri=MIXS['0000204'], name="org_matter", curie=MIXS.curie('0000204'),
                   model_uri=NMDC_DH.org_matter, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.org_nitro = Slot(uri=MIXS['0000205'], name="org_nitro", curie=MIXS.curie('0000205'),
                   model_uri=NMDC_DH.org_nitro, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.oxy_stat_samp = Slot(uri=MIXS['0000753'], name="oxy_stat_samp", curie=MIXS.curie('0000753'),
                   model_uri=NMDC_DH.oxy_stat_samp, domain=None, range=Optional[Union[str, "OxyStatSampEnum"]])

slots.ph = Slot(uri=MIXS['0001001'], name="ph", curie=MIXS.curie('0001001'),
                   model_uri=NMDC_DH.ph, domain=None, range=Optional[float])

slots.ph_meth = Slot(uri=MIXS['0001106'], name="ph_meth", curie=MIXS.curie('0001106'),
                   model_uri=NMDC_DH.ph_meth, domain=None, range=Optional[str])

slots.phosphate = Slot(uri=MIXS['0000505'], name="phosphate", curie=MIXS.curie('0000505'),
                   model_uri=NMDC_DH.phosphate, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.prev_land_use_meth = Slot(uri=MIXS['0000316'], name="prev_land_use_meth", curie=MIXS.curie('0000316'),
                   model_uri=NMDC_DH.prev_land_use_meth, domain=None, range=Optional[str])

slots.previous_land_use = Slot(uri=MIXS['0000315'], name="previous_land_use", curie=MIXS.curie('0000315'),
                   model_uri=NMDC_DH.previous_land_use, domain=None, range=Optional[str])

slots.profile_position = Slot(uri=MIXS['0001084'], name="profile_position", curie=MIXS.curie('0001084'),
                   model_uri=NMDC_DH.profile_position, domain=None, range=Optional[Union[str, "ProfilePositionEnum"]])

slots.rel_to_oxygen = Slot(uri=MIXS['0000015'], name="rel_to_oxygen", curie=MIXS.curie('0000015'),
                   model_uri=NMDC_DH.rel_to_oxygen, domain=None, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.salinity = Slot(uri=MIXS['0000183'], name="salinity", curie=MIXS.curie('0000183'),
                   model_uri=NMDC_DH.salinity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.salinity_meth = Slot(uri=MIXS['0000341'], name="salinity_meth", curie=MIXS.curie('0000341'),
                   model_uri=NMDC_DH.salinity_meth, domain=None, range=Optional[str])

slots.samp_collec_device = Slot(uri=MIXS['0000002'], name="samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=NMDC_DH.samp_collec_device, domain=None, range=Optional[str])

slots.samp_collec_method = Slot(uri=MIXS['0001225'], name="samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=NMDC_DH.samp_collec_method, domain=None, range=Optional[str])

slots.samp_mat_process = Slot(uri=MIXS['0000016'], name="samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=NMDC_DH.samp_mat_process, domain=None, range=Optional[str])

slots.samp_name = Slot(uri=MIXS['0001107'], name="samp_name", curie=MIXS.curie('0001107'),
                   model_uri=NMDC_DH.samp_name, domain=None, range=str)

slots.samp_size = Slot(uri=MIXS['0000001'], name="samp_size", curie=MIXS.curie('0000001'),
                   model_uri=NMDC_DH.samp_size, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.samp_store_temp = Slot(uri=MIXS['0000110'], name="samp_store_temp", curie=MIXS.curie('0000110'),
                   model_uri=NMDC_DH.samp_store_temp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.season_precpt = Slot(uri=MIXS['0000645'], name="season_precpt", curie=MIXS.curie('0000645'),
                   model_uri=NMDC_DH.season_precpt, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.season_temp = Slot(uri=MIXS['0000643'], name="season_temp", curie=MIXS.curie('0000643'),
                   model_uri=NMDC_DH.season_temp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.sieving = Slot(uri=MIXS['0000322'], name="sieving", curie=MIXS.curie('0000322'),
                   model_uri=NMDC_DH.sieving, domain=None, range=Optional[str])

slots.size_frac_low = Slot(uri=MIXS['0000735'], name="size_frac_low", curie=MIXS.curie('0000735'),
                   model_uri=NMDC_DH.size_frac_low, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.size_frac_up = Slot(uri=MIXS['0000736'], name="size_frac_up", curie=MIXS.curie('0000736'),
                   model_uri=NMDC_DH.size_frac_up, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.slope_aspect = Slot(uri=MIXS['0000647'], name="slope_aspect", curie=MIXS.curie('0000647'),
                   model_uri=NMDC_DH.slope_aspect, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.slope_gradient = Slot(uri=MIXS['0000646'], name="slope_gradient", curie=MIXS.curie('0000646'),
                   model_uri=NMDC_DH.slope_gradient, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.soil_horizon = Slot(uri=MIXS['0001082'], name="soil_horizon", curie=MIXS.curie('0001082'),
                   model_uri=NMDC_DH.soil_horizon, domain=None, range=Optional[Union[str, "SoilHorizonEnum"]])

slots.soil_text_measure = Slot(uri=MIXS['0000335'], name="soil_text_measure", curie=MIXS.curie('0000335'),
                   model_uri=NMDC_DH.soil_text_measure, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.soil_texture_meth = Slot(uri=MIXS['0000336'], name="soil_texture_meth", curie=MIXS.curie('0000336'),
                   model_uri=NMDC_DH.soil_texture_meth, domain=None, range=Optional[str])

slots.soil_type = Slot(uri=MIXS['0000332'], name="soil_type", curie=MIXS.curie('0000332'),
                   model_uri=NMDC_DH.soil_type, domain=None, range=Optional[str])

slots.soil_type_meth = Slot(uri=MIXS['0000334'], name="soil_type_meth", curie=MIXS.curie('0000334'),
                   model_uri=NMDC_DH.soil_type_meth, domain=None, range=Optional[str])

slots.source_mat_id = Slot(uri=MIXS['0000026'], name="source_mat_id", curie=MIXS.curie('0000026'),
                   model_uri=NMDC_DH.source_mat_id, domain=None, range=Optional[str])

slots.store_cond = Slot(uri=MIXS['0000327'], name="store_cond", curie=MIXS.curie('0000327'),
                   model_uri=NMDC_DH.store_cond, domain=None, range=Optional[str])

slots.temp = Slot(uri=MIXS['0000113'], name="temp", curie=MIXS.curie('0000113'),
                   model_uri=NMDC_DH.temp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.tillage = Slot(uri=MIXS['0001081'], name="tillage", curie=MIXS.curie('0001081'),
                   model_uri=NMDC_DH.tillage, domain=None, range=Optional[Union[Union[str, "TillageEnum"], List[Union[str, "TillageEnum"]]]])

slots.tot_carb = Slot(uri=MIXS['0000525'], name="tot_carb", curie=MIXS.curie('0000525'),
                   model_uri=NMDC_DH.tot_carb, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.tot_nitro_cont_meth = Slot(uri=MIXS['0000338'], name="tot_nitro_cont_meth", curie=MIXS.curie('0000338'),
                   model_uri=NMDC_DH.tot_nitro_cont_meth, domain=None, range=Optional[str])

slots.tot_nitro_content = Slot(uri=MIXS['0000530'], name="tot_nitro_content", curie=MIXS.curie('0000530'),
                   model_uri=NMDC_DH.tot_nitro_content, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.tot_org_c_meth = Slot(uri=MIXS['0000337'], name="tot_org_c_meth", curie=MIXS.curie('0000337'),
                   model_uri=NMDC_DH.tot_org_c_meth, domain=None, range=Optional[str])

slots.tot_org_carb = Slot(uri=MIXS['0000533'], name="tot_org_carb", curie=MIXS.curie('0000533'),
                   model_uri=NMDC_DH.tot_org_carb, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.tot_phosp = Slot(uri=MIXS['0000117'], name="tot_phosp", curie=MIXS.curie('0000117'),
                   model_uri=NMDC_DH.tot_phosp, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.water_cont_soil_meth = Slot(uri=MIXS['0000323'], name="water_cont_soil_meth", curie=MIXS.curie('0000323'),
                   model_uri=NMDC_DH.water_cont_soil_meth, domain=None, range=Optional[str])

slots.water_content = Slot(uri=MIXS['0000185'], name="water_content", curie=MIXS.curie('0000185'),
                   model_uri=NMDC_DH.water_content, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.watering_regm = Slot(uri=MIXS['0000591'], name="watering_regm", curie=MIXS.curie('0000591'),
                   model_uri=NMDC_DH.watering_regm, domain=None, range=Optional[Union[str, List[str]]])

slots.soil_emsl_jgi_mg_project_ID = Slot(uri=NMDC_DH.project_ID, name="soil_emsl_jgi_mg_project_ID", curie=NMDC_DH.curie('project_ID'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_project_ID, domain=SoilEmslJgiMg, range=str)

slots.soil_emsl_jgi_mg_sample_type = Slot(uri=NMDC_DH.sample_type, name="soil_emsl_jgi_mg_sample_type", curie=NMDC_DH.curie('sample_type'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_sample_type, domain=SoilEmslJgiMg, range=Union[str, "SampleTypeEnum"])

slots.soil_emsl_jgi_mg_sample_shipped = Slot(uri=NMDC_DH.sample_shipped, name="soil_emsl_jgi_mg_sample_shipped", curie=NMDC_DH.curie('sample_shipped'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_sample_shipped, domain=SoilEmslJgiMg, range=str)

slots.soil_emsl_jgi_mg_EMSL_store_temp = Slot(uri=NMDC_DH.EMSL_store_temp, name="soil_emsl_jgi_mg_EMSL_store_temp", curie=NMDC_DH.curie('EMSL_store_temp'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_EMSL_store_temp, domain=SoilEmslJgiMg, range=str)

slots.soil_emsl_jgi_mg_technical_reps = Slot(uri=NMDC_DH.technical_reps, name="soil_emsl_jgi_mg_technical_reps", curie=NMDC_DH.curie('technical_reps'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_technical_reps, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_replicate_number = Slot(uri=NMDC_DH.replicate_number, name="soil_emsl_jgi_mg_replicate_number", curie=NMDC_DH.curie('replicate_number'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_replicate_number, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_dna_seq_project = Slot(uri=NMDC_DH.dna_seq_project, name="soil_emsl_jgi_mg_dna_seq_project", curie=NMDC_DH.curie('dna_seq_project'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_dna_seq_project, domain=SoilEmslJgiMg, range=str)

slots.soil_emsl_jgi_mg_dna_seq_project_name = Slot(uri=NMDC_DH.dna_seq_project_name, name="soil_emsl_jgi_mg_dna_seq_project_name", curie=NMDC_DH.curie('dna_seq_project_name'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_dna_seq_project_name, domain=SoilEmslJgiMg, range=str)

slots.soil_emsl_jgi_mg_dna_samp_ID = Slot(uri=NMDC_DH.dna_samp_ID, name="soil_emsl_jgi_mg_dna_samp_ID", curie=NMDC_DH.curie('dna_samp_ID'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_dna_samp_ID, domain=SoilEmslJgiMg, range=str)

slots.soil_emsl_jgi_mg_dna_sample_name = Slot(uri=NMDC_DH.dna_sample_name, name="soil_emsl_jgi_mg_dna_sample_name", curie=NMDC_DH.curie('dna_sample_name'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_dna_sample_name, domain=SoilEmslJgiMg, range=str)

slots.soil_emsl_jgi_mg_dna_concentration = Slot(uri=NMDC_DH.dna_concentration, name="soil_emsl_jgi_mg_dna_concentration", curie=NMDC_DH.curie('dna_concentration'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_dna_concentration, domain=SoilEmslJgiMg, range=str)

slots.soil_emsl_jgi_mg_dna_volume = Slot(uri=NMDC_DH.dna_volume, name="soil_emsl_jgi_mg_dna_volume", curie=NMDC_DH.curie('dna_volume'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_dna_volume, domain=SoilEmslJgiMg, range=str)

slots.soil_emsl_jgi_mg_dna_absorb1 = Slot(uri=NMDC_DH.dna_absorb1, name="soil_emsl_jgi_mg_dna_absorb1", curie=NMDC_DH.curie('dna_absorb1'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_dna_absorb1, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_dna_absorb2 = Slot(uri=NMDC_DH.dna_absorb2, name="soil_emsl_jgi_mg_dna_absorb2", curie=NMDC_DH.curie('dna_absorb2'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_dna_absorb2, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_dna_container_ID = Slot(uri=NMDC_DH.dna_container_ID, name="soil_emsl_jgi_mg_dna_container_ID", curie=NMDC_DH.curie('dna_container_ID'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_dna_container_ID, domain=SoilEmslJgiMg, range=str)

slots.soil_emsl_jgi_mg_dna_cont_type = Slot(uri=NMDC_DH.dna_cont_type, name="soil_emsl_jgi_mg_dna_cont_type", curie=NMDC_DH.curie('dna_cont_type'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_dna_cont_type, domain=SoilEmslJgiMg, range=Union[str, "DnaContTypeEnum"])

slots.soil_emsl_jgi_mg_dna_cont_well = Slot(uri=NMDC_DH.dna_cont_well, name="soil_emsl_jgi_mg_dna_cont_well", curie=NMDC_DH.curie('dna_cont_well'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_dna_cont_well, domain=SoilEmslJgiMg, range=str)

slots.soil_emsl_jgi_mg_dna_sample_format = Slot(uri=NMDC_DH.dna_sample_format, name="soil_emsl_jgi_mg_dna_sample_format", curie=NMDC_DH.curie('dna_sample_format'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_dna_sample_format, domain=SoilEmslJgiMg, range=Union[str, "DnaSampleFormatEnum"])

slots.soil_emsl_jgi_mg_dna_dnase = Slot(uri=NMDC_DH.dna_dnase, name="soil_emsl_jgi_mg_dna_dnase", curie=NMDC_DH.curie('dna_dnase'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_dna_dnase, domain=SoilEmslJgiMg, range=Union[str, "DnaDnaseEnum"])

slots.soil_emsl_jgi_mg_dna_organisms = Slot(uri=NMDC_DH.dna_organisms, name="soil_emsl_jgi_mg_dna_organisms", curie=NMDC_DH.curie('dna_organisms'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_dna_organisms, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_dna_collect_site = Slot(uri=NMDC_DH.dna_collect_site, name="soil_emsl_jgi_mg_dna_collect_site", curie=NMDC_DH.curie('dna_collect_site'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_dna_collect_site, domain=SoilEmslJgiMg, range=str)

slots.soil_emsl_jgi_mg_dna_isolate_meth = Slot(uri=NMDC_DH.dna_isolate_meth, name="soil_emsl_jgi_mg_dna_isolate_meth", curie=NMDC_DH.curie('dna_isolate_meth'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_dna_isolate_meth, domain=SoilEmslJgiMg, range=str)

slots.soil_emsl_jgi_mg_dna_seq_project_PI = Slot(uri=NMDC_DH.dna_seq_project_PI, name="soil_emsl_jgi_mg_dna_seq_project_PI", curie=NMDC_DH.curie('dna_seq_project_PI'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_dna_seq_project_PI, domain=SoilEmslJgiMg, range=str)

slots.soil_emsl_jgi_mg_dna_project_contact = Slot(uri=NMDC_DH.dna_project_contact, name="soil_emsl_jgi_mg_dna_project_contact", curie=NMDC_DH.curie('dna_project_contact'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_dna_project_contact, domain=SoilEmslJgiMg, range=str)

slots.soil_emsl_jgi_mg_proposal_dna = Slot(uri=NMDC_DH.proposal_dna, name="soil_emsl_jgi_mg_proposal_dna", curie=NMDC_DH.curie('proposal_dna'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_proposal_dna, domain=SoilEmslJgiMg, range=str)

slots.soil_emsl_jgi_mg_collection_time = Slot(uri=NMDC_DH.collection_time, name="soil_emsl_jgi_mg_collection_time", curie=NMDC_DH.curie('collection_time'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_collection_time, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_collection_date_inc = Slot(uri=NMDC_DH.collection_date_inc, name="soil_emsl_jgi_mg_collection_date_inc", curie=NMDC_DH.curie('collection_date_inc'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_collection_date_inc, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_collection_time_inc = Slot(uri=NMDC_DH.collection_time_inc, name="soil_emsl_jgi_mg_collection_time_inc", curie=NMDC_DH.curie('collection_time_inc'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_collection_time_inc, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_start_date_inc = Slot(uri=NMDC_DH.start_date_inc, name="soil_emsl_jgi_mg_start_date_inc", curie=NMDC_DH.curie('start_date_inc'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_start_date_inc, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_start_time_inc = Slot(uri=NMDC_DH.start_time_inc, name="soil_emsl_jgi_mg_start_time_inc", curie=NMDC_DH.curie('start_time_inc'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_start_time_inc, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_filter_method = Slot(uri=NMDC_DH.filter_method, name="soil_emsl_jgi_mg_filter_method", curie=NMDC_DH.curie('filter_method'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_filter_method, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_experimental_factor_other = Slot(uri=NMDC_DH.experimental_factor_other, name="soil_emsl_jgi_mg_experimental_factor_other", curie=NMDC_DH.curie('experimental_factor_other'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_experimental_factor_other, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_non_microb_biomass = Slot(uri=NMDC_DH.non_microb_biomass, name="soil_emsl_jgi_mg_non_microb_biomass", curie=NMDC_DH.curie('non_microb_biomass'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_non_microb_biomass, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_non_microb_biomass_method = Slot(uri=NMDC_DH.non_microb_biomass_method, name="soil_emsl_jgi_mg_non_microb_biomass_method", curie=NMDC_DH.curie('non_microb_biomass_method'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_non_microb_biomass_method, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_microbial_biomass_C = Slot(uri=NMDC_DH.microbial_biomass_C, name="soil_emsl_jgi_mg_microbial_biomass_C", curie=NMDC_DH.curie('microbial_biomass_C'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_microbial_biomass_C, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_micro_biomass_C_meth = Slot(uri=NMDC_DH.micro_biomass_C_meth, name="soil_emsl_jgi_mg_micro_biomass_C_meth", curie=NMDC_DH.curie('micro_biomass_C_meth'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_micro_biomass_C_meth, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_microbial_biomass_N = Slot(uri=NMDC_DH.microbial_biomass_N, name="soil_emsl_jgi_mg_microbial_biomass_N", curie=NMDC_DH.curie('microbial_biomass_N'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_microbial_biomass_N, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_micro_biomass_N_meth = Slot(uri=NMDC_DH.micro_biomass_N_meth, name="soil_emsl_jgi_mg_micro_biomass_N_meth", curie=NMDC_DH.curie('micro_biomass_N_meth'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_micro_biomass_N_meth, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_org_nitro_method = Slot(uri=NMDC_DH.org_nitro_method, name="soil_emsl_jgi_mg_org_nitro_method", curie=NMDC_DH.curie('org_nitro_method'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_org_nitro_method, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_other_treatment = Slot(uri=NMDC_DH.other_treatment, name="soil_emsl_jgi_mg_other_treatment", curie=NMDC_DH.curie('other_treatment'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_other_treatment, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_isotope_exposure = Slot(uri=NMDC_DH.isotope_exposure, name="soil_emsl_jgi_mg_isotope_exposure", curie=NMDC_DH.curie('isotope_exposure'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_isotope_exposure, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_analysis_type = Slot(uri=NMDC_DH.analysis_type, name="soil_emsl_jgi_mg_analysis_type", curie=NMDC_DH.curie('analysis_type'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_analysis_type, domain=SoilEmslJgiMg, range=Union[Union[str, "AnalysisTypeEnum"], List[Union[str, "AnalysisTypeEnum"]]])

slots.soil_emsl_jgi_mg_env_package = Slot(uri=NMDC_DH.env_package, name="soil_emsl_jgi_mg_env_package", curie=NMDC_DH.curie('env_package'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_env_package, domain=SoilEmslJgiMg, range=Union[str, "EnvPackageEnum"])

slots.soil_emsl_jgi_mg_sample_link = Slot(uri=NMDC_DH.sample_link, name="soil_emsl_jgi_mg_sample_link", curie=NMDC_DH.curie('sample_link'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_sample_link, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_ecosystem = Slot(uri="str(uriorcurie)", name="soil_emsl_jgi_mg_ecosystem", curie=None,
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_ecosystem, domain=SoilEmslJgiMg, range=Union[str, "EcosystemEnum"])

slots.soil_emsl_jgi_mg_ecosystem_category = Slot(uri="str(uriorcurie)", name="soil_emsl_jgi_mg_ecosystem_category", curie=None,
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_ecosystem_category, domain=SoilEmslJgiMg, range=Union[str, "EcosystemCategoryEnum"])

slots.soil_emsl_jgi_mg_ecosystem_subtype = Slot(uri="str(uriorcurie)", name="soil_emsl_jgi_mg_ecosystem_subtype", curie=None,
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_ecosystem_subtype, domain=SoilEmslJgiMg, range=Union[str, "EcosystemSubtypeEnum"])

slots.soil_emsl_jgi_mg_ecosystem_type = Slot(uri="str(uriorcurie)", name="soil_emsl_jgi_mg_ecosystem_type", curie=None,
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_ecosystem_type, domain=SoilEmslJgiMg, range=Union[str, "EcosystemTypeEnum"])

slots.soil_emsl_jgi_mg_specific_ecosystem = Slot(uri="str(uriorcurie)", name="soil_emsl_jgi_mg_specific_ecosystem", curie=None,
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_specific_ecosystem, domain=SoilEmslJgiMg, range=Union[str, "SpecificEcosystemEnum"])

slots.soil_emsl_jgi_mg_agrochem_addition = Slot(uri=MIXS['0000639'], name="soil_emsl_jgi_mg_agrochem_addition", curie=MIXS.curie('0000639'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_agrochem_addition, domain=SoilEmslJgiMg, range=Optional[Union[str, List[str]]])

slots.soil_emsl_jgi_mg_air_temp_regm = Slot(uri=MIXS['0000551'], name="soil_emsl_jgi_mg_air_temp_regm", curie=MIXS.curie('0000551'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_air_temp_regm, domain=SoilEmslJgiMg, range=Optional[Union[str, List[str]]])

slots.soil_emsl_jgi_mg_al_sat = Slot(uri=MIXS['0000607'], name="soil_emsl_jgi_mg_al_sat", curie=MIXS.curie('0000607'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_al_sat, domain=SoilEmslJgiMg, range=Optional[Union[dict, "QuantityValue"]])

slots.soil_emsl_jgi_mg_al_sat_meth = Slot(uri=MIXS['0000324'], name="soil_emsl_jgi_mg_al_sat_meth", curie=MIXS.curie('0000324'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_al_sat_meth, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_alt = Slot(uri=MIXS['0000094'], name="soil_emsl_jgi_mg_alt", curie=MIXS.curie('0000094'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_alt, domain=SoilEmslJgiMg, range=Optional[Union[dict, "QuantityValue"]])

slots.soil_emsl_jgi_mg_annual_precpt = Slot(uri=MIXS['0000644'], name="soil_emsl_jgi_mg_annual_precpt", curie=MIXS.curie('0000644'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_annual_precpt, domain=SoilEmslJgiMg, range=Optional[Union[dict, "QuantityValue"]])

slots.soil_emsl_jgi_mg_annual_temp = Slot(uri=MIXS['0000642'], name="soil_emsl_jgi_mg_annual_temp", curie=MIXS.curie('0000642'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_annual_temp, domain=SoilEmslJgiMg, range=Optional[Union[dict, "QuantityValue"]])

slots.soil_emsl_jgi_mg_biotic_regm = Slot(uri=MIXS['0001038'], name="soil_emsl_jgi_mg_biotic_regm", curie=MIXS.curie('0001038'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_biotic_regm, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_biotic_relationship = Slot(uri=MIXS['0000028'], name="soil_emsl_jgi_mg_biotic_relationship", curie=MIXS.curie('0000028'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_biotic_relationship, domain=SoilEmslJgiMg, range=Optional[Union[str, "BioticRelationshipEnum"]])

slots.soil_emsl_jgi_mg_carb_nitro_ratio = Slot(uri=MIXS['0000310'], name="soil_emsl_jgi_mg_carb_nitro_ratio", curie=MIXS.curie('0000310'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_carb_nitro_ratio, domain=SoilEmslJgiMg, range=Optional[Union[dict, "QuantityValue"]])

slots.soil_emsl_jgi_mg_chem_administration = Slot(uri=MIXS['0000751'], name="soil_emsl_jgi_mg_chem_administration", curie=MIXS.curie('0000751'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_chem_administration, domain=SoilEmslJgiMg, range=Optional[Union[str, List[str]]])

slots.soil_emsl_jgi_mg_climate_environment = Slot(uri=MIXS['0001040'], name="soil_emsl_jgi_mg_climate_environment", curie=MIXS.curie('0001040'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_climate_environment, domain=SoilEmslJgiMg, range=Optional[Union[str, List[str]]])

slots.soil_emsl_jgi_mg_collection_date = Slot(uri=MIXS['0000011'], name="soil_emsl_jgi_mg_collection_date", curie=MIXS.curie('0000011'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_collection_date, domain=SoilEmslJgiMg, range=str)

slots.soil_emsl_jgi_mg_crop_rotation = Slot(uri=MIXS['0000318'], name="soil_emsl_jgi_mg_crop_rotation", curie=MIXS.curie('0000318'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_crop_rotation, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_cur_land_use = Slot(uri=MIXS['0001080'], name="soil_emsl_jgi_mg_cur_land_use", curie=MIXS.curie('0001080'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_cur_land_use, domain=SoilEmslJgiMg, range=Optional[Union[str, "CurLandUseEnum"]])

slots.soil_emsl_jgi_mg_cur_vegetation = Slot(uri=MIXS['0000312'], name="soil_emsl_jgi_mg_cur_vegetation", curie=MIXS.curie('0000312'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_cur_vegetation, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_cur_vegetation_meth = Slot(uri=MIXS['0000314'], name="soil_emsl_jgi_mg_cur_vegetation_meth", curie=MIXS.curie('0000314'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_cur_vegetation_meth, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_depth = Slot(uri=MIXS['0000018'], name="soil_emsl_jgi_mg_depth", curie=MIXS.curie('0000018'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_depth, domain=SoilEmslJgiMg, range=str)

slots.soil_emsl_jgi_mg_drainage_class = Slot(uri=MIXS['0001085'], name="soil_emsl_jgi_mg_drainage_class", curie=MIXS.curie('0001085'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_drainage_class, domain=SoilEmslJgiMg, range=Optional[Union[str, "DrainageClassEnum"]])

slots.soil_emsl_jgi_mg_elev = Slot(uri=MIXS['0000093'], name="soil_emsl_jgi_mg_elev", curie=MIXS.curie('0000093'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_elev, domain=SoilEmslJgiMg, range=Union[dict, "QuantityValue"])

slots.soil_emsl_jgi_mg_env_broad_scale = Slot(uri=MIXS['0000012'], name="soil_emsl_jgi_mg_env_broad_scale", curie=MIXS.curie('0000012'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_env_broad_scale, domain=SoilEmslJgiMg, range=str)

slots.soil_emsl_jgi_mg_env_local_scale = Slot(uri=MIXS['0000013'], name="soil_emsl_jgi_mg_env_local_scale", curie=MIXS.curie('0000013'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_env_local_scale, domain=SoilEmslJgiMg, range=str)

slots.soil_emsl_jgi_mg_env_medium = Slot(uri=MIXS['0000014'], name="soil_emsl_jgi_mg_env_medium", curie=MIXS.curie('0000014'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_env_medium, domain=SoilEmslJgiMg, range=str)

slots.soil_emsl_jgi_mg_experimental_factor = Slot(uri=MIXS['0000008'], name="soil_emsl_jgi_mg_experimental_factor", curie=MIXS.curie('0000008'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_experimental_factor, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_extreme_event = Slot(uri=MIXS['0000320'], name="soil_emsl_jgi_mg_extreme_event", curie=MIXS.curie('0000320'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_extreme_event, domain=SoilEmslJgiMg, range=Optional[Union[str, XSDDate]])

slots.soil_emsl_jgi_mg_fao_class = Slot(uri=MIXS['0001083'], name="soil_emsl_jgi_mg_fao_class", curie=MIXS.curie('0001083'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_fao_class, domain=SoilEmslJgiMg, range=Optional[Union[str, "FaoClassEnum"]])

slots.soil_emsl_jgi_mg_fire = Slot(uri=MIXS['0001086'], name="soil_emsl_jgi_mg_fire", curie=MIXS.curie('0001086'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_fire, domain=SoilEmslJgiMg, range=Optional[Union[str, XSDDate]])

slots.soil_emsl_jgi_mg_flooding = Slot(uri=MIXS['0000319'], name="soil_emsl_jgi_mg_flooding", curie=MIXS.curie('0000319'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_flooding, domain=SoilEmslJgiMg, range=Optional[Union[str, XSDDate]])

slots.soil_emsl_jgi_mg_gaseous_environment = Slot(uri=MIXS['0000558'], name="soil_emsl_jgi_mg_gaseous_environment", curie=MIXS.curie('0000558'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_gaseous_environment, domain=SoilEmslJgiMg, range=Optional[Union[str, List[str]]])

slots.soil_emsl_jgi_mg_geo_loc_name = Slot(uri=MIXS['0000010'], name="soil_emsl_jgi_mg_geo_loc_name", curie=MIXS.curie('0000010'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_geo_loc_name, domain=SoilEmslJgiMg, range=str)

slots.soil_emsl_jgi_mg_growth_facil = Slot(uri=MIXS['0001043'], name="soil_emsl_jgi_mg_growth_facil", curie=MIXS.curie('0001043'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_growth_facil, domain=SoilEmslJgiMg, range=Union[str, "GrowthFacilEnum"])

slots.soil_emsl_jgi_mg_heavy_metals = Slot(uri=MIXS['0000652'], name="soil_emsl_jgi_mg_heavy_metals", curie=MIXS.curie('0000652'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_heavy_metals, domain=SoilEmslJgiMg, range=Optional[Union[str, List[str]]])

slots.soil_emsl_jgi_mg_heavy_metals_meth = Slot(uri=MIXS['0000343'], name="soil_emsl_jgi_mg_heavy_metals_meth", curie=MIXS.curie('0000343'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_heavy_metals_meth, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_horizon_meth = Slot(uri=MIXS['0000321'], name="soil_emsl_jgi_mg_horizon_meth", curie=MIXS.curie('0000321'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_horizon_meth, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_humidity_regm = Slot(uri=MIXS['0000568'], name="soil_emsl_jgi_mg_humidity_regm", curie=MIXS.curie('0000568'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_humidity_regm, domain=SoilEmslJgiMg, range=Optional[Union[str, List[str]]])

slots.soil_emsl_jgi_mg_lat_lon = Slot(uri=MIXS['0000009'], name="soil_emsl_jgi_mg_lat_lon", curie=MIXS.curie('0000009'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_lat_lon, domain=SoilEmslJgiMg, range=str)

slots.soil_emsl_jgi_mg_light_regm = Slot(uri=MIXS['0000569'], name="soil_emsl_jgi_mg_light_regm", curie=MIXS.curie('0000569'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_light_regm, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_link_class_info = Slot(uri=MIXS['0000329'], name="soil_emsl_jgi_mg_link_class_info", curie=MIXS.curie('0000329'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_link_class_info, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_link_climate_info = Slot(uri=MIXS['0000328'], name="soil_emsl_jgi_mg_link_climate_info", curie=MIXS.curie('0000328'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_link_climate_info, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_local_class = Slot(uri=MIXS['0000330'], name="soil_emsl_jgi_mg_local_class", curie=MIXS.curie('0000330'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_local_class, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_local_class_meth = Slot(uri=MIXS['0000331'], name="soil_emsl_jgi_mg_local_class_meth", curie=MIXS.curie('0000331'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_local_class_meth, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_micro_biomass_meth = Slot(uri=MIXS['0000339'], name="soil_emsl_jgi_mg_micro_biomass_meth", curie=MIXS.curie('0000339'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_micro_biomass_meth, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_microbial_biomass = Slot(uri=MIXS['0000650'], name="soil_emsl_jgi_mg_microbial_biomass", curie=MIXS.curie('0000650'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_microbial_biomass, domain=SoilEmslJgiMg, range=Optional[Union[dict, "QuantityValue"]])

slots.soil_emsl_jgi_mg_misc_param = Slot(uri=MIXS['0000752'], name="soil_emsl_jgi_mg_misc_param", curie=MIXS.curie('0000752'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_misc_param, domain=SoilEmslJgiMg, range=Optional[Union[str, List[str]]])

slots.soil_emsl_jgi_mg_org_matter = Slot(uri=MIXS['0000204'], name="soil_emsl_jgi_mg_org_matter", curie=MIXS.curie('0000204'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_org_matter, domain=SoilEmslJgiMg, range=Optional[Union[dict, "QuantityValue"]])

slots.soil_emsl_jgi_mg_org_nitro = Slot(uri=MIXS['0000205'], name="soil_emsl_jgi_mg_org_nitro", curie=MIXS.curie('0000205'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_org_nitro, domain=SoilEmslJgiMg, range=Optional[Union[dict, "QuantityValue"]])

slots.soil_emsl_jgi_mg_oxy_stat_samp = Slot(uri=MIXS['0000753'], name="soil_emsl_jgi_mg_oxy_stat_samp", curie=MIXS.curie('0000753'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_oxy_stat_samp, domain=SoilEmslJgiMg, range=Optional[Union[str, "OxyStatSampEnum"]])

slots.soil_emsl_jgi_mg_ph = Slot(uri=MIXS['0001001'], name="soil_emsl_jgi_mg_ph", curie=MIXS.curie('0001001'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_ph, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_ph_meth = Slot(uri=MIXS['0001106'], name="soil_emsl_jgi_mg_ph_meth", curie=MIXS.curie('0001106'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_ph_meth, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_phosphate = Slot(uri=MIXS['0000505'], name="soil_emsl_jgi_mg_phosphate", curie=MIXS.curie('0000505'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_phosphate, domain=SoilEmslJgiMg, range=Optional[Union[dict, "QuantityValue"]])

slots.soil_emsl_jgi_mg_prev_land_use_meth = Slot(uri=MIXS['0000316'], name="soil_emsl_jgi_mg_prev_land_use_meth", curie=MIXS.curie('0000316'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_prev_land_use_meth, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_previous_land_use = Slot(uri=MIXS['0000315'], name="soil_emsl_jgi_mg_previous_land_use", curie=MIXS.curie('0000315'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_previous_land_use, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_profile_position = Slot(uri=MIXS['0001084'], name="soil_emsl_jgi_mg_profile_position", curie=MIXS.curie('0001084'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_profile_position, domain=SoilEmslJgiMg, range=Optional[Union[str, "ProfilePositionEnum"]])

slots.soil_emsl_jgi_mg_rel_to_oxygen = Slot(uri=MIXS['0000015'], name="soil_emsl_jgi_mg_rel_to_oxygen", curie=MIXS.curie('0000015'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_rel_to_oxygen, domain=SoilEmslJgiMg, range=Optional[Union[str, "RelToOxygenEnum"]])

slots.soil_emsl_jgi_mg_salinity = Slot(uri=MIXS['0000183'], name="soil_emsl_jgi_mg_salinity", curie=MIXS.curie('0000183'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_salinity, domain=SoilEmslJgiMg, range=Optional[Union[dict, "QuantityValue"]])

slots.soil_emsl_jgi_mg_salinity_meth = Slot(uri=MIXS['0000341'], name="soil_emsl_jgi_mg_salinity_meth", curie=MIXS.curie('0000341'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_salinity_meth, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_samp_collec_device = Slot(uri=MIXS['0000002'], name="soil_emsl_jgi_mg_samp_collec_device", curie=MIXS.curie('0000002'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_samp_collec_device, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_samp_collec_method = Slot(uri=MIXS['0001225'], name="soil_emsl_jgi_mg_samp_collec_method", curie=MIXS.curie('0001225'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_samp_collec_method, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_samp_mat_process = Slot(uri=MIXS['0000016'], name="soil_emsl_jgi_mg_samp_mat_process", curie=MIXS.curie('0000016'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_samp_mat_process, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_samp_name = Slot(uri=MIXS['0001107'], name="soil_emsl_jgi_mg_samp_name", curie=MIXS.curie('0001107'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_samp_name, domain=SoilEmslJgiMg, range=str)

slots.soil_emsl_jgi_mg_samp_size = Slot(uri=MIXS['0000001'], name="soil_emsl_jgi_mg_samp_size", curie=MIXS.curie('0000001'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_samp_size, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_samp_store_temp = Slot(uri=MIXS['0000110'], name="soil_emsl_jgi_mg_samp_store_temp", curie=MIXS.curie('0000110'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_samp_store_temp, domain=SoilEmslJgiMg, range=Union[dict, "QuantityValue"])

slots.soil_emsl_jgi_mg_season_precpt = Slot(uri=MIXS['0000645'], name="soil_emsl_jgi_mg_season_precpt", curie=MIXS.curie('0000645'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_season_precpt, domain=SoilEmslJgiMg, range=Optional[Union[dict, "QuantityValue"]])

slots.soil_emsl_jgi_mg_season_temp = Slot(uri=MIXS['0000643'], name="soil_emsl_jgi_mg_season_temp", curie=MIXS.curie('0000643'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_season_temp, domain=SoilEmslJgiMg, range=Optional[Union[dict, "QuantityValue"]])

slots.soil_emsl_jgi_mg_sieving = Slot(uri=MIXS['0000322'], name="soil_emsl_jgi_mg_sieving", curie=MIXS.curie('0000322'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_sieving, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_size_frac_low = Slot(uri=MIXS['0000735'], name="soil_emsl_jgi_mg_size_frac_low", curie=MIXS.curie('0000735'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_size_frac_low, domain=SoilEmslJgiMg, range=Optional[Union[dict, "QuantityValue"]])

slots.soil_emsl_jgi_mg_size_frac_up = Slot(uri=MIXS['0000736'], name="soil_emsl_jgi_mg_size_frac_up", curie=MIXS.curie('0000736'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_size_frac_up, domain=SoilEmslJgiMg, range=Optional[Union[dict, "QuantityValue"]])

slots.soil_emsl_jgi_mg_slope_aspect = Slot(uri=MIXS['0000647'], name="soil_emsl_jgi_mg_slope_aspect", curie=MIXS.curie('0000647'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_slope_aspect, domain=SoilEmslJgiMg, range=Optional[Union[dict, "QuantityValue"]])

slots.soil_emsl_jgi_mg_slope_gradient = Slot(uri=MIXS['0000646'], name="soil_emsl_jgi_mg_slope_gradient", curie=MIXS.curie('0000646'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_slope_gradient, domain=SoilEmslJgiMg, range=Optional[Union[dict, "QuantityValue"]])

slots.soil_emsl_jgi_mg_soil_horizon = Slot(uri=MIXS['0001082'], name="soil_emsl_jgi_mg_soil_horizon", curie=MIXS.curie('0001082'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_soil_horizon, domain=SoilEmslJgiMg, range=Optional[Union[str, "SoilHorizonEnum"]])

slots.soil_emsl_jgi_mg_soil_text_measure = Slot(uri=MIXS['0000335'], name="soil_emsl_jgi_mg_soil_text_measure", curie=MIXS.curie('0000335'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_soil_text_measure, domain=SoilEmslJgiMg, range=Optional[Union[dict, "QuantityValue"]])

slots.soil_emsl_jgi_mg_soil_texture_meth = Slot(uri=MIXS['0000336'], name="soil_emsl_jgi_mg_soil_texture_meth", curie=MIXS.curie('0000336'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_soil_texture_meth, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_soil_type = Slot(uri=MIXS['0000332'], name="soil_emsl_jgi_mg_soil_type", curie=MIXS.curie('0000332'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_soil_type, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_soil_type_meth = Slot(uri=MIXS['0000334'], name="soil_emsl_jgi_mg_soil_type_meth", curie=MIXS.curie('0000334'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_soil_type_meth, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_source_mat_id = Slot(uri=MIXS['0000026'], name="soil_emsl_jgi_mg_source_mat_id", curie=MIXS.curie('0000026'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_source_mat_id, domain=SoilEmslJgiMg, range=Union[str, SoilEmslJgiMgSourceMatId])

slots.soil_emsl_jgi_mg_store_cond = Slot(uri=MIXS['0000327'], name="soil_emsl_jgi_mg_store_cond", curie=MIXS.curie('0000327'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_store_cond, domain=SoilEmslJgiMg, range=Union[str, "StoreCondEnum"])

slots.soil_emsl_jgi_mg_temp = Slot(uri=MIXS['0000113'], name="soil_emsl_jgi_mg_temp", curie=MIXS.curie('0000113'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_temp, domain=SoilEmslJgiMg, range=Optional[Union[dict, "QuantityValue"]])

slots.soil_emsl_jgi_mg_tillage = Slot(uri=MIXS['0001081'], name="soil_emsl_jgi_mg_tillage", curie=MIXS.curie('0001081'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_tillage, domain=SoilEmslJgiMg, range=Optional[Union[Union[str, "TillageEnum"], List[Union[str, "TillageEnum"]]]])

slots.soil_emsl_jgi_mg_tot_carb = Slot(uri=MIXS['0000525'], name="soil_emsl_jgi_mg_tot_carb", curie=MIXS.curie('0000525'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_tot_carb, domain=SoilEmslJgiMg, range=Optional[Union[dict, "QuantityValue"]])

slots.soil_emsl_jgi_mg_tot_nitro_cont_meth = Slot(uri=MIXS['0000338'], name="soil_emsl_jgi_mg_tot_nitro_cont_meth", curie=MIXS.curie('0000338'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_tot_nitro_cont_meth, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_tot_nitro_content = Slot(uri=MIXS['0000530'], name="soil_emsl_jgi_mg_tot_nitro_content", curie=MIXS.curie('0000530'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_tot_nitro_content, domain=SoilEmslJgiMg, range=Optional[Union[dict, "QuantityValue"]])

slots.soil_emsl_jgi_mg_tot_org_c_meth = Slot(uri=MIXS['0000337'], name="soil_emsl_jgi_mg_tot_org_c_meth", curie=MIXS.curie('0000337'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_tot_org_c_meth, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_tot_org_carb = Slot(uri=MIXS['0000533'], name="soil_emsl_jgi_mg_tot_org_carb", curie=MIXS.curie('0000533'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_tot_org_carb, domain=SoilEmslJgiMg, range=Optional[Union[dict, "QuantityValue"]])

slots.soil_emsl_jgi_mg_tot_phosp = Slot(uri=MIXS['0000117'], name="soil_emsl_jgi_mg_tot_phosp", curie=MIXS.curie('0000117'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_tot_phosp, domain=SoilEmslJgiMg, range=Optional[Union[dict, "QuantityValue"]])

slots.soil_emsl_jgi_mg_water_cont_soil_meth = Slot(uri=MIXS['0000323'], name="soil_emsl_jgi_mg_water_cont_soil_meth", curie=MIXS.curie('0000323'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_water_cont_soil_meth, domain=SoilEmslJgiMg, range=Optional[str])

slots.soil_emsl_jgi_mg_water_content = Slot(uri=MIXS['0000185'], name="soil_emsl_jgi_mg_water_content", curie=MIXS.curie('0000185'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_water_content, domain=SoilEmslJgiMg, range=Optional[Union[dict, "QuantityValue"]])

slots.soil_emsl_jgi_mg_watering_regm = Slot(uri=MIXS['0000591'], name="soil_emsl_jgi_mg_watering_regm", curie=MIXS.curie('0000591'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mg_watering_regm, domain=SoilEmslJgiMg, range=Optional[Union[str, List[str]]])

slots.soil_emsl_jgi_mt_rna_seq_project = Slot(uri=NMDC_DH.rna_seq_project, name="soil_emsl_jgi_mt_rna_seq_project", curie=NMDC_DH.curie('rna_seq_project'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mt_rna_seq_project, domain=SoilEmslJgiMt, range=str)

slots.soil_emsl_jgi_mt_rna_seq_project_name = Slot(uri=NMDC_DH.rna_seq_project_name, name="soil_emsl_jgi_mt_rna_seq_project_name", curie=NMDC_DH.curie('rna_seq_project_name'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mt_rna_seq_project_name, domain=SoilEmslJgiMt, range=str)

slots.soil_emsl_jgi_mt_rna_samp_ID = Slot(uri=NMDC_DH.rna_samp_ID, name="soil_emsl_jgi_mt_rna_samp_ID", curie=NMDC_DH.curie('rna_samp_ID'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mt_rna_samp_ID, domain=SoilEmslJgiMt, range=str)

slots.soil_emsl_jgi_mt_rna_sample_name = Slot(uri=NMDC_DH.rna_sample_name, name="soil_emsl_jgi_mt_rna_sample_name", curie=NMDC_DH.curie('rna_sample_name'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mt_rna_sample_name, domain=SoilEmslJgiMt, range=str)

slots.soil_emsl_jgi_mt_rna_concentration = Slot(uri=NMDC_DH.rna_concentration, name="soil_emsl_jgi_mt_rna_concentration", curie=NMDC_DH.curie('rna_concentration'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mt_rna_concentration, domain=SoilEmslJgiMt, range=str)

slots.soil_emsl_jgi_mt_rna_volume = Slot(uri=NMDC_DH.rna_volume, name="soil_emsl_jgi_mt_rna_volume", curie=NMDC_DH.curie('rna_volume'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mt_rna_volume, domain=SoilEmslJgiMt, range=str)

slots.soil_emsl_jgi_mt_rna_absorb1 = Slot(uri=NMDC_DH.rna_absorb1, name="soil_emsl_jgi_mt_rna_absorb1", curie=NMDC_DH.curie('rna_absorb1'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mt_rna_absorb1, domain=SoilEmslJgiMt, range=Optional[str])

slots.soil_emsl_jgi_mt_rna_absorb2 = Slot(uri=NMDC_DH.rna_absorb2, name="soil_emsl_jgi_mt_rna_absorb2", curie=NMDC_DH.curie('rna_absorb2'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mt_rna_absorb2, domain=SoilEmslJgiMt, range=Optional[str])

slots.soil_emsl_jgi_mt_rna_container_ID = Slot(uri=NMDC_DH.rna_container_ID, name="soil_emsl_jgi_mt_rna_container_ID", curie=NMDC_DH.curie('rna_container_ID'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mt_rna_container_ID, domain=SoilEmslJgiMt, range=str)

slots.soil_emsl_jgi_mt_rna_cont_type = Slot(uri=NMDC_DH.rna_cont_type, name="soil_emsl_jgi_mt_rna_cont_type", curie=NMDC_DH.curie('rna_cont_type'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mt_rna_cont_type, domain=SoilEmslJgiMt, range=Union[str, "RnaContTypeEnum"])

slots.soil_emsl_jgi_mt_rna_cont_well = Slot(uri=NMDC_DH.rna_cont_well, name="soil_emsl_jgi_mt_rna_cont_well", curie=NMDC_DH.curie('rna_cont_well'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mt_rna_cont_well, domain=SoilEmslJgiMt, range=str)

slots.soil_emsl_jgi_mt_rna_sample_format = Slot(uri=NMDC_DH.rna_sample_format, name="soil_emsl_jgi_mt_rna_sample_format", curie=NMDC_DH.curie('rna_sample_format'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mt_rna_sample_format, domain=SoilEmslJgiMt, range=Union[str, "RnaSampleFormatEnum"])

slots.soil_emsl_jgi_mt_dnase_rna = Slot(uri=NMDC_DH.dnase_rna, name="soil_emsl_jgi_mt_dnase_rna", curie=NMDC_DH.curie('dnase_rna'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mt_dnase_rna, domain=SoilEmslJgiMt, range=Union[str, "DnaseRnaEnum"])

slots.soil_emsl_jgi_mt_rna_organisms = Slot(uri=NMDC_DH.rna_organisms, name="soil_emsl_jgi_mt_rna_organisms", curie=NMDC_DH.curie('rna_organisms'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mt_rna_organisms, domain=SoilEmslJgiMt, range=Optional[str])

slots.soil_emsl_jgi_mt_rna_collect_site = Slot(uri=NMDC_DH.rna_collect_site, name="soil_emsl_jgi_mt_rna_collect_site", curie=NMDC_DH.curie('rna_collect_site'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mt_rna_collect_site, domain=SoilEmslJgiMt, range=str)

slots.soil_emsl_jgi_mt_rna_isolate_meth = Slot(uri=NMDC_DH.rna_isolate_meth, name="soil_emsl_jgi_mt_rna_isolate_meth", curie=NMDC_DH.curie('rna_isolate_meth'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mt_rna_isolate_meth, domain=SoilEmslJgiMt, range=str)

slots.soil_emsl_jgi_mt_rna_seq_project_PI = Slot(uri=NMDC_DH.rna_seq_project_PI, name="soil_emsl_jgi_mt_rna_seq_project_PI", curie=NMDC_DH.curie('rna_seq_project_PI'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mt_rna_seq_project_PI, domain=SoilEmslJgiMt, range=str)

slots.soil_emsl_jgi_mt_rna_project_contact = Slot(uri=NMDC_DH.rna_project_contact, name="soil_emsl_jgi_mt_rna_project_contact", curie=NMDC_DH.curie('rna_project_contact'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mt_rna_project_contact, domain=SoilEmslJgiMt, range=str)

slots.soil_emsl_jgi_mt_proposal_rna = Slot(uri=NMDC_DH.proposal_rna, name="soil_emsl_jgi_mt_proposal_rna", curie=NMDC_DH.curie('proposal_rna'),
                   model_uri=NMDC_DH.soil_emsl_jgi_mt_proposal_rna, domain=SoilEmslJgiMt, range=str)

slots.quantity_value_has_unit = Slot(uri="str(uriorcurie)", name="quantity value_has unit", curie=None,
                   model_uri=NMDC_DH.quantity_value_has_unit, domain=QuantityValue, range=Optional[str])

slots.quantity_value_has_numeric_value = Slot(uri="str(uriorcurie)", name="quantity value_has numeric value", curie=None,
                   model_uri=NMDC_DH.quantity_value_has_numeric_value, domain=QuantityValue, range=Optional[float])

slots.quantity_value_has_raw_value = Slot(uri="str(uriorcurie)", name="quantity value_has raw value", curie=None,
                   model_uri=NMDC_DH.quantity_value_has_raw_value, domain=QuantityValue, range=Optional[str])

slots.placeholder_class_investigation_field = Slot(uri="str(uriorcurie)", name="placeholder_class_investigation field", curie=None,
                   model_uri=NMDC_DH.placeholder_class_investigation_field, domain=PlaceholderClass, range=Optional[str])