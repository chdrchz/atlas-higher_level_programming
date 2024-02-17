-- Script that lists all cities in a database
SELECT cities.id, cities.name, state.name FROM cities
LEFT JOIN states ON cities.state_id = states.id ORDER BY id ASC;
