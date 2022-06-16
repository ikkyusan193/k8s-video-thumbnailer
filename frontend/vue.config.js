module.exports = {
  publicPath: process.env.APP_BASEPATH, 
  transpileDependencies: ["vuetify"],
  devServer: {
    host: "localhost",
    disableHostCheck: true,
    //  port: 80, // top = deploy, bot = local
    port: 8080,
    https: false,
    proxy: {
      "/backend": {
        // target: "http://0.0.0.0.0:5000",
        target: "http://localhost:80"
      },
    },
  },
};