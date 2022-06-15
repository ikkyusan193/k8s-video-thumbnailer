<template v-model="$vuetify.theme.dark">
  <div>
    <v-container>
      <br />
      <!-- FAQ by mods -->
      <v-card class="mx-auto" outlined>
        <br />
        <v-row class="mx-4">
          <v-col>
            <h1 class="faq">
              Help
              <v-icon
                size="38"
                :color="!$vuetify.theme.dark ? 'black' : 'white'"
                >mdi-help-circle</v-icon
              >
              <!-- <span class="smaller">by moderators and Ajarns</span> -->
            </h1>
            <v-divider></v-divider>

            <!-- question 1 -->
            <v-row class="mx-2">
              <v-col>
                <br />
                <h2 class="faq">How to create threads?</h2>
                <p class="faq">
                  By going to the front page and clicking the 'Create a thread'
                  button. You will be redirected to the create page where you
                  will be able to create threads.
                </p>
                <p class="faq2">
                  *Note that you will be required to login into the website
                  before being able to create a thread*
                </p>
                <v-divider></v-divider>
              </v-col>
            </v-row>

            <!-- question 2 -->
            <v-row class="mx-2">
              <v-col>
                <h2 class="faq">Where do we register for our classes?</h2>
                <p class="faq">
                  For Trimester 1 of Academic Year 2021-2022, course
                  registration, tuition payment, and add/drop will take place on
                  <a
                    href="http://sky.muic.mahidol.ac.th/?data%5Btype%5D%5B%5D=login"
                    target="_blank"
                    >SKY
                  </a>
                  However, we will soon be switching over to SKY+ in Trimester
                  2.
                </p>
                <v-divider></v-divider>
              </v-col>
            </v-row>

            <!-- question 3 -->
            <v-row class="mx-2">
              <v-col>
                <h2 class="faq">
                  How can I get more information about courses or contact the
                  Ajarns?
                </h2>
                <p class="faq">
                  Please be sure to join the official MUIC Computer Science
                  Discord server to stay up to date with class information
                  and/or contact your Ajarns. You can do so by clicking
                  <a href="https://youtu.be/dQw4w9WgXcQ" target="_blank">here</a
                  >.
                </p>
              </v-col>
            </v-row>
          </v-col>
        </v-row>
        <br />
      </v-card>

      <br />
      <br />
    </v-container>
  </div>
</template>

<style src="../css/Help.css"></style>
