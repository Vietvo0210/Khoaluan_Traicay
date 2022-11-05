import { createRouter, createWebHistory} from 'vue-router';
import HomeSetting from "../components/HomeSetting";
import Login from "../components/Login";

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
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
});

export default router;
