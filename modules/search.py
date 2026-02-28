from duckduckgo_search import DDGS
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def search_and_extract(subquestion):
    results_data = []

    if not subquestion or not isinstance(subquestion, str):
        return []

    try:
        with DDGS() as ddgs:
            search_results = ddgs.text(subquestion, max_results=5)
            search_results = list(search_results)
    except Exception:
        return []

    if not search_results:
        return []

    for result in search_results[:5]:
        try:
            title = result.get("title", "")
            url = result.get("href", "") or result.get("url", "")

            if not url:
                continue

            domain = urlparse(url).netloc

            try:
                response = requests.get(
                    url,
                    timeout=5,
                    headers={
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                    },
                )
                response.raise_for_status()
            except Exception:
                continue

            soup = BeautifulSoup(response.text, "html.parser")

            for tag in soup(["script", "style", "noscript"]):
                tag.decompose()

            text = soup.get_text(separator=" ", strip=True)

            cleaned_text = " ".join(text.split())

            if len(cleaned_text) > 3000:
                cleaned_text = cleaned_text[:3000]

            results_data.append(
                {
                    "title": title,
                    "url": url,
                    "content": cleaned_text,
                    "domain": domain,
                }
            )

        except Exception:
            continue

    return results_data