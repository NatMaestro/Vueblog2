const { defineConfig } = require('@vue/cli-service');
const path = require('path');
const BundleTracker = require('webpack-bundle-tracker');
const webpack = require('webpack');

module.exports = defineConfig({
  transpileDependencies: true,
  outputDir: 'assets/bundle/', // Set the output directory for production builds
  publicPath: 'http://localhost:8080/', // Ensure this matches your dev server port and Django’s expectations

  chainWebpack: config => {
    config.optimization.splitChunks(false); // Disable code splitting for simplicity with Django

    config.plugin('BundleTracker').use(BundleTracker, [{ 
      path: path.join(__dirname, 'assets/bundle'),  // Ensure this matches your Django settings
      filename: 'webpack-stats.json',
    }]);

    config.resolve.alias.set('__STATIC__', 'static'); // Aliasing for static files
  },

  devServer: {
    port: 8080, // Ensure this matches the port you're using in `publicPath`
    headers: { 'Access-Control-Allow-Origin': '*' }, // Allow cross-origin requests for local dev
    proxy: {
      // Proxy API calls to Django during development
      '/api': {
        target: 'http://localhost:8000', // Django's local server port
        changeOrigin: true,
      },
    },
    hot: true, // Enable hot module reloading
    static: {
      watch: true, // Enable watching static files
    },
    client: {
      overlay: {
        warnings: false,
        errors: true,
      },
    },
  },

  configureWebpack: {
    entry: './src/main.js', // Ensure this is pointing to your Vue entry point
    output: {
      path: path.resolve(__dirname, 'assets/bundle/'), // The output path
      filename: '[name]-[hash].js', // Filename for hashed bundle output
    },
    plugins: [
      new webpack.DefinePlugin({
        // Define Vue feature flags here
        __VUE_OPTIONS_API__: JSON.stringify(true),
        __VUE_PROD_DEVTOOLS__: JSON.stringify(false),
        __VUE_PROD_HYDRATION_MISMATCH_DETAILS__: JSON.stringify(false) // Add the flag you encountered
      })
    ],
  },
});
