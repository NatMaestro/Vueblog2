<template>
    <nav class="bg-gray-900 w-full h-[80px] flex items-center">
      <div class="flex justify-between items-center text-white w-full m-10">
        <router-link class="font-bold text-2xl" to="/">BlogApp</router-link>
  
        <div>
          <ul class="flex gap-5">
            <router-link to="/">Home</router-link>
            <router-link to="/create">Create Article</router-link>
            <!-- Logout Button -->
            <button @click="logout" class="border-2 rounded-md w-[70px] flex items-center justify-center text-red-500 border-amber-500">
              Logout
            </button>
          </ul>
        </div>
      </div>
    </nav>
  </template>
  
  <script>
    import {csrftoken} from '../csrf/csrf_token'
  export default {

    methods: {
      async logout() {
  
        try {
          // Send a POST request to the Django logout endpoint
          const response = await fetch('/accounts/logout/', {
            method: 'POST',
            headers: {
              'X-CSRFToken': csrftoken, // Include the CSRF token in the request headers
              'Content-Type': 'application/json',
            },
          });
  
          if (response.ok) {
            // If successful, redirect to the login page or home
            window.location.href = '/accounts/login/';
          } else {
            console.error('Logout failed');
          }
        } catch (error) {
          console.error('An error occurred:', error);
        }
      },
      
    },
  };
  </script>
  
  <style>
  /* Your styles here */
  </style>
  