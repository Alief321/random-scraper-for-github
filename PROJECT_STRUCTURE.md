# 📁 Project Structure Documentation

## 📂 Complete Directory Tree

```
random-scraper-for-github-readme/
│
├── .github/
│   └── workflows/
│       └── daily_stupid_svg.yml          # GitHub Actions automation
│
├── src/                                   # Main source code
│   ├── __init__.py                       # Package exports
│   ├── base.py                           # Abstract base classes
│   │   ├── BaseScraper                   # Interface untuk semua scraper
│   │   └── SVGGenerator                  # Interface untuk SVG generator
│   │
│   ├── services/                         # Scraper implementations
│   │   ├── __init__.py
│   │   ├── stackoverflow.py              # StackOverflow question scraper
│   │   └── github.py                     # GitHub repository scraper
│   │
│   ├── generators/                       # SVG generator implementations
│   │   ├── __init__.py
│   │   └── svg_generators.py
│   │       ├── StackOverflowSVGGenerator
│   │       └── GitHubRepoSVGGenerator
│   │
│   └── utils/                            # Utility functions
│       ├── __init__.py
│       └── svg.py                        # SVG generation helpers
│
├── scripts/                               # CLI scripts
│   ├── generate_all.py                   # Main generator (flexible)
│   ├── generate_stupid_svg.py            # Legacy StackOverflow generator
│   ├── generate_random_repo.py           # Legacy GitHub generator
│   └── update_readme.py                  # README updater
│
│── data/                                # Generated output
│   ├── stupid_patterns.json             # Check pattern of stupid question
│   └── README.md                        # Docs of pattern
│
├── assets/                                # Generated output
│   ├── stackoverflow.svg                 # StackOverflow badge
│   └── github_repo.svg                   # GitHub badge
│
├── requirements.txt                       # Python dependencies
├── README.MD                              # Main documentation
├── EXTENSIBILITY.md                       # Guide untuk add scraper baru
└── PROJECT_STRUCTURE.md                   # File ini
```

## 🔄 Data Flow

```
┌─────────────────────────────────────────────────────────┐
│           SCRAPER (BaseScraper)                         │
│  ┌─────────────────────────────────────────────────┐  │
│  │ fetch() → Dict[title, link, ...metadata]       │  │
│  └─────────────────────────────────────────────────┘  │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│      GENERATOR (SVGGenerator)                           │
│  ┌─────────────────────────────────────────────────┐  │
│  │ generate(item) → SVG String                     │  │
│  └─────────────────────────────────────────────────┘  │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│           FILE SAVE                                     │
│  assets/[output_file].svg                              │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│      README UPDATE                                      │
│  ┌─────────────────────────────────────────────────┐  │
│  │ Extract SVG info & update README.MD             │  │
│  └─────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

## 📌 Core Modules

### `src/base.py`

Defines abstract interfaces:

- `BaseScraper`: Abstract class untuk semua scraper

  - `fetch()`: Method abstract untuk fetch data
  - `get_display_name()`: Untuk header SVG

- `SVGGenerator`: Abstract class untuk SVG generators
  - `generate(item)`: Method abstract untuk generate SVG

### `src/services/`

Concrete implementations of scrapers:

**`stackoverflow.py`**

- `StackOverflowScraper`: Fetch "stupid" questions dari StackOverflow RSS
  - Uses `feedparser` untuk parse RSS feed
  - Filter dengan keywords dalam `looks_stupid()`
  - Return: `{title, link}`

**`github.py`**

- `GitHubRepoScraper`: Fetch random repo dari GitHub API
  - Uses `requests` untuk GitHub API
  - Random sort (stars, forks, updated)
  - Return: `{title, link, repo_name, description, stars, language}`

### `src/generators/`

Concrete implementations of SVG generators:

**`svg_generators.py`**

- `StackOverflowSVGGenerator`: Generate SVG untuk StackOverflow badge

  - Color scheme: Orange (#ffb86b)
  - Header: "🤡 Stupid StackOverflow Question of the Day"

- `GitHubRepoSVGGenerator`: Generate SVG untuk GitHub badge
  - Color scheme: GitHub blue (#58a6ff)
  - Header: "⭐ Random Interesting GitHub Repository"

### `src/utils/svg.py`

SVG helper functions:

- `generate_svg()`: Main function untuk generate SVG
  - Customizable: colors, dimensions, text wrapping
  - Returns valid SVG string

## Data

this folder contain pattern check of stupid question of stackoverflow

## 🔧 Scripts

### `generate_all.py` (Main)

```bash
python scripts/generate_all.py [scraper_type]
```

- Flexible generator untuk semua scraper
- SCRAPERS dict map ke scraper + generator + output file
- Support multiple scrapers dengan extend SCRAPERS dict

### `update_readme.py`

```bash
python scripts/update_readme.py
```

- Read SVG files dari assets/
- Extract data (title, link, header)
- Generate README dengan current badges
- Update timestamp

## 🔌 Adding New Scraper (Step-by-step)

### 1. Create Service

```
src/services/my_scraper.py
├── MyScraperClass(BaseScraper)
├── fetch() → Dict
└── get_display_name() → str
```

### 2. Create Generator

```
src/generators/svg_generators.py
└── MySVGGeneratorClass(SVGGenerator)
    └── generate(item) → str
