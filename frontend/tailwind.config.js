/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,jsx}'],
  theme: {
    extend: {
      colors: {
        terracota: '#732E1A',
        arcilla: '#6E2D1B',
        siena: '#A0522D',
        crema: '#F3EBE1',
        'crema-claro': '#F8F1E9',
        beige: '#ECE2D0',
      },
      fontFamily: {
        sans: ['"Plus Jakarta Sans"', 'system-ui', 'sans-serif'],
      },
      borderRadius: {
        '4xl': '2rem',
      },
    },
  },
  plugins: [],
}
