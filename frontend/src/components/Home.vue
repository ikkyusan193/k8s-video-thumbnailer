

<template>
<v-row>
  <v-col justify="justify-start">
    <v-col>
    <h1>Controllers</h1>
   <v-row align="center">
    <v-btn text color="green" @click="submit_all()"> <!-- todo -->
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
          @click="submit(i)"
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
    <v-btn text color="primary"> <!-- additional features -->
      Reload
    </v-btn>
    <v-card class="pa-2" tile>
    <v-list three-line>
      <v-list-item-title class="text-h6" justify="center">
          Logs
        </v-list-item-title>
        <v-list-item 
          v-for="(item, i) in logs"
          :key="i"
        >
          <v-list-item-content>
            <v-list-item-title v-html="item.id"></v-list-item-title>
            <v-list-item-subtitle v-html="item.status"></v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
    </v-list>
  </v-card>

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
      videos: [],
      logs: []
    };
  },

  created() {
  },

  watch: {
  },

  methods: {
    submit(index){
      const data = { "input" : this.videos[index].name};
      Vue.axios.post("/backend/submit", data)
    },

    submit_all(){
      const data = { "bucket" : 'videos'};
      Vue.axios.post("/backend/submit-bucket",data)
    }

  },

  mounted() {
    Vue.axios
    .get("/backend/videos")
    .then(response => (this.videos = response.data))

    Vue.axios
    .get("/backend/jobs")
    .then(response => (this.logs = response.data))
  }
};
</script>

