/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html", // Path to your Django templates
    "./src/**/*.{vue,js,ts,jsx,tsx}", // Path to your Vue components
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

