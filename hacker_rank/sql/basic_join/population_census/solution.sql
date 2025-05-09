SELECT SUM(ci.population) FROM city ci LEFT JOIN country co ON ci.countrycode = co.code WHERE co.continent = 'Asia';
