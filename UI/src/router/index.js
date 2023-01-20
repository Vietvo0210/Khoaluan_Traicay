import { createRouter, createWebHistory} from 'vue-router';
import HomeSetting from "../components/HomeSetting";
import Login from "../components/Login";
import AboutUs from "../components/AboutUs";
import Contact from "../components/Contact";
const routes = [
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
    },
    {
        path: "/contact",
        name: "contact",
        component: Contact,
    },
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
});

export default router;

