<template>
  
  <v-app>

    <v-app-bar color="deep-purple" dark app >
      <v-toolbar-title>
        <router-link to="/" tag="span" style="cursor: pointer">
          {{ appTitle }}
        </router-link>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items>
        <v-btn
          v-for="item in menuItems"
          :key="item.title"
          :to="item.path">
          <v-icon left purple>{{ item.icon }}</v-icon>
          {{ item.title }}
        </v-btn>
      </v-toolbar-items>
    </v-app-bar>

    <h6>{{info}}</h6>
    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
// import Vue from "vue";
// import router from "./router";
const axios = require('axios').default;

export default {
  name: "App",

  data: () => ({
    drawer: false,
    appTitle: 'P2 – Video Thumbnailer',
    sidebar: false,
    menuItems: [
          { title: 'Dashboard', path: '/'},
          { title: 'Display Room', path: '/display'},
     ],
    searchInput: "",
    scrolled: false,
    info: {}
  }),

  created() {
    
  },

  mounted () {
    axios
      .get('/api/videos')
      .then(response => (this.info = response.data))
  },
};
</script>
