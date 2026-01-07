# 🎲 Random Scrapers for GitHub README

A modular Python project generating daily random content SVG badges for your GitHub profile.

## 📊 Current Badges

###  StackOverflow Question of the Day
![StackOverflow Question of the Day](./assets/stackoverflow.svg)

### Random GitHub Repository
![Random GitHub Repository](./assets/github_repo.svg)

**Last Updated:** 2026-01-07 01:02 UTC

## 🚀 Quick Start

```bash
# Clone & install
git clone https://github.com/Alief321/random-scraper-for-github-readme.git
cd random-scraper-for-github-readme
pip install -r requirements.txt

# Generate badges
python scripts/generate_all.py stackoverflow
python scripts/generate_all.py github
python scripts/update_readme.py
```

## 🎯 Embed in Your Repo

**StackOverflow Badge:**
```markdown
![StackOverflow Question](https://raw.githubusercontent.com/Alief321/random-scraper-for-github-readme/refs/heads/main/assets/stackoverflow.svg)
```

**GitHub Repo Badge:**
```markdown
![Random Repo](https://raw.githubusercontent.com/Alief321/random-scraper-for-github-readme/refs/heads/main/assets/github_repo.svg)
```

## 📚 Documentation

- **[Quick Reference](QUICK_REFERENCE.md)** - Commands, patterns & troubleshooting
- **[Extensibility Guide](EXTENSIBILITY.md)** - Add new scrapers step-by-step
- **[Project Structure](PROJECT_STRUCTURE.md)** - Architecture & file organization

## ⚙️ Features

- ✅ Modular service-based architecture
- ✅ Easy to add new scrapers
- ✅ GitHub Actions automation (daily updates)
- ✅ Customizable SVG styles
- ✅ Comprehensive documentation

## 📝 License

MIT License - Free to use and modify!

---

**Auto-updated by GitHub Actions** | [Contributing](EXTENSIBILITY.md) | [Docs](QUICK_REFERENCE.md)
