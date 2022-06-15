<template v-model="$vuetify.theme.dark">
  <div>
    <v-container>
      <br />
      <v-dialog v-model="future_update" max-width="300">
        <v-card>
          <v-card-title class="text-center ml-5" style="font-size: 18px"
            >This feature will be coming<br />soon in the next
            update</v-card-title
          >
        </v-card>
      </v-dialog>
      <v-card class="mx-auto" outlined max-width="800">
        <v-dialog
          type="error"
          dense
          outlined
          v-model="log_in_alert"
          dismissible
          max-width="400"
          ><v-card height="150"
            ><v-card-title class="justify-center" style="font-size: 20px"
              ><span class="mt-2"
                >Please log in to like/comment/reply</span
              ></v-card-title
            >
            <v-card-actions class="justify-space-around mt-3">
              <v-btn text outlined :to="{ name: 'Login' }"> Log in </v-btn>
              <v-btn text outlined @click="log_in_alert = false"> close </v-btn>
            </v-card-actions></v-card
          >
        </v-dialog>
        <v-card-subtitle
          >Created By {{ this.thread_username }} • {{ this.thread_date }}
          <v-btn
            icon
            absolute
            right
            class="mr-10"
            v-if="this.thread_username === this.current_user"
            @click="$router.push({ name: 'Edit', params: { id: thread_id } })"
            ><v-icon color="grey" class="mt-1">mdi-border-color</v-icon></v-btn
          >
          <v-dialog
            v-model="delete_thread"
            persistent
            max-width="300"
            v-if="this.thread_username === this.current_user"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-btn v-bind="attrs" v-on="on" icon absolute right>
                <v-icon color="grey">mdi-trash-can-outline</v-icon></v-btn
              >
            </template>
            <v-card>
              <v-card-title class="justify-center"
                >Delete the thread?</v-card-title
              >
              <v-card-actions class="justify-space-around">
                <v-btn text outlined @click="deletethread()"> YES </v-btn>
                <v-btn text outlined @click="delete_thread = false" color="red">
                  NO
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-card-subtitle>
        <v-card-title class="text-h4 pt-0" v-text="thread_title"></v-card-title>
        <v-card-text>
          <v-chip
            v-for="tag in thread_tags"
            :key="tag.title"
            v-text="tag"
            small
            class="mr-1"
          ></v-chip>
        </v-card-text>
        <v-card-text class="text-h5 ml-1">{{ thread_body }}</v-card-text>
        <v-card-actions>
          <v-btn class="ml-2 mt-3 mr-6" text @click="likethread()">
            <v-icon class="mr-5" color="grey" v-if="thread_is_liked"
              >mdi-thumb-up</v-icon
            >
            <v-icon class="mr-5" color="grey" v-else
              >mdi-thumb-up-outline</v-icon
            >
            <span v-text="thread_likes" style="font-size: 15px"></span>
          </v-btn>
          <v-spacer></v-spacer>
          <v-icon class="ml-2 mt-3 mr-5" color="grey"
            >mdi-message-outline</v-icon
          >
          <span
            v-text="thread_comment_count"
            class="ml-2 mt-3 mr-6"
            style="font-size: 15px"
          ></span>
          <v-spacer></v-spacer>
          <v-btn class="ml-2 mt-3 mr-6" text @click="future_update = true">
            <v-icon class="mr-1" color="grey">mdi-alert-octagon</v-icon>
            <span>Report</span>
          </v-btn>
        </v-card-actions>
      </v-card>

      <br />
      <v-card class="overflow-y-auto mx-auto" outlined max-width="800">
        <v-row class="mx-6 mt-6" no-gutters>
          <v-col cols="11">
            <v-text-field
              label="Please log in to comment"
              outlined
              clearable
              disabled
              v-if="!this.$store.state.status"
            ></v-text-field>
            <v-textarea
              v-else
              label="Comment"
              outlined
              clearable
              rows="1"
              v-model="comment_thread"
              clear-icon="mdi-close"
              @keydown.enter="addcomment"
            ></v-textarea>
          </v-col>
          <v-col cols="1">
            <v-btn v-if="!this.$store.state.status" text height="55" disabled
              ><v-icon large>mdi-send</v-icon></v-btn
            >
            <v-btn
              v-else
              text
              height="55"
              color="purple darken-3"
              :disabled="comment_thread === ''"
              @click="addcomment()"
              ><v-icon large>mdi-send</v-icon></v-btn
            >
          </v-col>
        </v-row>
        <div
          class="mx-6 mb-2"
          v-for="comment in thread_comments"
          :key="comment.yes"
        >
          <v-card outlined>
            <v-card-subtitle style="font-weight: bold"
              >{{ comment.sender
              }}<span
                style="color: dodgerblue"
                v-if="comment.sender === thread_username"
              >
                OP</span
              >
              <v-dialog
                v-model="delete_comment"
                persistent
                max-width="300"
                v-if="comment.sender === current_user && !comment.deleted"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-btn v-bind="attrs" v-on="on" icon x-small absolute right>
                    <v-icon color="grey">mdi-trash-can-outline</v-icon></v-btn
                  >
                </template>
                <v-card>
                  <v-card-title class="justify-center"
                    >Delete the comment?</v-card-title
                  >
                  <v-card-actions class="justify-space-around">
                    <v-btn
                      text
                      outlined
                      @click="deletecomment(comment.comment_id)"
                    >
                      YES
                    </v-btn>
                    <v-btn
                      text
                      outlined
                      @click="delete_comment = false"
                      color="red"
                    >
                      NO
                    </v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>
            </v-card-subtitle>
            <v-card-text class="ml-1"
              ><span
                class="font-italic"
                style="color: darkgrey"
                v-if="comment.deleted"
                >{{ comment.body }}</span
              ><span v-else>{{ comment.body }}</span></v-card-text
            >
            <v-card-actions v-if="!comment.deleted">
              <v-btn
                small
                class="ml-2 mr-6"
                text
                @click="likecomment(comment.comment_id)"
              >
                <v-icon small class="mr-5" color="grey" v-if="comment.is_liked"
                  >mdi-thumb-up</v-icon
                ><v-icon small class="mr-5" color="grey" v-else
                  >mdi-thumb-up-outline</v-icon
                >
                <span v-text="comment.likes"></span>
              </v-btn>
              <v-spacer></v-spacer>
              <v-btn
                small
                class="ml-2 mr-6"
                text
                @click="comment.reply = !comment.reply"
              >
                <v-icon small class="mr-5" color="grey">mdi-reply</v-icon>
                <span>Reply</span>
              </v-btn>
              <v-spacer></v-spacer>
              <v-btn small class="ml-2" text @click="future_update = true">
                <v-icon small class="mr-1" color="grey"
                  >mdi-alert-octagon</v-icon
                >
                <span>Report</span>
              </v-btn>
            </v-card-actions>
            <v-row class="mx-6 mt-6" no-gutters v-if="comment.reply">
              <v-col cols="11">
                <v-text-field
                  v-if="!checkstatus()"
                  label="Please log in to comment"
                  outlined
                  clearable
                  dense
                  disabled
                  v-model="comment_reply"
                ></v-text-field>
                <v-textarea
                  v-else
                  label="Comment"
                  outlined
                  clearable
                  dense
                  rows="1"
                  clear-icon="mdi-close"
                  @keydown.enter="addreply(comment.comment_id, comment.sender)"
                  v-model="comment_reply"
                ></v-textarea>
              </v-col>
              <v-col cols="1">
                <v-btn
                  v-if="!checkstatus()"
                  text
                  height="41"
                  color="purple darken-3"
                  disabled
                  ><v-icon large>mdi-send</v-icon></v-btn
                ><v-btn
                  v-else
                  text
                  height="41"
                  color="purple darken-3"
                  :disabled="comment_reply === ''"
                  @click="addreply(comment.comment_id, comment.sender)"
                  ><v-icon large>mdi-send</v-icon></v-btn
                >
              </v-col>
            </v-row>
          </v-card>
          <div v-for="subcom in comment.replies" :key="subcom.yes">
            <div class="ml-10">
              <v-card-subtitle style="font-weight: bold; color: dimgray"
                >{{ subcom.sender
                }}<span
                  style="color: dodgerblue"
                  v-if="subcom.sender === thread_username"
                >
                  OP</span
                ><v-dialog
                  v-model="delete_reply"
                  persistent
                  max-width="300"
                  v-if="subcom.sender === current_user && !subcom.deleted"
                >
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn
                      v-bind="attrs"
                      v-on="on"
                      icon
                      x-small
                      absolute
                      right
                      class="mr-6"
                    >
                      <v-icon color="grey">mdi-trash-can-outline</v-icon></v-btn
                    >
                  </template>
                  <v-card>
                    <v-card-title class="justify-center"
                      >Delete the reply?</v-card-title
                    >
                    <v-card-actions class="justify-space-around">
                      <v-btn
                        text
                        outlined
                        @click="deletecomment(subcom.comment_id)"
                      >
                        YES
                      </v-btn>
                      <v-btn
                        text
                        outlined
                        @click="delete_reply = false"
                        color="red"
                      >
                        NO
                      </v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog></v-card-subtitle
              >
              <v-card-text class="ml-1"
                ><span
                  class="font-italic"
                  style="color: darkgrey"
                  v-if="subcom.deleted"
                  >{{ subcom.body }}</span
                ><span v-else style="color: dimgray">{{
                  subcom.body
                }}</span></v-card-text
              >
              <v-card-actions v-if="!subcom.deleted">
                <v-btn
                  small
                  class="ml-2 mr-6"
                  text
                  @click="likecomment(subcom.comment_id)"
                >
                  <v-icon small class="mr-5" color="grey" v-if="subcom.is_liked"
                    >mdi-thumb-up</v-icon
                  ><v-icon small class="mr-5" color="grey" v-else
                    >mdi-thumb-up-outline</v-icon
                  >
                  <span v-text="subcom.likes"></span>
                </v-btn>
                <v-spacer></v-spacer>
                <v-btn
                  small
                  class="ml-2 mr-6"
                  text
                  @click="subcom.reply = !subcom.reply"
                >
                  <v-icon small class="mr-5" color="grey">mdi-reply</v-icon>
                  <span>Reply</span>
                </v-btn>
                <v-spacer></v-spacer>
                <v-btn
                  small
                  class="ml-2 mr-1"
                  text
                  @click="future_update = true"
                >
                  <v-icon small class="mr-1" color="grey"
                    >mdi-alert-octagon</v-icon
                  >
                  <span>Report</span>
                </v-btn>
              </v-card-actions>
              <v-row class="mx-6 mt-6" no-gutters v-if="subcom.reply">
                <v-col cols="11">
                  <v-text-field
                    v-if="!checkstatus()"
                    label="Please log in to comment"
                    disabled
                    outlined
                    clearable
                    dense
                  ></v-text-field>
                  <v-textarea
                    v-else
                    label="Comment"
                    outlined
                    clearable
                    dense
                    rows="1"
                    v-model="comment_reply"
                    clear-icon="mdi-close"
                    @keydown.enter="addreply(subcom.comment_id, subcom.sender)"
                  ></v-textarea>
                </v-col>
                <v-col cols="1">
                  <v-btn
                    v-if="!checkstatus()"
                    text
                    height="41"
                    color="purple darken-3"
                    disabled
                    ><v-icon large>mdi-send</v-icon></v-btn
                  >
                  <v-btn
                    v-else
                    text
                    height="41"
                    :disabled="comment_reply === ''"
                    color="purple darken-3"
                    @click="addreply(subcom.comment_id, subcom.sender)"
                    ><v-icon large>mdi-send</v-icon></v-btn
                  >
                </v-col>
              </v-row>
            </div>
          </div>
        </div>
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
  name: "Thread",
  data: () => ({
    current_user: null,
    thread_status: true,
    thread_likes: 0,
    thread_is_liked: false,
    thread_comment_count: 0,
    thread_id: "",
    thread_tags: [],
    thread_username: "",
    thread_date: "",
    thread_title: "",
    thread_body: "",
    comment_thread: "",
    comment_reply: "",
    thread_comments: [],
    log_in_alert: false,
    delete_thread: false,
    delete_comment: false,
    delete_reply: false,
    future_update: false,
  }),

  methods: {
    checkstatus() {
      return this.$store.state.status;
    },

    async getalldata() {
      const response = await axios
        .get("/api/getthread?thread_id=" + this.$route.params.id)
        .catch((error) => {
          if (error.response) {
            console.warn("something went wrong");
          }
        });
      console.log(response.data.comments);
      this.current_user = this.$store.state.login_displayname;
      this.thread_id = response.data.thread_id;
      this.thread_title = response.data.title;
      this.thread_body = response.data.body;
      this.thread_username = response.data.author;
      this.thread_tags = response.data.tags;
      this.thread_date = response.data.timestamp;
      this.thread_status = response.data.status;
      this.thread_likes = response.data.likes;
      this.thread_comments = response.data.comments;
      this.thread_comment_count = response.data.comments.length;
      this.thread_is_liked = response.data.is_liked;
      if (!response.data.status) {
        await this.$router.push("/");
      }
      this.comment_thread = "";
      this.comment_reply = "";
    },

    async addcomment() {
      let formData = new FormData();
      formData.append("thread_id", this.thread_id);
      formData.append("username", this.$store.state.login_skyusername);
      formData.append("comment_body", this.comment_thread);
      // formData.append("comment_id", this.comment_id);
      const response = await axios
        .post("/api/new_comment", formData)
        .catch((error) => {
          if (error.response) {
            console.warn("something went wrong");
          }
        });
      console.log(response.data.comments);
      if (!response.data.status) {
        console.warn("Failed to send comment");
      } else {
        await this.getalldata();
      }
    },

    async addreply(stored_id, stored_username) {
      let formData = new FormData();
      formData.append("thread_id", this.thread_id);
      formData.append("username", this.$store.state.login_skyusername);
      formData.append(
        "comment_body",
        `@${stored_username} ${this.comment_reply}`
      );
      formData.append("parent_id", stored_id);
      const response = await axios
        .post("/api/new_comment", formData)
        .catch((error) => {
          if (error.response) {
            console.warn("something went wrong");
          }
        });
      console.log(response.data);
      if (!response.data.status) {
        console.warn("Failed to send comment");
      } else {
        await this.getalldata();
      }
    },

    async likethread() {
      let formData = new FormData();
      formData.append("thread_id", this.thread_id);
      formData.append("username", this.$store.state.login_skyusername);
      const response = await axios
        .post("/api/like_thread", formData)
        .catch((error) => {
          if (error.response) {
            console.warn("something went wrong");
          }
        });
      console.log(response.data);
      if (!response.data.status) {
        console.warn("Failed to send comment");
        this.log_in_alert = true;
      } else {
        await this.getalldata();
      }
    },

    async likecomment(comment_id) {
      let formData = new FormData();
      formData.append("comment_id", comment_id);
      formData.append("username", this.$store.state.login_skyusername);
      const response = await axios
        .post("/api/like_comment", formData)
        .catch((error) => {
          if (error.response) {
            console.warn("something went wrong");
          }
        });
      console.log(response.data);
      if (!response.data.status) {
        console.warn("Failed to send comment");
        this.log_in_alert = true;
      } else {
        await this.getalldata();
      }
    },

    async deletethread() {
      let formData = new FormData();
      formData.append("thread_id", this.thread_id);
      formData.append("sky_username", this.$store.state.login_skyusername);
      const response = await axios
        .post("/api/deletethread", formData)
        .catch((error) => {
          if (error.response) {
            console.warn("something went wrong");
          }
        });
      console.log(response.data);
      if (!response.data.status) {
        console.warn("Failed to send comment");
      } else {
        await this.$router.push("/");
      }
    },

    async deletecomment(comment_id) {
      let formData = new FormData();
      formData.append("comment_id", comment_id);
      formData.append("sky_username", this.$store.state.login_skyusername);
      const response = await axios
        .post("/api/delete_comment", formData)
        .catch((error) => {
          if (error.response) {
            console.warn("something went wrong");
          }
        });
      console.log(response.data);
      if (!response.data.status) {
        console.warn("Failed to delete comment");
      } else {
        await this.getalldata();
      }
      this.delete_comment = false;
      this.delete_reply = false;
    },
  },

  async created() {
    await this.getalldata();
  },
};
</script>

<style src="../css/Thread.css"></style>
