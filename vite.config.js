import { defineConfig } from 'vite'

export default defineConfig({
  base: './', // Use relative base for GitHub Pages compatibility
  build: {
    outDir: 'dist',
  }
})
