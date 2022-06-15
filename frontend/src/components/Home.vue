<template>
  <!-- <v-row>
    <v-col
      v-for="n in 12"
      :key="n"
      class="d-flex child-flex"
      cols="4"
    >
     <v-card flat tile>
      <v-img
        :src="`https://picsum.photos/500/300?image=${n * 5 + 10}`"
        :lazy-src="`https://picsum.photos/10/6?image=${n * 5 + 10}`"
        aspect-ratio="2.5"
        class="grey lighten-2"
      >
      </v-img>
        <span align-items:center ></span>
              </v-card>
        <template v-slot:placeholder>
          <v-row
            class="fill-height ma-0"
            justify="center"
          >
          </v-row>
        </template>
      
    </v-col>
  </v-row> -->
  <h6>{{info}}</h6>
</template>

    <!-- <v-col>
        <v-btn text>
      Normal
    </v-btn>
        <v-btn text>
      Normal
    </v-btn>
  </v-col>
  </v-row>
</template> -->

<script>
// import Vue from "vue";

export default {
  name: "Home",
  data() {
    return {
      info: {}
    };
  },

  created() {
  },

  watch: {
  },

  methods: {
  },

  mounted() {
    this.$axios
      .get('/api/gifs')
      .then(response => (this.info = response.data.data))
      console.log(this.info)
  }
};
</script>

