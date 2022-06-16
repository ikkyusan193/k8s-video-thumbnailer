<template>
<v-col justify ="space-evenly">
      <v-btn text outlined color="red" @click="deleteAllGif()"> <!-- todo -->
      Delete All
    </v-btn>
    <v-row  class="mb-6">
    <v-col
      v-for="item in info"
      :key="item.name"
      class="d-flex child-flex"
      cols= 3
    >
     <v-card flat tile justify="center" class="pa-3">
      <v-img
        :src="item.link"
        class="grey lighten-2"
        @click="deleteGif(item.name)"
      >
      </v-img>
        <span align-items:center >{{item.name}}</span>
      </v-card>
        <template v-slot:placeholder>
          <v-row
            class="fill-height ma-0"
            justify="center"
          >
          </v-row>
        </template>
    </v-col>
  </v-row>
</v-col>

</template>


<script>
import Vue from "vue";

export default {
  name: "Display",
  data() {
    return {
      info: [],
    };
  },

  created() {
  },

  watch: {
  },

  methods: {
    deleteGif(name){
      const data = { "bucket" : 'gifs', "name" : name};
      Vue.axios.post('/backend/delete', data)
    },
    deleteAllGif(){
      const data = { "bucket" : 'gifs'};
      Vue.axios.post('/backend/delete-bucket', data)
    }
  },

  mounted() {
    Vue.axios
      .get('/backend/all')
      .then(response => (this.info = response.data))
      console.log(this.info)
  }
};
</script>