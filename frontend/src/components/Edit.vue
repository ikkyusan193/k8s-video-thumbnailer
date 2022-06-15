<template v-model="$vuetify.theme.dark">
  <div>
    <v-container>
      <br />
      <!-- FAQ by mods -->
      <v-card class="mx-auto" outlined max-width="1000">
        <br />
        <v-row class="mx-4">
          <v-col>
            <h1 class="one">Edit thread</h1>
            <v-divider></v-divider>
          </v-col>
        </v-row>
        <br />

        <v-row class="mx-4">
          <v-col>
            <v-text-field
              v-model="title"
              label="Title"
              outlined
              disabled
            ></v-text-field>
          </v-col>
        </v-row>
        <br />
        <v-row class="mx-4">
          <v-col>
            <v-textarea v-model="text" label="Body" outlined></v-textarea>
          </v-col>
        </v-row>
        <v-row class="mx-4">
          <v-col>
            <h2 class="one">Tags</h2>
            <v-divider></v-divider>
          </v-col>
        </v-row>

        <v-row class="mx-4">
          <v-col>
            <v-autocomplete
              v-model="tags"
              :items="selectlist"
              label="None"
              outlined
              hide-selected
              single-line
              clearable
              deletable-chips
              multiple
              small-chips
            ></v-autocomplete>
          </v-col>
        </v-row>
        <v-card-actions class="ma-4">
          <v-spacer></v-spacer>
          <v-btn
            @click="$router.push({ name: 'Thread', params: { id: thread_id } })"
            >cancel</v-btn
          >
          <v-btn @click="sendData">post</v-btn>
        </v-card-actions>
      </v-card>
      <v-snackbar v-model="error" color="error" :vertical="true">
        {{ errormsg }}

        <template v-slot:action="{ attrs }">
          <v-btn text v-bind="attrs" @click="error = false"> Close </v-btn>
        </template>
      </v-snackbar>
    </v-container>
  </div>
</template>

<script>
import Vue from "vue";
import axios from "axios";
import VueAxios from "vue-axios";
Vue.use(VueAxios, axios);
export default {
  name: "Edit",
  data: () => ({
    thread_id: "",
    title: "",
    text: "",
    tags: [],
    selectlist: [],
    errormsg: "",
    error: false,
  }),

  methods: {
    async sendData() {
      let formData = new FormData();
      formData.append("thread_id", this.thread_id);
      formData.append("text", this.text);
      formData.append("tags", this.tags);
      formData.append("sky_username", this.$store.state.login_skyusername);
      const response = await axios
        .post("/api/edit_thread", formData)
        .catch((error) => {
          if (error.response) {
            console.warn("something went wrong");
          }
        });
      console.log(response.data);
      if (response.data.status) {
        await this.$router.push("/thread/" + this.thread_id);
      } else {
        this.errormsg = response.data.message;
        this.error = true;
        console.warn(response.data.status);
      }
    },
    async getInfo() {
      const response = await axios
        .get("/api/edit_thread?thread_id=" + this.$route.params.id)
        .catch((error) => {
          if (error.response) {
            console.warn("something went wrong");
          }
        });
      console.log(response);
      this.thread_id = this.$route.params.id;
      this.title = response.data.title;
      this.text = response.data.body;
      this.selectlist = response.data.courses;
      this.tags = response.data.selected_tags;
    },
  },
  async created() {
    await this.getInfo();
  },
};
</script>

<style src="../css/Create.css"></style>
