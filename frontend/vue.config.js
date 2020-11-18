module.exports = {
  devServer: {
    /* Flask server (REST API) */
    proxy: {
      '^/api': {
        target: 'http://localhost:5000',
      },
    }
  }
}
