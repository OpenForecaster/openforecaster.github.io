# OpenForecaster Website

Blog-style website for "Scaling Open-Ended Reasoning to Predict the Future".

## Structure

- `index.md` — Main blog page (edit this to update content)
- `assets/images/` — Blog images (figures, plots, etc.)
- `assets/styles.css` — Base styles
- `assets/blog.css` — Blog-specific styles
- `_layouts/default.html` — Page template with MathJax
- `_config.yml` — Jekyll configuration

## Local Development

```bash
# Install dependencies (first time only)
bundle install

# Run local server
bundle exec jekyll serve

# Open http://localhost:4000 in your browser
```

## Features

- **Markdown support** — Write content in Markdown
- **LaTeX equations** — Use `$...$` for inline, `$$...$$` for display math
- **Collapsible spoilers** — Use `<details><summary>Title</summary>Content</details>`
- **Resource links** — arXiv, PDF, Code, Dataset, Discord at the top
- **Responsive design** — Works on mobile and desktop

## Editing the Blog

1. Open `index.md`
2. Edit the Markdown content between the `BLOG CONTENT STARTS HERE` and `BLOG CONTENT ENDS HERE` comments
3. Add images to `assets/images/` and reference them as `assets/images/filename.png`
4. Commit and push to deploy

## Collapsible Spoiler Example

```markdown
<details>
<summary>Click to expand</summary>

Hidden content goes here. You can include:
- Lists
- **Bold text**
- Code blocks
- Even images!

</details>
```

## Updating Resource Links

Edit the `href` values in `assets/site.config.js` (or directly in `index.md` hero section).
