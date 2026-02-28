# modules/claim_classifier.py

from collections import defaultdict

# Define keyword mapping for classification
KEYWORDS = {
    "growth": ["%", "cagr", "growth", "expansion"],
    "investment": ["$", "funding", "capital"],
    "risk": ["risk", "challenge", "decline", "uncertainty"],
    "regulation": ["policy", "government", "regulation"],
    "market_dynamics": ["demand", "supply", "competition"]
}

def classify_claims(claims: list) -> dict:
    """
    Classify a list of claims into predefined categories based on keywords.

    Args:
        claims (list): List of claim strings.

    Returns:
        dict: Dictionary with categories as keys and list of claims as values.
    """
    classified = {category: [] for category in KEYWORDS}
    classified["other"] = []

    for claim in claims:
        lower_claim = claim.lower()
        matched = False
        for category, keywords in KEYWORDS.items():
            if any(keyword in lower_claim for keyword in keywords):
                classified[category].append(claim)
                matched = True
                break
        if not matched:
            classified["other"].append(claim)

    return classified


def generate_claim_summary(classified_claims: dict) -> dict:
    """
    Generate a summary count of claims per category.

    Args:
        classified_claims (dict): Output from classify_claims function.

    Returns:
        dict: Count of claims per category.
    """
    summary = {category: len(claims) for category, claims in classified_claims.items()}
    return summary