<template>
  <v-dialog v-model="forgotpwd" max-width="600px">
    <template v-slot:activator="{ on, attrs }">
      <v-btn
        v-bind="attrs"
        v-on="on"
        color="#2a0094"
        dark
        @click="forgotpwd = true"
      >
        Forgot password
      </v-btn>
    </template>
    <v-card>
      <v-card-title>
        <span class="text-h5">Request a new password</span>
      </v-card-title>
      <v-card-text>
        <v-container>
          <v-text-field
            v-model="SKY_username"
            dense
            label="SKY Username"
            required
          ></v-text-field>
          <!--<p>{{ SKY_username }}</p>-->
          <v-text-field
            v-model="email"
            dense
            label="E-mail"
            required
          ></v-text-field>
          <!--<p>{{ email }}</p>-->
        </v-container>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" text @click="forgotpwd = false"
          >Close
        </v-btn>
        <v-btn color="blue darken-1" text @click="send_request">
          Send request
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import Vue from "vue";
import axios from "axios";
import VueAxios from "vue-axios";

Vue.use(VueAxios, axios);

export default {
  name: "ForgotPwd",
  data() {
    return {
      SKY_username: "",
      email: "",
      pwdrequest_text: "",
      forgotpwd: false,
    };
  },

  methods: {
    async send_request() {
      let formData = new FormData();
      formData.append("sky_username", this.SKY_username);
      formData.append("email", this.email);
      const response = await axios
        .post("/api/new_password", formData)
        .catch((error) => {
          if (error.response) {
            console.warn("something went wrong");
          }
        });

      this.pwdrequest_text = response.data.response;
      this.forgotpwd = false;
    },
  },
};
</script>
