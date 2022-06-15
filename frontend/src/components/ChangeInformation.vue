<template v-model="$vuetify.theme.dark">
  <v-container>
    <br />
    <v-card class="mx-auto">
      <!-- Header -->
      <v-list-item three-line>
        <v-list-item-content>
          <v-list-item-title class="mb-1">
            <h1 class="font-text">Change Account Information</h1>
          </v-list-item-title>
          <p />
          <v-divider class="divider-header"></v-divider>
          <br />
        </v-list-item-content>
        <v-list-item-avatar size="60" color="grey" class="justify-center">
          <v-icon dark> mdi-account </v-icon>
        </v-list-item-avatar>
      </v-list-item>
      <br />
      <v-row>
        <v-col class="mx-16">
          <v-form ref="form" v-model="valid" lazy-validation>
            <v-text-field
              v-model="display_name"
              :append-icon="
                this.check_display_name_exit ? 'mdi-check-all' : 'mdi-xamarin'
              "
              :color="this.check_display_name_exit ? 'green' : 'red'"
              @input="checkUser"
              :rules="display_name_rule"
              counter="25"
              outlined
              label="New display name"
              class="align-center"
              clearable
            ></v-text-field>
            <v-text-field
              v-model="current_password"
              :rules="password_rule"
              :append-icon="show_current_password ? 'mdi-eye' : 'mdi-eye-off'"
              :type="show_current_password ? 'text' : 'password'"
              hint="*This is required"
              outlined
              label="Current password*"
              color="#2a0094"
              class="align-center"
              @click:append="show_current_password = !show_current_password"
              clearable
            ></v-text-field>
            <v-text-field
              v-model="new_password"
              :append-icon="show_password ? 'mdi-eye' : 'mdi-eye-off'"
              :type="show_password ? 'text' : 'password'"
              outlined
              label="New password"
              color="#2a0094"
              class="align-center"
              @click:append="show_password = !show_password"
              clearable
            ></v-text-field>
            <v-text-field
              v-model="confirm_new_password"
              :rules="[passwordConfirmationRule]"
              :type="show_password ? 'text' : 'password'"
              outlined
              label="Confirm new password"
              color="#2a0094"
              class="align-center"
              @click:append="show_password = !show_password"
              clearable
            ></v-text-field>
          </v-form>
          <small>*indicates required field</small>
        </v-col>
      </v-row>
      <v-card-actions class="justify-end mx-4">
        <v-btn
          :disabled="!valid || this.current_password.length === 0"
          color="#2a0094"
          class="white--text"
          @click="sendUserInformation"
          >Save</v-btn
        >
      </v-card-actions>
    </v-card>
    <v-snackbar color="error" v-model="display_dialog" :vertical="true">
      {{ message_error }}

      <template v-slot:action="{ attrs }">
        <v-btn text v-bind="attrs" @click="display_dialog = false">
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </v-container>
</template>

<script>
import store from "../store";
import axios from "axios";
export default {
  name: "ChangePassword",
  data: () => ({
    valid: true,
    display_dialog: false,
    check_display_name_exit: true,
    display_name: store.state.login_displayname,
    show_password: false,
    show_current_password: false,
    message_error: "",
    current_password: "",
    new_password: "",
    confirm_new_password: "",
    display_name_rule: [
      (v) => !!v || "Display name is required",
      (v) =>
        (v && v.length <= 25) || "Display name must be less than 25 characters",
    ],
    password_rule: [(v) => !!v || "Password can not be empty"],
  }),
  methods: {
    async checkUser() {
      let request = new FormData();
      request.append("display_name", this.display_name);
      let response = await axios
        .post("/api/checkuser", request)
        .catch((error) => {
          if (error.response) {
            console.warn("something went wrong");
          }
        });
      if (this.display_name === store.state.login_displayname)
        this.check_display_name_exit = true;
      else {
        this.check_display_name_exit = response.data.status;
      }
    },
    async sendUserInformation() {
      if (this.new_password !== this.confirm_new_password) {
        this.message_error = "Please confirm your new password";
        this.display_dialog = true;
      } else if (!this.check_display_name_exit) {
        this.message_error = "Display name is already taken";
        this.display_dialog = true;
      } else {
        let request = new FormData();
        request.append("sky_username", store.state.login_skyusername);
        request.append("display_name", this.display_name);
        request.append("current_password", this.current_password);
        request.append("new_password", this.new_password);
        let response = await axios.post("/api/change_info", request);
        console.log(response.data);
        if (response.data.status) {
          await this.$router.push("/");
        } else {
          this.message_error = response.data.message;
          this.display_dialog = true;
        }
      }
    },
  },
  computed: {
    passwordConfirmationRule() {
      return () =>
        this.new_password === this.confirm_new_password ||
        "New password must match";
    },
  },
};
</script>

<style src="../css/ChangeInformation.css"></style>
