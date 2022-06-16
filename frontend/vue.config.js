module.exports = {
  transpileDependencies: ["vuetify"],
  devServer: {
    host: "localhost",
    port: 8080,
    https: false,
    proxy: {
      "/backend": {
        target: "http://0.0.0.0.0:5000",
        // target: "http://localhost:80"
      },
    },
  },
};