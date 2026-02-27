import { defineConfig } from 'vite'
import { resolve } from 'path'

export default defineConfig({
  base: '/miply-website/',
  build: {
    outDir: 'dist',
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        whatIsMip: resolve(__dirname, 'what-is-mip.html'),
        guild: resolve(__dirname, 'guild.html'),
        buildLog: resolve(__dirname, 'build-log.html'),
        join: resolve(__dirname, 'join.html'),
      },
    },
  },
})