<template>
    <div class="container mx-auto p-8">
        <h1 class="text-3xl font-bold mb-5">Create New Article</h1>
        <form @submit.prevent="submitArticle">
            <!-- Title Input -->
            <div class="mb-4">
                <label for="title" class="block text-xl font-semibold mb-2">Title</label>
                <input 
                    type="text" 
                    id="title" 
                    v-model="article.title" 
                    class="w-full px-4 py-2 border rounded-md"
                    placeholder="Enter article title"
                    required
                />
            </div>
            
            <!-- Author Input -->
            <!-- <div class="mb-4">
                <label for="author" class="block text-xl font-semibold mb-2">Author</label>
                <input 
                    type="text" 
                    id="author" 
                    v-model="article.author" 
                    class="w-full px-4 py-2 border rounded-md"
                    placeholder="Enter author name"
                    required
                />
            </div> -->
            
            <!-- Body Textarea -->
            <div class="mb-6">
                <label for="body" class="block text-xl font-semibold mb-2">Article Body</label>
                <textarea 
                    id="body" 
                    v-model="article.body" 
                    class="w-full px-4 py-2 border rounded-md h-40" 
                    placeholder="Write your article content"
                    required
                ></textarea>
            </div>
            
            <!-- Submit Button -->
            <button 
                type="submit" 
                class="bg-blue-500 text-white px-6 py-2 rounded-md hover:bg-blue-600">
                Publish Article
            </button>
        </form>
    </div>
</template>

<script>
    import { csrftoken } from '../csrf/csrf_token'
    export default {
        data() {
            return {
                article: {
                    title: '',
                    body: ''
                }
            }
        },
        methods: {
            async submitArticle() {
                if (this.article.title === '' || this.article.body === '') {
                    alert('Please fill in all required fields');
                    return;
                }
                try {
                    const response = await fetch('/api/articles/', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'X-CSRFToken': csrftoken,
                        },
                        body: JSON.stringify(this.article)
                    });

                    if (!response.ok) {
                        throw new Error('Error creating article');
                    }

                    const data = await response.json();
                    console.log('Article created:', data);
                    // Optionally, navigate to a different page or show a success message
                    this.$router.push('/');  // Redirect to home after submission
                    alert('Article created successfully!');
                } catch (err) {
                    console.error(err);
                    alert('Failed to create the article');
                }
            }
        }
    }
</script>

<style lang="scss" scoped>
.container {
    max-width: 600px;
    margin: 0 auto;
}

input, textarea {
    border: 1px solid #ccc;
    outline: none;
}

input:focus, textarea:focus {
    border-color: #3182ce;
}

button:focus {
    outline: none;
}
</style>
