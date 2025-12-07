"""SVG Generators for different scraper types"""
from src.base import SVGGenerator
from src.utils.svg import generate_svg
from typing import Dict, Any


class StackOverflowSVGGenerator(SVGGenerator):
    """Generator for StackOverflow question SVG"""
    
    def generate(self, item: Dict[str, Any]) -> str:
        print(item)
        """Generate SVG for StackOverflow question"""
        return generate_svg(
            title=item.get("title", "Unknown question"),
            link=item.get("link", "https://stackoverflow.com"),
            header_text=item.get("display_name", "🤡 Stupid StackOverflow Question of the Day"),
            colors={
                "bg": "#0f172a",
                "accent": "#ffb86b",
                "text_color": "#e6eef8",
                "link_color": "#9be7ff"
            }
        )


class GitHubRepoSVGGenerator(SVGGenerator):
    """Generator for GitHub repository SVG"""
    
    def generate(self, item: Dict[str, Any]) -> str:
        """Generate SVG for GitHub repository"""
        return generate_svg(
            title=item.get("title", "Unknown repository"),
            link=item.get("link", "https://github.com"),
            header_text="⭐ Random Interesting GitHub Repository",
            colors={
                "bg": "#0d1117",
                "accent": "#58a6ff",
                "text_color": "#c9d1d9",
                "link_color": "#79c0ff"
            }
        )
