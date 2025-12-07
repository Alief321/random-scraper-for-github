# Stupid Patterns Configuration

This directory contains pattern configuration files for the Stupid Question Detector.

## Files

### `stupid_patterns.json`

Main pattern configuration file containing all detection patterns organized by categories.

## Structure

```json
{
  "categories": {
    "category_name": {
      "description": "Category description",
      "patterns": ["pattern1", "pattern2"]
    }
  },
  "metadata": {
    "version": "1.0.0",
    "last_updated": "2025-12-07",
    "total_categories": 16
  }
}
```

## Current Categories

1. **security_hacking** - Security and hacking related (14 patterns)
2. **personal_relationship** - Personal/relationship issues (8 patterns)
3. **urgency_desperation** - Urgency indicators (10 patterns)
4. **vim_related** - Classic Vim confusion (7 patterns)
5. **school_homework** - School/homework related (10 patterns)
6. **basic_mistakes** - Basic beginner mistakes (12 patterns)
7. **confusion_indicators** - Confusion signals (11 patterns)
8. **lack_of_effort** - Lack of effort (8 patterns)
9. **stuck_help** - Stuck and help requests (5 patterns)
10. **copy_paste** - Copy/paste issues (5 patterns)
11. **weird_unusual** - Weird situations (7 patterns)
12. **typos_quality** - Typos and low quality (9 patterns)
13. **interview_test_cheating** - Interview/test related (6 patterns)
14. **ai_chatgpt** - AI/ChatGPT related (6 patterns)
15. **database_disasters** - Database disasters (5 patterns)
16. **beginner_confusion** - Extreme beginner (6 patterns)

**Total: 129 patterns across 16 categories**

## Adding New Patterns

Edit `stupid_patterns.json` and add to existing category or create new one:

```json
{
  "categories": {
    "your_category": {
      "description": "Your category description",
      "patterns": ["pattern one", "pattern two"]
    }
  }
}
```

Changes will be loaded automatically on next run.

## Pattern Guidelines

1. **Lowercase** - Patterns are case-insensitive
2. **Specific** - Be specific to avoid false positives
3. **No duplicates** - Each pattern should be unique
4. **Cultural sensitivity** - Avoid offensive terms
5. **Contextual** - Consider common usage context

## Usage in Code

```python
from src.utils.stupid_detector import get_detector

detector = get_detector()
# Patterns automatically loaded from JSON

# Reload after editing JSON
detector.reload_patterns()
```

## Testing Patterns

```bash
# Test detector
python -c "from src.utils.stupid_detector import get_detector; print(get_detector().get_pattern_count())"
```

## Backup

Keep backups of this file before making major changes:

```bash
cp stupid_patterns.json stupid_patterns.backup.json
```
