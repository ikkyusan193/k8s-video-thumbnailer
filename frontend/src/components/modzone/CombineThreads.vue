<template>
  <v-dialog v-model="combthread" fullscreen scrollable>
    <template v-slot:activator="{ on, attrs }">
      <v-card
        v-bind="attrs"
        v-on="on"
        height="300px"
        outlined
        @click="combthread = true"
      >
        <v-card-title>
          <h3>Combine threads</h3>
        </v-card-title>
        <v-card-subtitle>
          <p>StackOverflow users will understand why we need this</p>
        </v-card-subtitle>
      </v-card>
    </template>

    <v-card>
      <v-card-title>
        <span class="text-h5">Combine threads</span>
      </v-card-title>
      <v-alert v-model="res_alert" dense dismissible outlined text type="info">
        {{ res_msg }}
      </v-alert>
      <v-divider></v-divider>

      <v-card-text v-if="threads.length > 0">
        <v-container v-for="t in threads" :key="t" fluid>
          <v-row dense>
            <v-col cols="1">
              <h5>Thread ID</h5>
              <p>{{ t.thread_id }}</p>
            </v-col>
            <v-col cols="7">
              <h5>Title</h5>
              <p>{{ t.title }}</p>
            </v-col>
            <v-col cols="2">
              <h5>Created by</h5>
              <p>{{ t.display_name }}</p>
            </v-col>
            <v-col cols="1">
              <h5>Likes</h5>
              <p>{{ t.likes }}</p>
            </v-col>
            <v-col cols="1">
              <h5>Comments</h5>
              <p>{{ t.comment_count }}</p>
            </v-col>
          </v-row>
          <v-row dense>
            <v-col cols="3">
              <h5>Posted on</h5>
              <p>{{ t.date }}</p>
            </v-col>
            <v-col cols="5">
              <h5>Tags</h5>
              <p v-if="t.tags.length === 0">None</p>
              <p v-else>{{ t.tags }}</p>
            </v-col>
            <v-col cols="4">
              <h5>Duplicates (Thread IDs)</h5>
              <p v-if="t.reported_as_dupes.length === 0">None</p>
              <p v-else>{{ t.reported_as_dupes }}</p>
            </v-col>
          </v-row>
        </v-container>
      </v-card-text>
      <v-card-text v-else>
        <p>Currently, there are no threads</p>
      </v-card-text>
      <v-divider></v-divider>
      <v-card-text>
        <v-text-field
          v-model="threadA"
          dense
          label="Thread ID A"
          required
        ></v-text-field>
        <v-text-field
          v-model="threadB"
          dense
          label="Thread ID B"
          required
        ></v-text-field>
      </v-card-text>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn text @click="combthread = false">Close</v-btn>
        <v-btn text @click="send_dupes">Merge</v-btn>
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
  name: "CombineThreads",
  data() {
    return {
      combthread: false,

      threadA: "",
      threadB: "",
      res_msg: "",
      res_alert: false,

      threads: [],
    };
  },
  methods: {
    async modzone() {
      const response = await axios.get("/api/modzone");
      this.threads = response.data.threads;
    },

    async send_dupes() {
      let formData = new FormData();
      formData.append("thread_a", this.threadA);
      formData.append("thread_b", this.threadB);
      formData.append("sky_username", this.$store.state.login_skyusername);
      const response = await Vue.axios.post(
        "/api/modzone/merge_threads",
        formData
      );
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
