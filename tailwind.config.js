/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./index.html",
        "./src/**/*.{js,ts,jsx,tsx}",
    ],
    theme: {
        extend: {
            colors: {
                'theme-red': 'var(--color-red)',
                'theme-blue': 'var(--color-blue)',
                'theme-yellow-highlight': 'var(--color-yellow-highlight)',
                'theme-yellow-sticky': 'var(--color-yellow-sticky)',
                'theme-bg-page': 'var(--color-bg-page)',
                'theme-bg-card': 'var(--color-bg-card)',
                'theme-dark': 'var(--color-dark)',
                'theme-muted': 'var(--color-muted)',
                'theme-border-dark': 'var(--color-dark)',
                'theme-border-light': 'var(--color-border-light)',
                'theme-grid': 'var(--color-grid)',
            },
        },
    },
    plugins: [],
}
