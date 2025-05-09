SELECT ci.name FROM city ci LEFT JOIN country co ON ci.countrycode = co.code WHERE co.continent = 'Africa';
