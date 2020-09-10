const knex = require('knex');

const database = require('knex')({
  client: 'sqlite3',
  connection: {
    filename: "./test.sqlite"
  }
});
