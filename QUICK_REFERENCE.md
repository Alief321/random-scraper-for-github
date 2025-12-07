# 🚀 Quick Reference

## ⚡ Common Commands

```bash
# Generate StackOverflow badge
python scripts/generate_all.py stackoverflow

# Generate GitHub badge
python scripts/generate_all.py github

# Update README with latest data
python scripts/update_readme.py

# Generate both + update README
python scripts/generate_all.py stackoverflow && \
python scripts/generate_all.py github && \
python scripts/update_readme.py
```

## 📋 File Locations

| Type       | Location                           | Purpose                    |
| ---------- | ---------------------------------- | -------------------------- |
| Scrapers   | `src/services/`                    | Fetch data implementations |
| Generators | `src/generators/svg_generators.py` | SVG creation               |
| Utils      | `src/utils/svg.py`                 | SVG helpers                |
| Detector   | `src/utils/stupid_detector.py`     | Stupid pattern detection   |
| Scripts    | `scripts/`                         | CLI entry points           |
| Output     | `assets/`                          | Generated SVG badges       |
| Config     | `requirements.txt`                 | Dependencies               |
| Docs       | `README.MD`, `EXTENSIBILITY.md`    | Documentation              |

## 🔧 Quick Customization

### Change SVG Colors

**File:** `src/generators/svg_generators.py`

```python
colors={
    "bg": "#your_color",
    "accent": "#your_color",
    "text_color": "#your_color",
    "link_color": "#your_color"
}
```

### Change GitHub Actions Schedule

**File:** `.github/workflows/daily_stupid_svg.yml`

```yaml
cron: '0 0 * * *' # Change this cron expression
```

### Add Stupid Question Patterns

**File:** `src/utils/stupid_detector.py`

```python
from src.utils.stupid_detector import get_detector

detector = get_detector()
detector.add_custom_patterns([
    "your_keyword",
    "another_keyword"
])
```

**Total Patterns:** 110+ across 13 categories  
**Documentation:** See `docs/STUPID_DETECTOR.md` for full pattern list

## 📦 Add New Dependency

1. Edit `requirements.txt`:

   ```
   your-package>=1.0.0
   ```

2. Install locally:
   ```bash
   pip install -r requirements.txt
   ```

## 🧪 Testing New Scraper

1. Create scraper in `src/services/my_scraper.py`
2. Create generator in `src/generators/svg_generators.py`
3. Register in `__init__.py` files
4. Add to SCRAPERS dict
5. Test:
   ```bash
   python scripts/generate_all.py my_service
   python scripts/update_readme.py
   ```

## 📊 SVG Output Files

- `assets/stupid.svg` - StackOverflow badge
- `assets/github_repo.svg` - GitHub badge
- `assets/your_service.svg` - Custom scraper (example)

## 🎯 Data Structure

Every scraper must return:

```python
{
    "title": "Main content",     # Required
    "link": "https://url",       # Required
    # Additional fields optional:
    "field_name": "value"
}
```

## 🐛 Troubleshooting

| Issue                | Solution                                          |
| -------------------- | ------------------------------------------------- |
| Import errors        | Check `src/*/__init__.py` has exports             |
| SVG not generated    | Ensure scraper returns Dict with `title` & `link` |
| README not updated   | Check SVG files exist in `assets/`                |
| GitHub Actions fails | Check dependencies in `requirements.txt`          |

## 📚 Documentation Map

- **README.MD** - Start here! Main guide
- **EXTENSIBILITY.md** - How to add new scrapers
- **PROJECT_STRUCTURE.md** - Architecture & file organization
- **QUICK_REFERENCE.md** - This file!

## 💡 Common Patterns

### Simple HTTP Scraper

```python
import requests
from src.base import BaseScraper

class MyScraper(BaseScraper):
    def fetch(self):
        try:
            r = requests.get("https://api.example.com/data")
            data = r.json()
            return {
                "title": data["title"],
                "link": data["url"]
            }
        except:
            return None
```

### RSS Feed Scraper

```python
import feedparser
from src.base import BaseScraper

class MyFeedScraper(BaseScraper):
    def fetch(self):
        try:
            feed = feedparser.parse("https://example.com/feed.xml")
            entry = feed.entries[0]
            return {
                "title": entry.title,
                "link": entry.link
            }
        except:
            return None
```

### API Scraper with Auth

```python
import requests
from src.base import BaseScraper

class AuthScraper(BaseScraper):
    def fetch(self):
        try:
            headers = {"Authorization": "Bearer YOUR_TOKEN"}
            r = requests.get("https://api.example.com/data", headers=headers)
            data = r.json()
            return {
                "title": data["title"],
                "link": data["url"]
            }
        except:
            return None
```

## 🎨 Preset Color Schemes

### Dark Theme (Default)

```python
{
    "bg": "#0f172a",
    "accent": "#ffb86b",
    "text_color": "#e6eef8",
    "link_color": "#9be7ff"
}
```

### GitHub Dark

```python
{
    "bg": "#0d1117",
    "accent": "#58a6ff",
    "text_color": "#c9d1d9",
    "link_color": "#79c0ff"
}
```

### Neon

```python
{
    "bg": "#0a0e27",
    "accent": "#ff006e",
    "text_color": "#00f5ff",
    "link_color": "#ffbe0b"
}
```

### Minimal

```python
{
    "bg": "#ffffff",
    "accent": "#000000",
    "text_color": "#333333",
    "link_color": "#0066cc"
}
```

## 🔗 Useful Links

- [Feedparser Docs](https://feedparser.readthedocs.io/)
- [Requests Docs](https://requests.readthedocs.io/)
- [BeautifulSoup Docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [SVG Tutorial](https://developer.mozilla.org/en-US/docs/Web/SVG)

---

**Last Updated:** 2025-12-07
