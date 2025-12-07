"""GitHub Random Repository Scraper Service"""
import requests
import random
from typing import Optional, Dict, Any
from src.base import BaseScraper


class GitHubRepoScraper(BaseScraper):
    """Scraper for random interesting GitHub repositories"""
    
    def __init__(self):
        super().__init__("github")
        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
    
    def fetch(self) -> Optional[Dict[str, Any]]:
        """Fetch a random interesting GitHub repository using GitHub API"""
        try:
            # Use GitHub API to search for popular repositories
            # Search for repos with stars > 1000, sort by stars
            sort_options = ["stars", "forks", "updated"]
            sort_by = random.choice(sort_options)
            
            # Random page to get different results
            page = random.randint(1, 5)
            
            url = "https://api.github.com/search/repositories"
            params = {
                "q": "stars:>10",
                "sort": sort_by,
                "order": "desc",
                "per_page": 100,
                "page": page
            }
            
            response = requests.get(url, params=params, headers=self.headers, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if not data.get("items"):
                print("No repositories found")
                return None
            
            # Pick random repo
            repo = random.choice(data["items"])
            
            repo_name = repo.get("full_name", "Unknown")
            repo_url = repo.get("html_url", "https://github.com")
            description = repo.get("description", "No description")
            stars = repo.get("stargazers_count", 0)
            language = repo.get("language", "Unknown")
            
            # Build title
            title_parts = [repo_name]
            if description:
                title_parts.append(description[:50].rstrip())
            if language and language != "Unknown":
                title_parts.append(f"({language})")
            
            full_title = " • ".join(title_parts)
            
            return {
                "title": full_title,
                "link": repo_url,
                "repo_name": repo_name,
                "description": description,
                "stars": stars,
                "language": language
            }
        except Exception as e:
            print(f"Error fetching from GitHub: {e}")
            return None
    
    def get_display_name(self) -> str:
        """Get display name"""
        return "⭐ Random Interesting GitHub Repository"
