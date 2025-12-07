"""StackOverflow Stupid Question Scraper Service"""
import feedparser
from typing import Optional, Dict, Any
from src.base import BaseScraper
from src.utils.stupid_detector import is_stupid_question
import random


class StackOverflowScraper(BaseScraper):
    """Scraper for stupid StackOverflow questions"""
    
    def __init__(self):
        super().__init__("stackoverflow")
        self.feed_url = "https://stackoverflow.com/feeds"
        self.found_stupid = True  # Track if stupid question was found
    
    def looks_stupid(self, title: str) -> bool:
        """Check if question looks stupid based on patterns"""
        return is_stupid_question(title)
    
    def fetch(self) -> Optional[Dict[str, Any]]:
        """Fetch a stupid question from StackOverflow feed"""
        try:
            feed = feedparser.parse(self.feed_url)
            if not getattr(feed, "entries", None):
                return None
            
            candidates = []
            # Check first 60 newest entries
            for entry in feed.entries[:60]:
                title = entry.title
                link = entry.link
                if self.looks_stupid(title):
                    candidates.append({"title": title, "link": link, "display_name": self.get_display_name()})
            
            # Fallback: if no candidates, use first entry
            if not candidates:
                print("No stupid questions found, using random fallback")
                self.found_stupid = False
                entry = random.choice(feed.entries)
                return {"title": entry.title, "link": entry.link, "display_name": self.get_display_name()}
            
            self.found_stupid = True
            # Return first found (deterministic)
            return candidates[0]
        except Exception as e:
            print(f"Error fetching from StackOverflow: {e}")
            return None
    
    def get_display_name(self) -> str:
        """Get display name"""
        if self.found_stupid:
            return "🤡 Stupid StackOverflow Question of the Day"
        return "💻 StackOverflow Question of the Day"
