const knex = require('knex');

module.exports = database = knex({
  client: 'sqlite3',
  connection: {
    filename: "./test.sqlite"
  }
});
