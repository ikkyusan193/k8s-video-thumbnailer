<template>
  <v-dialog v-model="manmod" fullscreen scrollable>
    <template v-slot:activator="{ on, attrs }">
      <v-card
        v-bind="attrs"
        v-on="on"
        height="300px"
        outlined
        @click="manmod = true"
      >
        <v-card-title>
          <h3>Manage moderators</h3>
        </v-card-title>
        <v-card-subtitle>
          <p>
            "In case we wanna cancel someone from being a mod lol" - Pornkamol
          </p>
        </v-card-subtitle>
      </v-card>
    </template>

    <v-card>
      <v-card-title>
        <span class="text-h5">Manage moderators</span>
      </v-card-title>
      <v-card-subtitle>
        <p>Please do not abuse this system thanks</p>
      </v-card-subtitle>
      <v-divider></v-divider>

      <v-card-text v-if="users.length > 0">
        <v-container v-for="u in users" :key="u" fluid>
          <v-row dense>
            <v-col cols="3">
              <h5>SKY Username</h5>
              <p>{{ u.sky_username }}</p>
            </v-col>
            <v-col cols="3">
              <h5>Display name</h5>
              <p>{{ u.display_name }}</p>
            </v-col>
            <v-col cols="4">
              <h5>E-mail</h5>
              <p>{{ u.email }}</p>
            </v-col>
            <v-col cols="2">
              <h5>Mod</h5>
              <v-switch
                v-model="u.mod"
                type="info"
                @change="update_mod(u.sky_username, u.mod)"
              ></v-switch>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <h5>isMod</h5>
              <p>{{ u.mod }}</p>
            </v-col>
          </v-row>
        </v-container>
      </v-card-text>
      <v-card-text v-else>
        <p>There is no user</p>
      </v-card-text>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn text @click="manmod = false">Close</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import axios from "axios";
import Vue from "vue";
import VueAxios from "vue-axios";

Vue.use(VueAxios, axios);

export default {
  name: "MakeMod",
  data() {
    return {
      manmod: false,

      users: [],

      res_alert: false,
      res_msg: "",
    };
  },
  methods: {
    async modzone() {
      const response = await axios.get("/api/modzone");
      this.users = response.data.users;
    },

    async update_mod(candidate_username, is_mod) {
      let formData = new FormData();
      formData.append("sky_username", this.$store.state.login_skyusername);
      formData.append("candidate_username", candidate_username);
      formData.append("modval", is_mod);

      const response = await axios.post("/api/modzone/set_moderator", formData);
      this.res_msg = response.data.message;
      this.res_alert = true;
    },
  },

  created() {
    this.modzone();
  },
};
</script>

<style scoped></style>
