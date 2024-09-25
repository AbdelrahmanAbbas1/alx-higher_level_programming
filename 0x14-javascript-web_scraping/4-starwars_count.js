#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const character = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, (err, response, data) => {
  if (err) console.log(err);

  const films = JSON.parse(data);
  let count = 0;
  films.results.forEach(film => {
    film.characters.forEach(ch => {
      if (ch === character) count++;
    });
  });
  console.log(count);
});
