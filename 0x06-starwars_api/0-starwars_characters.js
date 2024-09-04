#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const film = JSON.parse(body);
  const characters = film.characters;
  
  characters.forEach((characterUrl) => {
    request(characterUrl, (err, res, charBody) => {
      if (err) {
        console.error(err);
        return;
      }
      const character = JSON.parse(charBody);
      console.log(character.name);
    });
  });
});
