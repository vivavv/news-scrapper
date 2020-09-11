const db = require('../../config/knex'); 

const table = 'ARTICLES';

module.exports = class Article {
  
  static all() {
    return db
      .select('*')
      .from(table);
  }
}

// module.exports.Article;
