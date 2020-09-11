const express = require('express');
const validate = require('express-validation');
const controller = require('../../controllers/user.controller');
const articleService = require('../../services/article.service');

const router = express.Router();

router
  .route('/')
  .get((async (req, res) => {

    const {articles} = await articleService.list(req.query);
    res.status(200);
    res.json({data: articles})

  })
  );



module.exports = router;
