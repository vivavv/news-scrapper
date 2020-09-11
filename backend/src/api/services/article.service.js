const Article = require('../models/Article');

const articleService = {
  /**
   * CRUD services
   */
  list: () => Article.all(),
};


module.exports = articleService;
