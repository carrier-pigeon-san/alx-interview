#!/usr/bin/node
// Write a script that prints all characters of a Star Wars movie:
const request = require('request');
const { argv } = require('node:process');
const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;

request.get(url, { json: true }, async (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }

  if (res.statusCode === 200) {
    for (const character of body.characters) {
      const response = await new Promise((resolve, reject) => {
        request.get(character, { json: true }, (err, res, body) => {
          if (err) {
            return reject(err);
          }
          resolve(body);
        });
      });
      console.log(response.name);
    }
  }
});
