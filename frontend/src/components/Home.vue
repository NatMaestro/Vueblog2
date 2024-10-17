<template>
    <div class="container mx-auto max-w-max h-[900px]">
      <h1 class="text-3xl font-bold mb-4 text-center my-10">All Articles</h1>
      <div v-if="articles.length" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 justify-between container">
        <div
          v-for="(article, index) in articles"
          :key="article.id"
          :class="[bgColors[index % bgColors.length], 'rounded-lg shadow-md p-6 text-white h-[300px]']"
        >
        <span class="flex gap-2 text-gray-950 font-bold items-center">Author: <p :class="[bgColors[index % bgColors.length + 1],'text-sm border-2 rounded-md w-fitp-[3px]']">{{ article.author }}</p></span>
            <router-link :to="{ name: 'details', params: { slug: article.slug } }" class="flex flex-col h-full">
            <h2 class="text-2xl font-semibold mt-10">{{ article.title }}</h2>
            </router-link>
          <!-- <p class="text-sm truncate">Published on: {{ formatDate(article.created_at) }}</p>
          <p class="mt-2">{{ article.body }}</p> -->
        </div>
      </div>
      <p v-else class="text-lg">No articles available.</p>
    </div>
  </template>
  
  <script>
    import { csrftoken } from '../csrf/csrf_token'
  
    export default {
      data() {
        return {
          articles: [],
          bgColors: [
            'bg-red-400',
            'bg-yellow-800',
            'bg-green-700',
            'bg-blue-700',
            'bg-purple-800',
            'bg-pink-800',
          ],
        }
      },
      methods: {
        async getAllArticles() {
          const response = await fetch('/api/articles/', {
            method: 'GET',
            headers: {
              'Content-Type': 'application/json',
              'X-CSRFToken': csrftoken,
            },
          })
          if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`)
          }
          const data = await response.json()
          console.log('data>>>', data)
          this.articles.push(...data)
        },
      },
      created() {
        this.getAllArticles()
      },
    }
  </script>
  
  <style scoped>
  /* Scoped styles are not needed since Tailwind classes handle most styling */
  </style>
  