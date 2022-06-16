module.exports = {
  baseUrl: '/frontend', 
  transpileDependencies: ["vuetify"],
  devServer: {
    host: "localhost",
    disableHostCheck: true,
    port: 80,
    https: false,
    proxy: {
      "/backend": {
        target: "http://0.0.0.0.0:5000",
        // target: "http://localhost:80"
      },
    },
  },
};