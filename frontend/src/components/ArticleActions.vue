<template>
    <div class="flex gap-5">
        <router-link :to="{name: 'article-edit', params:{slug:slug}}" class="flex justify-center items-center font-bold text-white w-[100px] h-10 border bg-blue-500 rounded-lg mt-5">
            Update
        </router-link>

      <button class="flex justify-center items-center font-bold text-white w-[100px] h-10 border bg-red-500 rounded-lg mt-5" @click="deleteArticle">
        Delete
      </button>
    </div>
  </template>
  
  <script>
  import { csrftoken } from '../csrf/csrf_token'
  
  export default {
    props: {
      slug: {
        type: String,
        required: true
      }
    },
    methods: {
    async deleteArticle() {
        try {
            const confirmDelete = confirm("Are you sure you want to delete this article?");
            if (!confirmDelete) return;

            const response = await fetch(`/api/articles/${this.slug}/`, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,
                },
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            alert("Article deleted successfully.");
            this.$router.push("/"); // Redirect to homepage after deletion
        } catch (error) {
            alert("Failed to delete the article. Please try again.");
        }
    }
}

  }
  </script>
  
  <style lang="scss" scoped></style>
  