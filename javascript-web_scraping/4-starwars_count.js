#!/usr/bin/node
const request = require('request');
const characterId = '18/';
const filmApiUrl = 'https://swapi-api.hbtn.io/api/films/';
const characterApiUrl = 'https://swapi-api.hbtn.io/api/people/';

request(filmApiUrl, function (err, response, body) {
  if (err) throw err;
  // converting the data to json
  const films = JSON.parse(body).results;
  // iterating over each film to find matching character id
  let movieCount = 0;
  films.forEach(function (film) {
    // find the characters for each movie
    const characters = film.characters;
    if (characters.includes(characterApiUrl + characterId)) {
      movieCount++;
    }
  });

  console.log(movieCount);
});
