<template>
  <v-dialog v-model="modpassword" fullscreen>
    <template v-slot:activator="{ on, attrs }">
      <v-card
        v-bind="attrs"
        v-on="on"
        height="300px"
        outlined
        @click="modpassword = true"
      >
        <v-card-title>
          <h3>Change password</h3>
        </v-card-title>
        <v-card-subtitle>
          <p>
            Help out forgetful people who forgot their password because we are
            very nice people
          </p>
        </v-card-subtitle>
      </v-card>
    </template>

    <v-card>
      <v-card-title>
        <span class="text-h5">Change a user's password</span>
      </v-card-title>

      <v-card-text v-if="users.length > 0">
        <v-container v-for="u in users" :key="u" fluid>
          <v-row dense>
            <v-col cols="4">
              <h5>SKY Username</h5>
              <p>{{ u.sky_username }}</p>
            </v-col>
            <v-col cols="4">
              <h5>Display name</h5>
              <p>{{ u.display_name }}</p>
            </v-col>
            <v-col cols="4">
              <h5>E-mail</h5>
              <p>{{ u.email }}</p>
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

      <v-card-text>
        <v-container>
          <v-alert
            v-model="res_alert"
            dense
            dismissible
            outlined
            text
            type="info"
          >
            {{ res_msg }}
          </v-alert>
          <v-spacer></v-spacer>
          <v-text-field
            v-model="requested_change_username"
            dense
            label="Username to change"
            required
          ></v-text-field>
          <v-text-field
            v-model="new_password"
            dense
            label="New password"
            required
          ></v-text-field>
        </v-container>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn text @click="modpassword = false">Close</v-btn>
        <v-btn text @click="change_password">Change</v-btn>
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
  name: "ModPassword",
  data() {
    return {
      res_msg: "",
      res_alert: false,
      modpassword: false,

      users: [],

      requested_change_username: "",
      new_password: "",
    };
  },
  created() {
    this.modzone();
  },

  methods: {
    async change_password() {
      let formData = new FormData();
      formData.append("sky_username", this.$store.state.login_skyusername);
      formData.append(
        "requested_change_username",
        this.requested_change_username
      );
      formData.append("new_password", this.new_password);
      const response = await axios.post(
        "/api/modzone/password_change",
        formData
      );
      this.res_msg = response.data.message;
      this.res_alert = true;
    },

    async modzone() {
      const response = await axios.get("/api/modzone");
      this.users = response.data.users;
    },
  },
};
</script>

<style scoped></style>
