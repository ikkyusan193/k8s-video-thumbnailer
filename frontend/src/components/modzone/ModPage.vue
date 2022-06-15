<template>
  <v-container>
    <br />
    <v-row dense>
      <v-col>
        <AddTags />
        <br />
        <CombineThreads />
      </v-col>

      <v-col>
        <ModPassword />
        <br />
        <MakeMod />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import AddTags from "./AddTags";
import CombineThreads from "./CombineThreads";
import MakeMod from "./MakeMod";
import ModPassword from "./ChangePassword";

export default {
  name: "ModPage",
  components: { MakeMod, ModPassword, CombineThreads, AddTags },
};
</script>

<style scoped></style>
