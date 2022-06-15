import Vue from "vue";
import VueRouter from "vue-router";
import axios from "axios";
import VueAxios from "vue-axios";
// import all pages here
import Home from "../components/Home";
import Login from "../components/Login";
import FAQ from "../components/FAQ";
import Help from "../components/Help";
import Create from "../components/Create";
import store from "../store";
import Thread from "../components/Thread";
import Search from "../components/Search";
import ChangeInformation from "../components/ChangeInformation";
import Edit from "../components/Edit";
import ModPage from "../components/modzone/ModPage";

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
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/faq",
    name: "FAQ",
    component: FAQ,
  },
  {
    path: "/help",
    name: "Help",
    component: Help,
  },
  {
    path: "/create",
    name: "Create",
    component: Create,
  },
  {
    path: "/thread/:id",
    name: "Thread",
    component: Thread,
  },
  {
    path: "/search/:keywords",
    name: "Search",
    component: Search,
    props: (route) => ({ filter: route.query.filter }),
  },
  {
    path: "/changeinfo",
    name: "ChangeInformation",
    component: ChangeInformation,
  },
  {
    path: "/modzone/main",
    name: "ModPage",
    component: ModPage,
  },
  {
    path: "/edit_thread/:id",
    name: "Edit",
    component: Edit,
  },
];

const router = new VueRouter({ mode: "history", routes: routes });

router.beforeEach(async (to, from, next) => {
  const response = await axios.get("/api/whoami").catch((error) => {
    if (error.response) {
      console.warn("something went wrong");
    }
  });
  await store.dispatch("storedinfo", response.data);
  let loggedIn = store.state.status;
  let router_list = [
    "Login",
    "Thread",
    "Create",
    "Help",
    "FAQ",
    "Home",
    "Search",
    "ChangeInformation",
    "ModPage",
    "Edit",
  ];

  if (
    (to.name === "Login" && loggedIn) ||
    !router_list.includes(to.name) ||
    (to.name === "ChangeInformation" && !loggedIn)
  ) {
    next({ name: "Home" });
  } else if (to.name === "Create" && !loggedIn) {
    next({ name: "Login" });
  } else {
    next();
  }
});

export default router;
