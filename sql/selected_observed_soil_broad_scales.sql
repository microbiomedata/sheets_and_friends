.headers on
.mode tabs
-- takes ~ 1 minute
-- masks some error cases without directly solving them
--   (see having statements)
-- also masks large number of blank/null env_broad_scale values
SELECT
	lower(env_broad_scale) as lower_env_broad_scale,
	count(1) as sample_count
from
	harmonized_wide hw
where
	lower(env_package) like '%soil%'
group by
	lower_env_broad_scale
having
	sample_count > 1
	and env_broad_scale is not null
	and env_broad_scale != ''
	and length(env_broad_scale) > 1
order by
	count(1) desc;