#!/usr/bin/env python3
"""
Main generator script for all scrapers
Run: python scripts/generate_all.py [scraper_type]
Example: python scripts/generate_all.py stackoverflow
         python scripts/generate_all.py github
"""
import os
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.services import StackOverflowScraper, GitHubRepoScraper
from src.generators import StackOverflowSVGGenerator, GitHubRepoSVGGenerator


SCRAPERS = {
    "stackoverflow": {
        "scraper": StackOverflowScraper,
        "generator": StackOverflowSVGGenerator,
        "output_file": "stupid.svg"
    },
    "github": {
        "scraper": GitHubRepoScraper,
        "generator": GitHubRepoSVGGenerator,
        "output_file": "github_repo.svg"
    }
}


def generate_svg(scraper_type: str = "stackoverflow"):
    """Generate SVG for given scraper type"""
    if scraper_type not in SCRAPERS:
        print(f"❌ Unknown scraper type: {scraper_type}")
        print(f"Available types: {', '.join(SCRAPERS.keys())}")
        return False
    
    config = SCRAPERS[scraper_type]
    scraper_class = config["scraper"]
    generator_class = config["generator"]
    output_file = config["output_file"]
    
    print(f"🔄 Fetching from {scraper_type}...")
    scraper = scraper_class()
    item = scraper.fetch()
    
    if not item:
        print(f"❌ Failed to fetch from {scraper_type}")
        return False
    
    print(f"✅ Fetched: {item.get('title', 'N/A')[:50]}...")
    
    print(f"🎨 Generating SVG...")
    generator = generator_class()
    svg_content = generator.generate(item)
    
    # Save SVG
    os.makedirs("assets", exist_ok=True)
    output_path = os.path.join("assets", output_file)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    
    print(f"✅ Saved to: {output_path}")
    return True


def main():
    if len(sys.argv) > 1:
        scraper_type = sys.argv[1]
    else:
        scraper_type = "stackoverflow"
    
    generate_svg(scraper_type)


if __name__ == "__main__":
    main()
