from typing import List, Dict
from urllib.parse import urlparse


def analyze_sources(articles: List[Dict]) -> Dict:
    """
    Analyze source credibility and diversity.

    Args:
        articles: List of article dictionaries with 'url' key.

    Returns:
        Dictionary containing credibility metrics.
    """

    total_sources = len(articles)

    # Handle empty input safely
    if total_sources == 0:
        return {
            "total_sources": 0,
            "unique_domains": 0,
            "gov_sources": 0,
            "edu_sources": 0,
            "org_sources": 0,
            "com_sources": 0,
            "credibility_score": 0.0,
            "diversity_level": "Low"
        }

    domains = set()
    gov_count = 0
    edu_count = 0
    org_count = 0
    com_count = 0

    for article in articles:
        url = article.get("url", "")
        if not url:
            continue

        parsed = urlparse(url)
        domain = parsed.netloc.lower().replace("www.", "")
        domains.add(domain)

        if domain.endswith(".gov"):
            gov_count += 1
        elif domain.endswith(".edu"):
            edu_count += 1
        elif domain.endswith(".org"):
            org_count += 1
        elif domain.endswith(".com"):
            com_count += 1

    unique_domains = len(domains)

    # Raw credibility score calculation
    raw_score = (
        gov_count * 3.0 +
        edu_count * 2.0 +
        org_count * 1.5 +
        com_count * 1.0
    )

    max_possible_score = total_sources * 3.0  # All sources are .gov
    credibility_score = (
        (raw_score / max_possible_score) * 100
        if max_possible_score > 0 else 0.0
    )

    return {
        "total_sources": total_sources,
        "unique_domains": unique_domains,
        "gov_sources": gov_count,
        "edu_sources": edu_count,
        "org_sources": org_count,
        "com_sources": com_count,
        "credibility_score": round(credibility_score, 2),
        "diversity_level": get_diversity_rating(unique_domains)
    }


def get_diversity_rating(unique_domains: int) -> str:
    """
    Determine source diversity level.
    """
    if unique_domains > 3:
        return "High"
    elif 2 <= unique_domains <= 3:
        return "Moderate"
    return "Low"