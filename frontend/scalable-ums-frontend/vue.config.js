module.exports = {
  transpileDependencies: ["vuetify"],
  devServer: {
    host: "localhost", // frontend hostname or ip
    disableHostCheck: true,
    port: 8000, // frontend port
    https: false, // no ssl
    proxy: {
      "/api": {
        // proxy everything from frontend http://localhost:8080/api/** to backend at http://localhost:8081/api/**
        // that is why all api path on backend should begin with /api
        target: "http://localhost:8080",
      },
    },
  },
};
