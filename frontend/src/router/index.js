import Vue from "vue";
import VueRouter from "vue-router";
import axios from "axios";
import VueAxios from "vue-axios";
// import all pages here
import Home from "../components/Home";
import Display from "../components/Display";

Vue.use(VueAxios, axios);

// import { search } from "core-js/fn/symbol";

// Protocol to avoid redirection duplication
const originalPush = VueRouter.prototype.push;
VueRouter.prototype.push = function push(location) {
  return originalPush.call(this, location).catch((err) => err);
};

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/display",
    name: "Display",
    component: Display,
  },
];

const router = new VueRouter({ mode: "history", routes: routes, base: "/frontend" });

export default router;
