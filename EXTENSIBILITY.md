# 🧩 Extensibility Guide

Panduan lengkap untuk menambahkan scraper baru ke proyek ini.

## 🏗️ Arsitektur Proyek

Proyek ini menggunakan **service-based architecture** dengan dua abstract base classes:

1. **`BaseScraper`** - Interface untuk semua scraper
2. **`SVGGenerator`** - Interface untuk generator SVG

## ✨ Menambahkan Scraper Baru

### Step 1: Buat Scraper Service

Buat file baru di `src/services/your_service.py`:

```python
from typing import Optional, Dict, Any
from src.base import BaseScraper

class YourScraper(BaseScraper):
    """Deskripsi scraper Anda"""

    def __init__(self):
        super().__init__("your_service")

    def fetch(self) -> Optional[Dict[str, Any]]:
        """
        Fetch data dari sumber Anda

        Returns:
            Dict dengan minimal keys: title, link
            Bisa tambah key tambahan sesuai kebutuhan
        """
        try:
            # Your fetching logic here
            title = "Fetched content"
            link = "https://example.com"

            return {
                "title": title,
                "link": link,
                "custom_field": "optional data"
            }
        except Exception as e:
            print(f"Error: {e}")
            return None

    def get_display_name(self) -> str:
        """Return display name untuk header SVG"""
        return "📌 Your Custom Badge"
```

### Step 2: Buat SVG Generator

Edit atau extend `src/generators/svg_generators.py`:

```python
from src.base import SVGGenerator
from src.utils.svg import generate_svg
from typing import Dict, Any

class YourSVGGenerator(SVGGenerator):
    """Generator untuk your_service"""

    def generate(self, item: Dict[str, Any]) -> str:
        """Generate SVG dari item data"""
        return generate_svg(
            title=item.get("title", "No title"),
            link=item.get("link", "https://example.com"),
            header_text="📌 Your Custom Badge",
            colors={
                "bg": "#1a1a1a",
                "accent": "#ff6b6b",
                "text_color": "#ffffff",
                "link_color": "#4ecdc4"
            }
        )
```

### Step 3: Register Services

**Edit `src/services/__init__.py`:**

```python
from src.services.stackoverflow import StackOverflowScraper
from src.services.github import GitHubRepoScraper
from src.services.your_service import YourScraper

__all__ = [
    "StackOverflowScraper",
    "GitHubRepoScraper",
    "YourScraper"  # <-- Add your scraper
]
```

**Edit `src/generators/__init__.py`:**

```python
from src.generators.svg_generators import (
    StackOverflowSVGGenerator,
    GitHubRepoSVGGenerator,
    YourSVGGenerator  # <-- Add your generator
)

__all__ = [
    "StackOverflowSVGGenerator",
    "GitHubRepoSVGGenerator",
    "YourSVGGenerator"  # <-- Add your generator
]
```

### Step 4: Add to Main Script

Edit `scripts/generate_all.py`:

```python
from src.services.your_service import YourScraper
from src.generators.svg_generators import YourSVGGenerator

SCRAPERS = {
    "stackoverflow": {
        "scraper": StackOverflowScraper,
        "generator": StackOverflowSVGGenerator,
        "output_file": "stackoverflow.svg"
    },
    "github": {
        "scraper": GitHubRepoScraper,
        "generator": GitHubRepoSVGGenerator,
        "output_file": "github_repo.svg"
    },
    "your_service": {  # <-- Add your service
        "scraper": YourScraper,
        "generator": YourSVGGenerator,
        "output_file": "your_badge.svg"
    }
}
```

### Step 5: Test

```bash
# Test scraper
python scripts/generate_all.py your_service

# Update README
python scripts/update_readme.py
```

## 🎨 SVG Customization

### Available Colors

```python
colors = {
    "bg": "#0f172a",        # Background color
    "accent": "#ffb86b",    # Header text color
    "text_color": "#e6eef8", # Main text color
    "link_color": "#9be7ff"  # Link color
}
```

### SVG Generation Options

```python
generate_svg(
    title="Main content",
    link="https://example.com",
    header_text="📌 Badge Title",
    width=680,              # SVG width
    max_lines=6,            # Max title lines
    line_height=20,         # Height per line
    padding=20,             # Content padding
    colors=colors           # Custom colors
)
```

## 🔄 Data Format

Semua scraper harus return dict dengan struktur:

```python
{
    "title": str,           # Required: Main content
    "link": str,            # Required: URL target
    # Optional fields:
    "custom_field": any     # Tambahan sesuai kebutuhan
}
```

## 📋 Contoh Scraper Sederhana

### Random Quote Scraper

```python
import requests
from src.base import BaseScraper

class QuoteScraper(BaseScraper):
    def __init__(self):
        super().__init__("quote")

    def fetch(self):
        try:
            response = requests.get("https://api.quotable.io/random")
            data = response.json()
            return {
                "title": f'"{data["content"]}" - {data["author"]}',
                "link": "https://quotable.io"
            }
        except:
            return None

    def get_display_name(self):
        return "💭 Random Quote"
```

### Weather Scraper

```python
import requests
from src.base import BaseScraper

class WeatherScraper(BaseScraper):
    def __init__(self):
        super().__init__("weather")

    def fetch(self):
        try:
            response = requests.get("https://wttr.in/format=j1")
            data = response.json()
            current = data["current_condition"][0]
            return {
                "title": f"Weather: {current['desc']} • {current['temp_C']}°C",
                "link": "https://wttr.in"
            }
        except:
            return None

    def get_display_name(self):
        return "🌤️ Current Weather"
```

## 🚀 Automation (GitHub Actions)

Untuk menambahkan scraper ke automation, edit `.github/workflows/daily_stupid_svg.yml`:

```yaml
- name: Generate Your Service Badge
  run: python scripts/generate_all.py your_service
```

## 📦 Dependencies

Jika scraper memerlukan dependency tambahan:

1. Add ke `requirements.txt`:

   ```
   your-package>=1.0.0
   ```

2. Update workflow:
   ```yaml
   - name: Install dependencies
     run: |
       python -m pip install --upgrade pip
       pip install -r requirements.txt
   ```

## ✅ Testing

Buat test file `tests/test_your_scraper.py`:

```python
import unittest
from src.services.your_service import YourScraper
from src.generators.svg_generators import YourSVGGenerator

class TestYourScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = YourScraper()
        self.generator = YourSVGGenerator()

    def test_fetch(self):
        item = self.scraper.fetch()
        self.assertIsNotNone(item)
        self.assertIn("title", item)
        self.assertIn("link", item)

    def test_generate_svg(self):
        item = {
            "title": "Test Title",
            "link": "https://example.com"
        }
        svg = self.generator.generate(item)
        self.assertIn("<svg", svg)
        self.assertIn("Test Title", svg)
```

## 📝 Best Practices

1. **Error Handling**: Selalu handle exceptions, return None jika gagal
2. **Timeouts**: Set timeout untuk HTTP requests
3. **Rate Limiting**: Respek API rate limits
4. **Caching**: Cache hasil jika memungkinkan untuk performa
5. **User-Agent**: Set proper User-Agent headers
6. **Logging**: Log informasi debug untuk troubleshooting

## 🤝 Contributing

Saat submit PR untuk scraper baru:

1. Include docstrings lengkap
2. Handle error cases
3. Add test cases
4. Update README dengan deskripsi scraper
5. Test locally sebelum submit

---

**Happy Scraping!** 🎉
