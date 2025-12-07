"""Stupid question detection patterns and utilities"""
import json
from pathlib import Path
from typing import List, Set, Dict


class StupidQuestionDetector:
    """Detector for identifying potentially "stupid" or funny questions"""
    
    def __init__(self, patterns_file: str = None):
        """
        Initialize detector with patterns from JSON file
        
        Args:
            patterns_file: Path to JSON patterns file. If None, uses default.
        """
        if patterns_file is None:
            # Default patterns file location
            base_dir = Path(__file__).parent.parent.parent
            patterns_file = base_dir / "data" / "stupid_patterns.json"
        
        self.patterns_file = patterns_file
        self.categories = {}
        self.patterns = self._load_patterns()
    
    def _load_patterns(self) -> Set[str]:
        """Load all detection patterns from JSON file"""
        patterns = []
        
        try:
            with open(self.patterns_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Load patterns from all categories
            self.categories = data.get('categories', {})
            for category_name, category_data in self.categories.items():
                category_patterns = category_data.get('patterns', [])
                patterns.extend(category_patterns)
            
            print(f"✅ Loaded {len(patterns)} patterns from {len(self.categories)} categories")
        
        except FileNotFoundError:
            print(f"⚠️ Patterns file not found: {self.patterns_file}")
            print("Using fallback minimal patterns")
            # Fallback minimal patterns
            patterns = [
                "hack", "crack", "virus", "malware",
                "plz", "please help", "urgent",
                "exit vim", "stuck in vim",
                "homework", "school project",
                "my code not working"
            ]
        except json.JSONDecodeError as e:
            print(f"⚠️ Error parsing JSON: {e}")
            print("Using fallback minimal patterns")
            patterns = ["help", "urgent", "stuck"]
        
        return set(p.lower() for p in patterns)
    
    def is_stupid(self, title: str) -> bool:
        """
        Check if question title matches stupid patterns
        
        Args:
            title: Question title to check
            
        Returns:
            True if matches any stupid pattern
        """
        title_lower = title.lower()
        return any(pattern in title_lower for pattern in self.patterns)
    
    def get_matched_patterns(self, title: str) -> List[str]:
        """
        Get all patterns that match the title
        
        Args:
            title: Question title to check
            
        Returns:
            List of matched patterns
        """
        title_lower = title.lower()
        return [p for p in self.patterns if p in title_lower]
    
    def add_custom_pattern(self, pattern: str):
        """Add custom detection pattern"""
        self.patterns.add(pattern.lower())
    
    def add_custom_patterns(self, patterns: List[str]):
        """Add multiple custom patterns"""
        self.patterns.update(p.lower() for p in patterns)
    
    def get_pattern_count(self) -> int:
        """Get total number of patterns"""
        return len(self.patterns)
    
    def get_categories(self) -> Dict[str, Dict]:
        """Get all categories with their patterns"""
        return self.categories
    
    def get_category_info(self, category_name: str) -> Dict:
        """Get information about a specific category"""
        return self.categories.get(category_name, {})
    
    def reload_patterns(self):
        """Reload patterns from JSON file"""
        self.patterns = self._load_patterns()


# Singleton instance
_detector = StupidQuestionDetector()


def is_stupid_question(title: str) -> bool:
    """
    Quick function to check if question is stupid
    
    Args:
        title: Question title
        
    Returns:
        True if stupid
    """
    return _detector.is_stupid(title)


def get_detector() -> StupidQuestionDetector:
    """Get the global detector instance"""
    return _detector
