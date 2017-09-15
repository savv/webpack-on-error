const path = require('path');

module.exports = {
  entry: './index.js',
  devtool: 'eval',
  output: {
    filename: 'index.js',
    path: path.resolve(__dirname, 'dist')
  }
};
