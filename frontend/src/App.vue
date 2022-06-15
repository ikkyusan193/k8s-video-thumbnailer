<template>
  
  <v-app>
    <v-navigation-drawer v-model="sidebar" app>
      <v-list>
        <v-list-tile
          v-for="item in menuItems"
          :key="item.title"
          :to="item.path">
          <v-list-tile-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>{{ item.title }}</v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar color="deep-purple" dark app >
      <v-toolbar-title>
        <router-link to="/" tag="span" style="cursor: pointer">
          {{ appTitle }}
        </router-link>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items>
        <v-btn
          flat
          v-for="item in menuItems"
          :key="item.title"
          :to="item.path">
          <v-icon left purple>{{ item.icon }}</v-icon>
          {{ item.title }}
        </v-btn>
      </v-toolbar-items>
    </v-app-bar>

    <v-content>
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>
// import Vue from "vue";
// import router from "./router";

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
  }),

  created() {
    
  },

  methods: {
  },
};
</script>
