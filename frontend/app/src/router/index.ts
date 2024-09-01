import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHashHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
      meta: {
        title: 'Computorv1 | Home'
      }
    },
    {
      path: '/playground',
      name: 'playground',
      component: () => import('../views/TestView.vue'),
      meta: {
        title: 'Computorv1 | Playground'
      }
    },
    {
      path: '/learn-math',
      name: 'learn-math',
      component: () => import('../views/LearnMathView.vue'),
      meta: {
        title: 'Computorv1 | Learn the Math'
      }
    }
  ]
})

router.beforeEach((to, from, next) => {
  if (to.meta.title && typeof to.meta.title === "string") {
    document.title = to.meta.title;
  }
  next();
})

export default router
