const express = require('express');
const userRoutes = require('./user.route');
const authRoutes = require('./auth.route');
const articleRoutes = require('./article.route');

const router = express.Router();

/**
 * GET v1/status
 */
router.get('/status', (req, res) => res.send('OK'));

/**
 * GET v1/docs
 */
// router.use('/users', userRoutes);
// router.use('/auth', authRoutes);
router.use('/articles', articleRoutes);

module.exports = router;
