# DataGlitch Website

A clean and simple static website generator using Flask and Frozen-Flask.

## Setup

1. Clone the repository and `cd` into the project directory:

   ```bash
   git clone https://github.com/dataglitch/website.git
   cd website
   ```

2. Install dependencies:

   ```bash
   uv sync
   ```

3. Configure environment variables:
   - Copy `.env.sample` to `.env`
   - Modify the values in `.env` as needed

## Development

To run the development server locally:

```bash
uv run ./src/main.py
```

## Generate Static Site(Optional)

   To generate the static site:

   ```bash
   python freeze.py
   ```

   The static files will be generated in the `static_files` directory.

## Deployment

This project uses Cloudflare Pages for deployment. Cloudflare Pages will automatically detect any changes in the repository's `static_files` directory and trigger a new deployment. No additional workflow setup is required.

### Deployment Setup(Optional)

1. In your Cloudflare account:
   - Create a new Pages project
   - Connect your GitHub repository
   - Set the build directory to `static_files`

The deployment will automatically:

1. Detect changes in your repository
2. Deploy the contents of the `static_files` directory to your Cloudflare Pages site
