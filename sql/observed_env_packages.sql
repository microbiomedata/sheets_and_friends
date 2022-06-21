-- seconds
.headers on
.mode tabs
SELECT
	env_package,
	count(1) as sample_count
from
	harmonized_wide hw
group by
	env_package
order by
	count(1) desc;
