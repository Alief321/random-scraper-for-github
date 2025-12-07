"""Base service class for scraper services"""
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional


class BaseScraper(ABC):
    """Abstract base class for all scraper services"""
    
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def fetch(self) -> Optional[Dict[str, Any]]:
        """Fetch random item from source
        
        Returns:
            Dict with keys: title, link, and any additional metadata
            None if fetch fails
        """
        pass
    
    @abstractmethod
    def get_display_name(self) -> str:
        """Get display name for this scraper"""
        pass


class SVGGenerator(ABC):
    """Abstract base class for SVG generators"""
    
    @abstractmethod
    def generate(self, item: Dict[str, Any]) -> str:
        """Generate SVG content from item
        
        Args:
            item: Dictionary with title, link, and optional metadata
            
        Returns:
            SVG string
        """
        pass
