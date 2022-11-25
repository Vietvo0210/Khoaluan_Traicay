import { createRouter, createWebHistory } from "vue-router";

// Default Pages
import Dashboard from "../views/Dashboard.vue";
// Component Pages
import TraiCay from "../views/components/TraiCay.vue";
import TraiCayDacSan from "../views/components/TraiCayDacSan.vue";

var appname = " - Admin Fruit";

const routes = [
  // Routes
  {
    path: "/",
    name: "Dashboard",
    component: Dashboard,
    meta: { title: "Dashboard " + appname },
  },

  // Components based Routes
  {
    path: "/component/TraiCay",
    name: "TraiCay",
    component: TraiCay,
    meta: { title: "Trái Cây" + appname },
  },
  {
    path: "/component/TraiCayDacSan",
    name: "TraiCayDacSan",
    component: TraiCayDacSan,
    meta: { title: "Trái Cây Đặc Sản" + appname },
  },
  
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,

  linkExactActiveClass: "exact-active",
});

router.beforeEach((to, from, next) => {
  document.title = to.meta.title;
  next();
});

export default router;
