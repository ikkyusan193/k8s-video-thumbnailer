

<template>
<v-row>
  <v-col justify="justify-start">
    <v-col>
    <h1>Controllers</h1>
   <v-row align="center">
    <v-btn text color="green"> <!-- todo -->
      Submit all
    </v-btn>
    <v-btn text color="primary"> <!-- additional features -->
      Add video
    </v-btn>
    <v-btn text color="error">  
      Delete video
    </v-btn>
  </v-row>
   </v-col>
     <v-card class="pa-2" tile>
    <v-list dense>
          <v-list-item-title class="text-h6" justify="center">
          Video List
        </v-list-item-title>
      <v-list-item-group
        v-model="selectedItem"
        color="primary"
      >
        <v-list-item
          v-for="(item, i) in videos"
          :key="i"
        >
          <v-list-item-content>
            <v-list-item-title v-text="item.name"></v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list-item-group>
    </v-list>
  </v-card>
  </v-col>

  <v-col>
    <h1>Status</h1>

  </v-col>
</v-row>



  
</template>

<script>
import Vue from 'vue';



export default {
  name: "Home",
  data() {
    return {
      selectedItem: 1,
      videos: []
    };
  },

  created() {
  },

  watch: {
  },

  methods: {
  },

  mounted() {
    Vue.axios
    .get("/backend/videos")
    .then(response => (this.videos = response.data))
  }
};
</script>