```

### 3. Register

```
src/services/__init__.py → import MyScraperClass
src/generators/__init__.py → import MySVGGeneratorClass
```

### 4. Add to scripts

```
scripts/generate_all.py → SCRAPERS dict
{
    "my_service": {
        "scraper": MyScraperClass,
        "generator": MySVGGeneratorClass,
        "output_file": "my_badge.svg"
    }
}
```

### 5. Test

```bash
python scripts/generate_all.py my_service
python scripts/update_readme.py
```

## 🤖 GitHub Actions Workflow

**File:** `.github/workflows/daily_stupid_svg.yml`

### Trigger

- Daily: `0 0 * * *` (00:00 UTC)
- Manual: workflow_dispatch

### Steps

1. Checkout repo
2. Setup Python 3.11
3. Install dependencies (pip install -r requirements.txt)
4. Generate StackOverflow badge (`python scripts/generate_all.py stackoverflow`)
5. Generate GitHub badge (`python scripts/generate_all.py github`)
6. Update README (`python scripts/update_readme.py`)
7. Commit & push (if changes)

### To Add New Scraper to Workflow

```yaml
- name: Generate My Service Badge
  run: python scripts/generate_all.py my_service
```

## 📊 Dependencies

### Required Packages

```
feedparser==6.0.11      # RSS/Atom parsing
requests>=2.28.0        # HTTP requests
beautifulsoup4>=4.11.0  # HTML parsing (optional untuk scraper custom)
```

### Python Version

- Minimum: 3.7
- Tested: 3.11

## ✅ Validation Points

### Scraper Implementation

- ✓ Inherit dari `BaseScraper`
- ✓ Implement `fetch()` method
- ✓ Implement `get_display_name()` method
- ✓ Handle exceptions gracefully
- ✓ Return None on failure
- ✓ Set proper timeouts

### Generator Implementation

- ✓ Inherit dari `SVGGenerator`
- ✓ Implement `generate(item)` method
- ✓ Accept Dict dengan `title` dan `link`
- ✓ Return valid SVG string
- ✓ Include proper colors dict

### Registration

- ✓ Added to `src/services/__init__.py`
- ✓ Added to `src/generators/__init__.py`
- ✓ Added to SCRAPERS dict in `generate_all.py`
- ✓ Output file specified

## 🧪 Testing

```bash
# Test individual scraper
python scripts/generate_all.py [scraper_type]

# Check output SVG
cat assets/[output_file].svg

# Update README
python scripts/update_readme.py

# Verify README updated
cat README.MD | grep "Last Updated"
```

## 📚 Documentation Files

- **README.MD** - Main documentation & usage guide
- **EXTENSIBILITY.md** - Complete guide untuk add new scrapers
- **PROJECT_STRUCTURE.md** - This file, struktur & architecture

---

**Maintained:** 2025-12-07
**Last Updated:** Automatically by GitHub Actions daily at 00:00 UTC
