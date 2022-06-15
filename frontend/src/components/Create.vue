<template v-model="$vuetify.theme.dark">
  <div>
    <v-container>
      <br />
      <!-- FAQ by mods -->
      <v-card class="mx-auto" outlined max-width="1000">
        <br />
        <v-row class="mx-4">
          <v-col>
            <h1 class="one">Create a new thread</h1>
            <v-divider></v-divider>
          </v-col>
        </v-row>
        <br />

        <v-form v-model="valid">
          <v-row class="mx-4">
            <v-col>
              <v-text-field
                v-model="title"
                label="Title"
                outlined
                counter
                maxlength="120"
                :rules="[() => !!title || 'This field is required']"
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
            <v-btn :disabled="!valid" @click="sendData">post</v-btn>
          </v-card-actions>
        </v-form>
      </v-card>
    </v-container>
  </div>
</template>

<script>
import Vue from "vue";
import axios from "axios";
import VueAxios from "vue-axios";
Vue.use(VueAxios, axios);
export default {
  name: "Create",
  data: () => ({
    title: "",
    text: "",
    tags: "",
    selectlist: [],
    errormsg: "",
    valid: false,
  }),

  methods: {
    async sendData() {
      let formData = new FormData();
      formData.append("title", this.title);
      formData.append("text", this.text);
      formData.append("tags", this.tags);
      formData.append("username", this.$store.state.login_skyusername);
      const response = await axios
        .post("/api/create_thread", formData)
        .catch((error) => {
          if (error.response) {
            console.warn("something went wrong");
          }
        });
      console.log(response.data);
      if (response.data.status) {
        await this.$router.push("/thread/" + response.data.thread_id);
      } else {
        this.error = true;
        this.errormsg = response.data.message;
        console.warn(response.data.status);
      }
    },
    async extractlist() {
      const response = await axios.get("/api/create_thread").catch((error) => {
        if (error.response) {
          console.warn("something went wrong");
        }
      });
      console.log(response);
      this.selectlist = response.data.courses;
    },
  },
  async created() {
    await this.extractlist();
  },
};
</script>

<style src="../css/Create.css"></style>
