from typing import List, Dict
from urllib.parse import urlparse
import re

def analyze_sources(articles: List[Dict]) -> Dict:
    """
    Analyze source credibility and diversity.
    
    Args:
        articles: List of article dicts with 'url' key
        
    Returns:
        Credibility analysis dictionary
    """
    total_sources = len(articles)
    if total_sources == 0:
        return {
            "total_sources": 0,
            "unique_domains": 0,
            "gov_sources": 0,
            "edu_sources": 0,
            "org_sources": 0,
            "com_sources": 0,
            "credibility_score": 0.0
        }
    
    domains = set()
    gov_count, edu_count, org_count, com_count = 0, 0, 0, 0
    
    for article in articles:
        url = article.get('url', '')
        if not url:
            continue
            
        # Extract domain
        parsed = urlparse(url)
        domain = parsed.netloc.lower().replace('www.', '')
        domains.add(domain)
        
        # Count TLDs
        if domain.endswith('.gov'):
            gov_count += 1
        elif domain.endswith('.edu'):
            edu_count += 1
        elif domain.endswith('.org'):
            org_count += 1
        elif domain.endswith('.com'):
            com_count += 1
    
    unique_domains = len(domains)
    
    # Calculate raw credibility score
    raw_score = (
        gov_count * 3.0 +
        edu_count * 2.0 +
        org_count * 1.5 +
        com_count * 1.0
    )
    
    # Normalize to 0-100 scale
    max_possible = total_sources * 3.0  # Max if all .gov
    credibility_score = (raw_score / max_possible * 100) if max_possible > 0 else 0.0
    
    return {
        "total_sources": total_sources,
        "unique_domains": unique_domains,
        "gov_sources": gov_count,
        "edu_sources": edu_count,
        "org_sources": org_count,
        "com_sources": com_count,
        "credibility_score": round(credibility_score, 2)
    }

def get_diversity_rating(unique_domains: int) -> str:
    """Helper for diversity rating (for future use)."""
    if unique_domains > 3:
        return "High"
    elif unique_domains >= 2:
        return "Moderate"
    return "Low"
