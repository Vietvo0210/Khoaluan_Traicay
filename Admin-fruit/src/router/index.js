import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'dashboard',
    component: () => import('./../views/Dashboard')
  },
  {
    path: '/Product',
    name: 'product',
    component: () => import('./../views/Product')
  },
  {
    path: '/Profile',
    name: 'profile',
    component: () => import('./../views/Profile')
  },
  {
    path: '/Order',
    name: 'order',
    component: () => import('./../views/Order')
  },
  {
    path: '/Customer',
    name: 'customer',
    component: () => import('./../views/Customer')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
