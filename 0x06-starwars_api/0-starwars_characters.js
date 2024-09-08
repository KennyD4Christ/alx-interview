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

  const printCharacters = (characters, index = 0) => {
    if (index >= characters.length) return;

    request(characters[index], (err, res, charBody) => {
      if (err) {
        console.error(err);
        printCharacters(characters, index + 1);
        return;
      }
      const character = JSON.parse(charBody);
      console.log(character.name);
      printCharacters(characters, index + 1);
    });
  };

  printCharacters(characters);
});
