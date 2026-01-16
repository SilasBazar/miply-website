# Miply Website

A modern, responsive website built with Vite and Tailwind CSS, featuring a clean whiteboard-inspired design.

## 🚀 Quick Start

### Prerequisites

Before you begin, ensure you have the following installed:
- **Node.js** (version 20 or higher recommended)
- **npm** (comes with Node.js)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/SilasBazar/miply-website.git
   cd miply-website
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

## 🛠️ Development

### Running the Development Server

To start the local development server with hot module replacement:

```bash
npm run dev
```

This will start the Vite development server, typically at `http://localhost:5173`. The page will automatically reload when you make changes to the source files.

### Project Structure

```
miply-website/
├── .github/
│   └── workflows/
│       └── deploy.yml          # GitHub Pages deployment workflow
├── src/
│   ├── main.js                 # Main JavaScript entry point
│   └── style.css               # Custom styles and Tailwind directives
├── index.html                  # Main HTML file
├── vite.config.js              # Vite configuration
├── tailwind.config.js          # Tailwind CSS configuration
├── postcss.config.js           # PostCSS configuration
└── package.json                # Project dependencies and scripts
```

## 📦 Building for Production

### Build the Site

To create an optimized production build:

```bash
npm run build
```

This command:
- Bundles and minifies all JavaScript and CSS
- Optimizes assets for production
- Outputs the built files to the `dist/` directory

### Preview the Production Build

To preview the production build locally:

```bash
npm run preview
```

This starts a local server to preview the production build before deployment.

## 🌐 Deployment

### GitHub Pages

This project is configured for automatic deployment to GitHub Pages. The deployment process is handled by GitHub Actions.

#### Automatic Deployment

Every push to the `main` branch automatically triggers a deployment:

1. GitHub Actions runs the workflow defined in `.github/workflows/deploy.yml`
2. Dependencies are installed with `npm ci`
3. The site is built with `npm run build`
4. The `dist/` directory is deployed to GitHub Pages

#### Manual Deployment

You can also trigger a manual deployment:

1. Go to the **Actions** tab in your GitHub repository
2. Select the "Deploy static content to Pages" workflow
3. Click **Run workflow**

#### Viewing the Live Site

Once deployed, your site will be available at:
```
https://silasbazar.github.io/miply-website/
```

## 🎨 Technology Stack

- **[Vite](https://vitejs.dev/)** - Fast build tool and development server
- **[Tailwind CSS](https://tailwindcss.com/)** - Utility-first CSS framework
- **[PostCSS](https://postcss.org/)** - CSS transformation tool
- **[Autoprefixer](https://github.com/postcss/autoprefixer)** - Automatic vendor prefixing

## 📝 Available Scripts

| Command | Description |
|---------|-------------|
| `npm run dev` | Start development server with hot reload |
| `npm run build` | Build for production to `dist/` directory |
| `npm run preview` | Preview production build locally |

## 🔧 Configuration

### Vite Configuration

The `vite.config.js` file includes:
- **Base path**: Set to `/miply-website/` for GitHub Pages
- **Output directory**: `dist/`
- **Entry point**: `index.html`

### Tailwind Configuration

Custom Tailwind configuration is available in `tailwind.config.js`, including:
- Custom color schemes
- Extended spacing utilities
- Custom animations and transitions

## 📄 License

This project is private and not licensed for public use.

## 🤝 Contributing

This is a private project. If you have access and would like to contribute:

1. Create a new branch for your feature
2. Make your changes
3. Test thoroughly with `npm run dev`
4. Build and verify with `npm run build` and `npm run preview`
5. Submit a pull request to the `main` branch

---

**Version**: 0.0.1
