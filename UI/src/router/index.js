import { createRouter, createWebHistory} from 'vue-router';
import HomeSetting from "../components/HomeSetting";
import Login from "../components/Login";
import HomePredict from "../components/HomePredict";
import AboutUs from "../components/AboutUs";

const routes = [
    {
        path: "/homepredict",
        name: "homepredict",
        component: HomePredict,
    },
    {
        path: "/product",
        name: "product",
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
