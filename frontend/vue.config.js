module.exports = {
  transpileDependencies: ["vuetify"],
  devServer: {
    host: "localhost",
    port: 8080,
    https: false,
    proxy: {
      "/api": {
        target: "http://0.0.0.0.0:5000",
        // target: "localhost"
      },
    },
  },
};