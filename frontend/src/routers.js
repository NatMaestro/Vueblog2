import { createRouter, createWebHistory } from "vue-router";
import Home from "./components/Home.vue";
import CreateArticle from "./components/CreateArticle.vue";
import ArticleDetails from "./components/ArticleDetails.vue";
import ArticleEdit from "./components/ArticleEdit.vue";


const routes = [
    {
        path: "/",
        name: "Home",
        component: Home
    },
    {
        path: "/create",
        name: "Create",
        component: CreateArticle
    },
    {
        path: "/details/:slug",
        name: "details",
        component: ArticleDetails,
        props: true // Enable route params in components
    },
    {
        path: "/edit/:slug",
        name: "article-edit",
        component: ArticleEdit,
        props: true // Enable route params in components
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router;