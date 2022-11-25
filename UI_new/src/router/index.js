import { createRouter, createWebHistory} from 'vue-router';
import HomeSetting from "../components/HomeSetting";
import Login from "../components/Login";
import Header from "../components/Header";
import AboutUs from "../components/AboutUs";

const routes = [
    {
        path: "/home",
        name: "home",
        component: HomeSetting,
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
