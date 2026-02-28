# modules/scoring.py

import re


def extract_percentages(text):
    """
    Extract percentage numbers from text.
    Returns list of float values.
    """
    matches = re.findall(r'(\d+\.?\d*)\s*%', text)
    return [float(num) for num in matches]


def collect_all_percentages(articles):
    """
    Extract percentages from list of article dictionaries.
    """
    all_values = []

    for article in articles:
        text = article.get("content", "")
        values = extract_percentages(text)
        all_values.extend(values)

    return all_values


def detect_conflict(values, threshold=5):
    """
    Detect if values differ more than threshold.
    Returns:
    - conflict_exists (True/False)
    - difference
    """
    if len(values) < 2:
        return False, 0

    max_value = max(values)
    min_value = min(values)
    difference = max_value - min_value

    conflict_exists = difference > threshold

    return conflict_exists, difference


def compute_scores(values):
    """
    Compute conflict index and confidence score.
    """
    if not values:
        return 0, 0

    max_value = max(values)
    min_value = min(values)
    difference = max_value - min_value

    conflict_index = difference / max_value if max_value != 0 else 0
    confidence_score = max(0, 100 - (conflict_index * 100))

    return round(conflict_index, 2), round(confidence_score, 2)