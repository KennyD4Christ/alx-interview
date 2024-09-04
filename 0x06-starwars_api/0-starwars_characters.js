#!/usr/bin/node

const request = require('request');

// Get the Movie ID from the first positional argument
const movieID = process.argv[2];

// Construct the URL to fetch the movie details
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}/`;

// Make the request to the API
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the response body as JSON
  const movieData = JSON.parse(body);

  // Extract the character URLs from the movie data
  const characters = movieData.characters;

  // Fetch and print each character's name in the order they appear in the list
  characters.forEach((characterURL) => {
    request(characterURL, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      // Parse the character data and print the name
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});

