import { defineConfig } from 'vite'
import { resolve } from 'path'
import fs from 'fs'

const htmlFiles = fs.readdirSync(__dirname).filter(file => file.endsWith('.html'));
const input = {};
htmlFiles.forEach(file => {
  const name = file.replace(/\.html$/, '');
  input[name] = resolve(__dirname, file);
});

export default defineConfig({
  base: '/miply-website/',
  build: {
    outDir: 'dist',
    rollupOptions: {
      input,
    },
  },
})