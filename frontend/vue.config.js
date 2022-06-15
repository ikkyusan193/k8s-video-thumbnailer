module.exports = {
  transpileDependencies: ["vuetify"],
  devServer: {
    host: "localhost",
    disableHostCheck: true,
    port: 9000,
    https: false,
    proxy: {
      "/api": {
        target: "http://127.0.0.1:5000",
      },
    },
  },
};