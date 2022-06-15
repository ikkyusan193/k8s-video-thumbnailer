import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  actions: {
    storedinfo({ commit }, response) {
      commit("setStatus", response.is_logged_in);
      commit("setUserName", response.display_name);
      commit("setSkyUserName", response.sky_username);
    },
    resetinfo({ commit }) {
      commit("setStatus", false);
      commit("setUserName", null);
      commit("setSkyUserName", null);
    },
  },
  mutations: {
    setStatus(state, status) {
      this.state.status = status;
    },
    setUserName(state, login_displayname) {
      this.state.login_displayname = login_displayname;
    },
    setSkyUserName(state, login_skyusername) {
      this.state.login_skyusername = login_skyusername;
    },
  },
  state: { login_displayname: null, login_skyusername: null, status: false },
  modules: {},
});
