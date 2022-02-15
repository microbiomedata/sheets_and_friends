

CREATE TABLE quantity_value (
	has_unit TEXT, 
	has_numeric_value FLOAT, 
	has_raw_value TEXT, 
	PRIMARY KEY (has_unit, has_numeric_value, has_raw_value)
);

CREATE TABLE soil_emsl_jgi_mg (
	"project_ID" TEXT NOT NULL, 
	sample_type TEXT NOT NULL, 
	sample_shipped TEXT NOT NULL, 
	"EMSL_store_temp" TEXT NOT NULL, 
	technical_reps TEXT, 
	replicate_number TEXT, 
	dna_seq_project TEXT NOT NULL, 
	dna_seq_project_name TEXT NOT NULL, 
	"dna_samp_ID" TEXT NOT NULL, 
	dna_sample_name TEXT NOT NULL, 
	dna_concentration TEXT NOT NULL, 
	dna_volume TEXT NOT NULL, 
	dna_absorb1 TEXT NOT NULL, 
	dna_absorb2 TEXT, 
	"dna_container_ID" TEXT NOT NULL, 
	dna_cont_type VARCHAR(5) NOT NULL, 
	dna_cont_well TEXT NOT NULL, 
	dna_sample_format VARCHAR(19) NOT NULL, 
	dna_dnase VARCHAR(3) NOT NULL, 
	dna_organisms TEXT, 
	dna_collect_site TEXT NOT NULL, 
	dna_isolate_meth TEXT NOT NULL, 
	"dna_seq_project_PI" TEXT NOT NULL, 
	dna_project_contact TEXT NOT NULL, 
	proposal_dna TEXT NOT NULL, 
	rna_seq_project TEXT NOT NULL, 
	rna_seq_project_name TEXT NOT NULL, 
	"rna_samp_ID" TEXT NOT NULL, 
	rna_sample_name TEXT NOT NULL, 
	rna_concentration TEXT NOT NULL, 
	rna_volume TEXT NOT NULL, 
	rna_absorb1 TEXT NOT NULL, 
	rna_absorb2 TEXT, 
	"rna_container_ID" TEXT NOT NULL, 
	rna_cont_type VARCHAR(5) NOT NULL, 
	rna_cont_well TEXT NOT NULL, 
	rna_sample_format TEXT NOT NULL, 
	dnase_rna VARCHAR(3) NOT NULL, 
	rna_organisms TEXT, 
	rna_collect_site TEXT NOT NULL, 
	rna_isolate_meth TEXT NOT NULL, 
	"rna_seq_project_PI" TEXT NOT NULL, 
	rna_project_contact TEXT NOT NULL, 
	proposal_rna TEXT NOT NULL, 
	non_microb_biomass TEXT, 
	non_microb_biomass_method TEXT, 
	"microbial_biomass_C" TEXT, 
	"micro_biomass_C_meth" TEXT, 
	"microbial_biomass_N" TEXT, 
	"micro_biomass_N_meth" TEXT, 
	org_nitro_method TEXT, 
	collection_time TEXT, 
	collection_date_inc TEXT, 
	collection_time_inc TEXT, 
	start_date_inc TEXT, 
	start_time_inc TEXT, 
	filter_method TEXT, 
	experimental_factor_other TEXT, 
	other_treatment TEXT, 
	isotope_exposure TEXT, 
	env_package VARCHAR(4) NOT NULL, 
	analysis_type VARCHAR(22) NOT NULL, 
	sample_link TEXT, 
	ecosystem TEXT, 
	ecosystem_category TEXT, 
	ecosystem_subtype TEXT, 
	ecosystem_type TEXT, 
	specific_ecosystem TEXT, 
	gold_path_field TEXT, 
	environment_field TEXT, 
	core_field TEXT, 
	nucleic_acid_sequence_source_field TEXT, 
	investigation_field TEXT, 
	agrochem_addition TEXT, 
	air_temp_regm TEXT, 
	al_sat TEXT, 
	al_sat_meth TEXT, 
	alt TEXT, 
	annual_precpt TEXT, 
	annual_temp TEXT, 
	biotic_regm TEXT, 
	biotic_relationship VARCHAR(12), 
	carb_nitro_ratio TEXT, 
	chem_administration TEXT, 
	climate_environment TEXT, 
	collection_date DATE NOT NULL, 
	crop_rotation TEXT, 
	cur_land_use VARCHAR(93), 
	cur_vegetation TEXT, 
	cur_vegetation_meth TEXT, 
	depth TEXT NOT NULL, 
	drainage_class VARCHAR(19), 
	elev TEXT NOT NULL, 
	env_broad_scale TEXT NOT NULL, 
	env_local_scale TEXT NOT NULL, 
	env_medium TEXT NOT NULL, 
	experimental_factor TEXT, 
	extreme_event DATE, 
	fao_class VARCHAR(13), 
	fire DATE, 
	flooding DATE, 
	gaseous_environment TEXT, 
	geo_loc_name TEXT NOT NULL, 
	growth_facil TEXT, 
	heavy_metals TEXT, 
	heavy_metals_meth TEXT, 
	horizon_meth TEXT, 
	humidity_regm TEXT, 
	lat_lon TEXT NOT NULL, 
	light_regm TEXT, 
	link_class_info TEXT, 
	link_climate_info TEXT, 
	local_class TEXT, 
	local_class_meth TEXT, 
	micro_biomass_meth TEXT, 
	microbial_biomass TEXT, 
	misc_param TEXT, 
	org_matter TEXT, 
	org_nitro TEXT, 
	oxy_stat_samp VARCHAR(9), 
	ph FLOAT, 
	ph_meth TEXT, 
	phosphate TEXT, 
	prev_land_use_meth TEXT, 
	previous_land_use TEXT, 
	profile_position VARCHAR(9), 
	rel_to_oxygen VARCHAR(17), 
	salinity TEXT, 
	salinity_meth TEXT, 
	samp_collec_device TEXT, 
	samp_collec_method TEXT, 
	samp_mat_process TEXT, 
	samp_name TEXT NOT NULL, 
	samp_size TEXT, 
	samp_store_temp TEXT, 
	season_precpt TEXT, 
	season_temp TEXT, 
	sieving TEXT, 
	size_frac_low TEXT, 
	size_frac_up TEXT, 
	slope_aspect TEXT, 
	slope_gradient TEXT, 
	soil_horizon VARCHAR(10), 
	soil_text_measure TEXT, 
	soil_texture_meth TEXT, 
	soil_type TEXT, 
	soil_type_meth TEXT, 
	source_mat_id TEXT, 
	store_cond TEXT, 
	"temp" TEXT, 
	tillage VARCHAR(13), 
	tot_carb TEXT, 
	tot_nitro_cont_meth TEXT, 
	tot_nitro_content TEXT, 
	tot_org_c_meth TEXT, 
	tot_org_carb TEXT, 
	tot_phosp TEXT, 
	water_cont_soil_meth TEXT, 
	water_content TEXT, 
	watering_regm TEXT, 
	attribute TEXT, 
	PRIMARY KEY ("project_ID", sample_type, sample_shipped, "EMSL_store_temp", technical_reps, replicate_number, dna_seq_project, dna_seq_project_name, "dna_samp_ID", dna_sample_name, dna_concentration, dna_volume, dna_absorb1, dna_absorb2, "dna_container_ID", dna_cont_type, dna_cont_well, dna_sample_format, dna_dnase, dna_organisms, dna_collect_site, dna_isolate_meth, "dna_seq_project_PI", dna_project_contact, proposal_dna, rna_seq_project, rna_seq_project_name, "rna_samp_ID", rna_sample_name, rna_concentration, rna_volume, rna_absorb1, rna_absorb2, "rna_container_ID", rna_cont_type, rna_cont_well, rna_sample_format, dnase_rna, rna_organisms, rna_collect_site, rna_isolate_meth, "rna_seq_project_PI", rna_project_contact, proposal_rna, non_microb_biomass, non_microb_biomass_method, "microbial_biomass_C", "micro_biomass_C_meth", "microbial_biomass_N", "micro_biomass_N_meth", org_nitro_method, collection_time, collection_date_inc, collection_time_inc, start_date_inc, start_time_inc, filter_method, experimental_factor_other, other_treatment, isotope_exposure, env_package, analysis_type, sample_link, ecosystem, ecosystem_category, ecosystem_subtype, ecosystem_type, specific_ecosystem, gold_path_field, environment_field, core_field, nucleic_acid_sequence_source_field, investigation_field, agrochem_addition, air_temp_regm, al_sat, al_sat_meth, alt, annual_precpt, annual_temp, biotic_regm, biotic_relationship, carb_nitro_ratio, chem_administration, climate_environment, collection_date, crop_rotation, cur_land_use, cur_vegetation, cur_vegetation_meth, depth, drainage_class, elev, env_broad_scale, env_local_scale, env_medium, experimental_factor, extreme_event, fao_class, fire, flooding, gaseous_environment, geo_loc_name, growth_facil, heavy_metals, heavy_metals_meth, horizon_meth, humidity_regm, lat_lon, light_regm, link_class_info, link_climate_info, local_class, local_class_meth, micro_biomass_meth, microbial_biomass, misc_param, org_matter, org_nitro, oxy_stat_samp, ph, ph_meth, phosphate, prev_land_use_meth, previous_land_use, profile_position, rel_to_oxygen, salinity, salinity_meth, samp_collec_device, samp_collec_method, samp_mat_process, samp_name, samp_size, samp_store_temp, season_precpt, season_temp, sieving, size_frac_low, size_frac_up, slope_aspect, slope_gradient, soil_horizon, soil_text_measure, soil_texture_meth, soil_type, soil_type_meth, source_mat_id, store_cond, "temp", tillage, tot_carb, tot_nitro_cont_meth, tot_nitro_content, tot_org_c_meth, tot_org_carb, tot_phosp, water_cont_soil_meth, water_content, watering_regm, attribute)
);