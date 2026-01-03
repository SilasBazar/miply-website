/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./index.html",
        "./src/**/*.{js,ts,jsx,tsx}",
    ],
    theme: {
        extend: {
            fontFamily: {
                sans: ['Inter', 'sans-serif'],
                hand: ['Kalam', 'cursive'],
            },
            colors: {
                'bg-canvas': '#f8fafc',
                'ink-main': '#1e293b',
                'ink-muted': '#64748b',
                'marker-highlight': '#fcd34d',
                'pen-blue': '#3b82f6',
                'pen-red': '#ef4444',
                'grid-dot': '#cbd5e1',
            }
        },
    },
    plugins: [],
}
