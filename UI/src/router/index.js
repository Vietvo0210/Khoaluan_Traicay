import { createRouter, createWebHistory} from 'vue-router';
import HomeSetting from "../components/HomeSetting";
import Login from "../components/Login";
import AboutUs from "../components/AboutUs";
import NewView from '@/components/NewView'

const routes = [
    {
        path: "/product",
        name: "product",
        component: HomeSetting,
    },
    {
      path: "/news",
      name: "news",
      component: NewView,
    },
    {
        path: "/login",
        name: "login",
        component: Login,
    },
    {
        path: "/aboutUs",
        name: "aboutUs",
        component: AboutUs,
    }
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
});

export default router;
