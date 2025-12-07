#!/usr/bin/env python3
"""
Update README with latest SVG data
Automatically detects which scrapers have generated content
"""
import os
import re
import sys
from pathlib import Path
from datetime import datetime, timezone

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

def get_svg_info(svg_file: str):
    """Extract info from SVG file"""
    if not os.path.exists(svg_file):
        return None
    
    with open(svg_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Extract title lines from SVG
    title_matches = re.findall(
        r'<text x="20" y="(?:66|86|\d+)"[^>]*>([^<]+)</text>',
        content
    )
    
    # Extract link
    link_match = re.search(r'<a href="([^"]+)">', content)
    
    if title_matches:
        title = " ".join(title_matches)
    else:
        title = "No data available"
    
    link = link_match.group(1) if link_match else None
    
    # Extract header
    header_match = re.search(r'aria-label="([^"]+)"', content)
    header = header_match.group(1) if header_match else "Badge"
    
    return {"title": title, "link": link, "header": header}

def generate_readme():
    """Generate comprehensive README"""
    
    # Get current time
    current_date = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    
    # Check which scrapers have generated content
    so_svg_info = get_svg_info("assets/stupid.svg")
    gh_svg_info = get_svg_info("assets/github_repo.svg")
    
    readme = f'''# 🎲 Random Scrapers for GitHub README

A modular Python project generating daily random content SVG badges for your GitHub profile.

## 📊 Current Badges

### Stupid StackOverflow Question
![Stupid StackOverflow Question](./assets/stupid.svg)

### Random GitHub Repository
![Random GitHub Repository](./assets/github_repo.svg)

**Last Updated:** {current_date}

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
![Stupid Question](https://raw.githubusercontent.com/Alief321/random-scraper-for-github-readme/refs/heads/main/assets/stupid.svg)
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
'''
    
    return readme

def save_readme(content):
    """Save README.md"""
    with open("README.MD", "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ README.MD updated successfully!")


def main():
    readme_content = generate_readme()
    save_readme(readme_content)


if __name__ == "__main__":
    main()
