<template>
  <v-dialog v-model="addtags" max-width="600px">
    <template v-slot:activator="{ on, attrs }">
      <v-card
        v-bind="attrs"
        v-on="on"
        height="300px"
        outlined
        @click="addtags = true"
      >
        <v-card-title>
          <h3>Add tags</h3>
        </v-card-title>
        <v-card-subtitle>
          <p>Add more tags because we still don't have enough</p>
        </v-card-subtitle>
      </v-card>
    </template>

    <v-card>
      <v-card-title>
        <span class="text-h5">Add a new tag</span>
      </v-card-title>
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
            v-model="course_id"
            dense
            label="Course ID"
            required
          ></v-text-field>
          <v-text-field
            v-model="course_name"
            dense
            label="Course Name"
            required
          ></v-text-field>
        </v-container>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn text @click="addtags = false">Close</v-btn>
        <v-btn text @click="add_tags">Add</v-btn>
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
  name: "AddTags",
  data() {
    return {
      course_id: "",
      course_name: "",
      res_msg: "",
      addtags: false,
      res_alert: false,
    };
  },

  methods: {
    async add_tags() {
      let formData = new FormData();
      formData.append("sky_username", this.$store.state.login_skyusername);
      formData.append("course_id", this.course_id);
      formData.append("course_name", this.course_name);

      const response = await axios
        .post("/api/modzone/add_tag", formData)
        .catch((error) => {
          if (error.response) {
            console.warn("something went wrong while adding tags");
          }
        });
      this.res_msg = response.data.message;
      this.res_alert = true;
    },
  },
};
</script>

<style scoped></style>
