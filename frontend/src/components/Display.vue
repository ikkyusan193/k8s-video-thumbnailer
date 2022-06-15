<template>
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
        aspect-ratio="2"
        class="grey lighten-2"
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
</template>


<script>
import Vue from "vue";

export default {
  name: "Display",
  data() {
    return {
      info: []
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
      .get('/backend/all')
      .then(response => (this.info = response.data))
      console.log(this.info)
  }
};
</script>