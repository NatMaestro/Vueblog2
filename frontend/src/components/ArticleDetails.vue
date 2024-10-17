<template>
    <div class="container mx-auto m-10">
        <h3 class="text-3xl font-bold mb-3">{{ article.title }}</h3>

        <h5 class="font-bold text-xl">Author: <span class="ml-5 border-2 bg-blue-500 rounded-md">{{ article.author }}</span></h5>
        <p class="my-10 ">{{ article.body }}</p>
        <h6>Published on: <span>{{ formattedDate }}</span></h6>

        <ArticleActions v-if="IsAuthor" :slug="article.slug" />
        <!-- <p v-if="loading">Loading article...</p>
        <p v-if="error">{{ error }}</p> -->
    </div>
</template>


<script>
    import { csrftoken } from '../csrf/csrf_token'
    import ArticleActions from '../components/ArticleActions'
    export default {
        components: {
            ArticleActions
        },
        props: {
            slug: {
                type: String,
                required: true
            }
        },
        data() {
            return {
                article: {}, // Initially, it's an empty object
                requestUser: null, //
                // loading: true, // To track the loading state
                // error: null // To handle any errors
            }
        },
        methods: {
                async getArticle() {
                    try {
                        const response = await fetch(`/api/articles/`, {
                            method: 'GET',
                            headers: {
                                'Content-Type': 'application/json',
                                'X-CSRFToken': csrftoken,
                            },
                        });

                        const contentType = response.headers.get("content-type");

                        if (!response.ok) {
                            throw new Error(`HTTP error! status: ${response.status}`);
                        }

                        if (contentType && contentType.includes("application/json")) {
                            // It's JSON, so parse it
                            const articles = await response.json();

                            // Find the article with the matching slug
                            const matchedArticle = articles.find(article => article.slug === this.slug);

                            if (matchedArticle) {
                                this.article = matchedArticle;  // Set the article if found
                            } else {
                                alert("Article not found.");
                            }
                        } else {
                            // It's not JSON, likely HTML (could be an error page)
                            const errorText = await response.text();
                            console.error("Received non-JSON response:", errorText);
                            throw new Error("Expected JSON response but received HTML.");
                        }
                    } catch (error) {
                        console.error('Error fetching articles:', error.message);
                        alert("Failed to load articles.");
                    }
                },
                getUserRequest() {
                    // Fetch the authenticated user's information
                    this.requestUser = localStorage.getItem("username")
                }
            },
            computed: {
                IsAuthor() {
                    return this.article.author === this.requestUser
                },
                formattedDate() {
                const dateString = this.article.created_at;
                if (!dateString) return 'N/A';  // Handle missing date
                
                const date = new Date(dateString);  // Parse the ISO date string
                if (isNaN(date.getTime())) {
                    return 'Invalid Date';  // Handle invalid date
                }
                
                return new Intl.DateTimeFormat('en-US', {
                    year: 'numeric',
                    month: 'long',
                    day: 'numeric',
                    hour: 'numeric',
                    minute: 'numeric',
                    hour12: true,  // Display time in 12-hour format with AM/PM
                }).format(date);
            }
        },

            created() {
                this.getArticle()
                this.getUserRequest()
            },
    }
</script>

<style lang="scss" scoped>
/* Scoped styles */
</style>
