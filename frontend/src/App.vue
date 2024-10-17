<template>
  <div id="app">
    <Navbar/>
    <router-view/>

  </div>
  <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
</template>

<script>
import Navbar from './components/Navbar.vue'
// import { csrftoken } from '../csrf/csrf_token'

export default {
  name: 'App',
  components: {
    Navbar
  },
  methods: {
        async getUser() {
          const response = await fetch('api/user/', {
            method: 'GET',
            headers: {
              'Content-Type': 'application/json',
              // 'X-CSRFToken': csrftoken,
            },
          })
          if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`)
          }
          const data = await response.json()
          console.log('data>>>', data)
          const username = data["username"]
          localStorage.setItem("username", username)
          // this.articles.push(...data)
        },
      },
      created() {
        this.getUser()
      }
}
</script>

<style>

</style>
