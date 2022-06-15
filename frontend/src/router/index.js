import Vue from "vue";
import VueRouter from "vue-router";
import axios from "axios";
import VueAxios from "vue-axios";
// import all pages here

Vue.use(VueAxios, axios);
Vue.use(VueRouter);


const routerOptions = [
  { path: "/", component: "Home" },
  { path: "/display", component: "Display"},
];

const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => import(`../components/${route.component}.vue`)
  };
});

const router = new VueRouter({ mode: "history", routes: routes });

export default router;
