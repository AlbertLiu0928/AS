// Run from the repository root:  npx tailwindcss@3 -c tools/tailwind.config.js -i tools/input.css -o assets/tailwind.css --minify
module.exports = {
  content: [
    "./index.html", "./404.html",
    "./about/**/*.html", "./ai-inspection/**/*.html", "./contact/**/*.html", "./faq/**/*.html",
    "./industries/**/*.html", "./privacy/**/*.html", "./products/**/*.html", "./terms/**/*.html",
    "./assets/site.js",
  ],
  theme: {
    extend: {
      colors: { navyMain: '#002d5a', navyLight: '#f4f7fa', navyText: '#1e293b', slateGray: '#64748b' },
      fontFamily: { sans: ['Noto Sans TC', 'sans-serif'], tech: ['Orbitron', 'sans-serif'] },
    },
  },
};
