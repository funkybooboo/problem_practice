select 
    co.continent,
    floor(avg(ci.population)) as average_population
from 
    country co
join 
    city ci on co.code = ci.countrycode
group by 
    co.continent;

