<template>
  <v-app>
    <v-app-bar
      fixed
      height="80"
      dense
      color="#502b80"
      dark
      :src="require('./assets/MUIC_building.jpg')"
    >
      <!-- Fade color -->
      <template v-slot:img="{ props }">
        <v-img
          v-bind="props"
          :gradient="
            !$vuetify.theme.dark
              ? 'to top right, rgba(58, 0, 133,.7), rgba(25,32,72,.7)'
              : 'to top right, rgba(10,10,20,.7), rgba(25,32,72,.7)'
          "
        ></v-img>
      </template>

      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>

      <v-btn plain fab icon x-large class="mr-3" :to="{ name: 'Home' }">
        <v-img
          :src="require('./assets/icc_logo_border.png')"
          height="65"
          width="60"
          contain
        />
      </v-btn>

      <h1 class="white--text font-weight-bold">IC Courses</h1>

      <v-spacer></v-spacer>

      <v-col v-if="this.$route.name !== 'Search'" cols="12" sm="6" md="4">
        <v-text-field
          v-model="searchInput"
          label="Search here"
          class="mx-auto"
          clearable
          prepend-icon="mdi-magnify"
          @keydown.enter="searchbar()"
        ></v-text-field>
      </v-col>

      <v-menu bottom min-width="200px" open-on-hover offset-y right offset-x>
        <template v-slot:activator="{ on }">
          <v-btn icon v-on="on">
            <v-avatar size="48">
              <v-icon>mdi-account</v-icon>
            </v-avatar>
          </v-btn>
        </template>
        <v-card class="mx-auto" max-width="275" min-width="260" outlined>
          <v-list-item three-line>
            <v-list-item-content>
              <div v-if="!this.$store.state.status" class="text-h5 mb-1">
                Not logged in
              </div>
              <div v-else class="text-h5 mb-1">
                {{ this.$store.state.login_displayname }}
              </div>
              <v-list-item-subtitle v-if="!this.$store.state.status"
                >Status: Offline
              </v-list-item-subtitle>
              <v-list-item-subtitle v-else
                >Status: Online
              </v-list-item-subtitle>
            </v-list-item-content>

            <v-list-item-avatar size="60" color="grey">
              <v-icon dark> mdi-account </v-icon>
            </v-list-item-avatar>
          </v-list-item>

          <v-card-actions justify="space-around">
            <v-btn
              v-if="!this.$store.state.status"
              text
              :to="{ name: 'Login' }"
            >
              Log in
            </v-btn>
            <v-btn v-else text @click="logout"> Logout </v-btn>
            <v-btn
              v-if="this.$store.state.status"
              text
              :to="{ name: 'ChangeInformation' }"
            >
              Edit Account</v-btn
            >
          </v-card-actions>
        </v-card>
      </v-menu>

      <v-tooltip bottom nudge-left="20">
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            icon
            @click="$vuetify.theme.dark = !$vuetify.theme.dark"
            v-bind="attrs"
            v-on="on"
          >
            <v-icon>mdi-brightness-4</v-icon>
          </v-btn>
        </template>
        <span>Light / Dark Mode</span>
      </v-tooltip>
    </v-app-bar>

    <br /><br /><br />

    <v-navigation-drawer v-model="drawer" fixed>
      <v-list>
        <v-list-item>
          <v-list-item-avatar>
            <v-avatar size="40">
              <v-img :src="require('./assets/icc_logo_border.png')" contain />
            </v-avatar>
          </v-list-item-avatar>

          <v-list-item-content>
            <v-list-item-title>IC Courses</v-list-item-title>
          </v-list-item-content>

          <v-btn icon @click.stop="drawer = !drawer">
            <v-icon>mdi-chevron-left</v-icon>
          </v-btn>
        </v-list-item>
      </v-list>
      <v-divider></v-divider>
      <v-list nav dense>
        <v-list-item-group color="#9f7cf7">
          <v-list-item v-for="item in items" :key="item.title" :to="item.link">
            <v-list-item-icon>
              <v-icon v-text="item.icon"></v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title v-text="item.title"></v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>

    <v-main>
      <router-view />
    </v-main>

    <v-btn
      v-scroll="onScroll"
      v-show="scrolled"
      fab
      dark
      fixed
      bottom
      right
      color="purple darken-3"
      @click="toTop"
    >
      <v-icon>mdi-chevron-up</v-icon>
    </v-btn>
  </v-app>
</template>

<script>
import Vue from "vue";
import router from "./router";

export default {
  name: "App",

  data: () => ({
    drawer: false,
    items: [
      { title: "Forum", icon: "mdi-view-dashboard", link: "/" },
      { title: "FAQs", icon: "mdi-forum", link: "/faq" },
      { title: "Help", icon: "mdi-help-circle-outline", link: "/help" },
    ],
    searchInput: "",
    scrolled: false,
  }),

  created() {
    document.title = "IC Courses";
  },

  methods: {
    searchbar() {
      console.warn(this.searchInput);
      this.$router.push("/search/" + this.searchInput + "?filter=title");
      this.searchInput = "";
    },
    onScroll(e) {
      if (typeof window === "undefined") return;
      const top = window.pageYOffset || e.target.scrollTop || 0;
      this.scrolled = top > 20;
    },
    toTop() {
      this.$vuetify.goTo(0);
    },
    async logout() {
      let result = await Vue.axios.get("/api/logout");
      if (result.data.status) {
        console.log("logged out");
        await this.$store.dispatch("resetinfo");
        await router.push({ name: "Home" });
      }
    },
  },
};
</script>
