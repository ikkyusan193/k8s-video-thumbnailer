<style></style>

<template v-model="$vuetify.theme.dark">
  <v-container class="mx-auto" max-width="300">
    <br />
    <v-row dense>
      <v-col>
        <v-dialog v-model="zoomedImage" @click="zoomedImage = null">
          <v-card>
            <v-img :src="this.image" contain></v-img>
          </v-card>
        </v-dialog>
        <v-carousel
          cycle
          elevation="2"
          height="280px"
          hide-delimiters
          show-arrows-on-hover
        >
          <v-carousel-item v-for="a in announcements" :key="a.title">
            <v-card height="280px" outlined>
              <v-img
                :src="a.src"
                aspect-ratio="16/9"
                contain
                height="210"
                @click="zoom(a.src)"
              ></v-img>
              <v-card-title
                ><h3 class="home">{{ a.title }}</h3></v-card-title
              >
            </v-card>
          </v-carousel-item>
        </v-carousel>
      </v-col>

      <v-col>
        <v-row dense>
          <v-col>
            <v-card :to="{ name: 'FAQ' }" height="136px" outlined>
              <v-card-title><h1 class="home">FAQs</h1></v-card-title>
              <v-card-text
                ><p class="home">Frequently Asked Questions</p></v-card-text
              >
            </v-card>
          </v-col>
        </v-row>

        <v-row dense>
          <v-col>
            <v-card :to="{ name: 'Create' }" height="136px" outlined>
              <v-card-title><h1 class="home">+</h1></v-card-title>
              <v-card-text><p class="home">Create A New Thread</p></v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-col>
    </v-row>

    <br />

    <v-card outlined>
      <v-card-title><h2 class="home">Popular Tags</h2></v-card-title>
      <div class="text-center">
        <v-chip
          v-for="tag in popularTags"
          :key="tag.title"
          class="ma-2"
          small
          v-text="tag"
          @click="search(tag)"
        ></v-chip>
      </div>
    </v-card>

    <br />

    <v-card outlined>
      <v-container fluid>
        <v-row align="center">
          <v-col><h2 class="home">Threads</h2></v-col>
          <v-col class="d-flex" cols="12" sm="6">
            <v-select
              v-model="order"
              :items="ordering"
              full-width
              hide-details
              label="order"
              outlined
              prefix="MOST"
              single-line
            ></v-select>
          </v-col>
        </v-row>
      </v-container>
    </v-card>
    <v-card class="overflow-y-auto mx-auto" height="500" outlined>
      <v-container fluid>
        <v-row v-for="t in threads" :key="t.no" align="center">
          <v-col>
            <v-card outlined>
              <v-card-subtitle
                >Created By {{ t.display_name }} • {{ t.date }}
              </v-card-subtitle>
              <v-card-title
                style="font-size: x-large"
                v-text="t.title"
              ></v-card-title>
              <v-card-text>
                <v-chip
                  v-for="tag in t.tags"
                  :key="tag.title"
                  class="ma-1"
                  small
                  v-text="tag"
                ></v-chip>
              </v-card-text>
              <v-card-actions>
                <v-icon class="ml-5 mt-3 mr-3" color="grey"
                  >mdi-thumb-up-outline
                </v-icon>
                <span class="mt-3" v-text="t.likes"></span>
                <v-spacer></v-spacer>
                <v-icon class="ml-5 mt-3 mr-3" color="grey"
                  >mdi-message-outline
                </v-icon>
                <span class="mt-3" v-text="t.comment_count"></span>
                <v-spacer></v-spacer>
                <v-btn
                  :to="{ path: '/thread/' + t.thread_id }"
                  class="ml-2 mt-3"
                  text
                >
                  Continue the thread
                  <v-icon left> mdi-arrow-right</v-icon>
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-card>
  </v-container>
</template>

<script>
import Vue from "vue";

export default {
  name: "Home",
  data() {
    return {
      announcements: [
        {
          title: "Registration Day 1",
          src: require("../assets/regis1.jpg"),
        },
        {
          title: "Registration Day 2",
          src: require("../assets/regis2.jpg"),
        },
        {
          title: "Registration Day 3",
          src: require("../assets/regis3.jpg"),
        },
        {
          title: "Registration Day 4",
          src: require("../assets/regis4.jpg"),
        },
      ],
      popularTags: [],
      ordering: ["RECENT", "POPULAR", "LIKES"],
      order: "RECENT",
      threads: [],
      zoomedImage: false,
      image: "",
      selectedTag: "",
    };
  },

  created() {
    this.getInfo();
  },

  watch: {
    order: function () {
      this.getInfo();
    },
  },

  methods: {
    async getInfo() {
      let formData = new FormData();
      formData.append("order", this.order);
      let result = await Vue.axios.post("/api/home", formData);
      this.popularTags = result.data.tags;
      this.threads = result.data.threads;
      console.log(this.threads);
      console.log(result.data);
    },
    zoom(src) {
      this.zoomedImage = true;
      this.image = src;
    },
    search(tag) {
      this.$router.push("/search/" + tag + "?filter=tags");
    },
  },
};
</script>

<style src="../css/Home.css"></style>
