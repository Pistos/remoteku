module.exports = {
  devServer: {
    /* Flask server (REST API) */
    proxy: 'http://localhost:5000'
  }
}
