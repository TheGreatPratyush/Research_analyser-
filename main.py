from modules.planner import generate_subquestions
from modules.search import search_and_extract
from modules.claims import extract_claims
from modules.scoring import (
    collect_all_percentages,
    detect_conflict,
    compute_scores
)


def run_pipeline(query: str):

    print("\nResearch Question:", query)

    # Step 1 — Break into sub-questions
    subquestions = generate_subquestions(query)
    print("\nSub-Questions:")
    for sq in subquestions:
        print("-", sq)

    all_articles = []
    all_claims = []

    # Step 2 — Search each sub-question
    for sq in subquestions:
        articles = search_and_extract(sq)
        all_articles.extend(articles)

    # Step 3 — Extract claims
    for article in all_articles:
        claims = extract_claims(article.get("content", ""))
        all_claims.extend(claims)

    print("\nExtracted Claims:")
    for claim in all_claims:
        print("-", claim)

    # Step 4 — Conflict Detection
    values = collect_all_percentages(all_articles)
    conflict_exists, difference = detect_conflict(values)
    conflict_index, confidence = compute_scores(values)

    print("\nConflict Exists:", conflict_exists)
    print("Confidence Score:", confidence)


if __name__ == "__main__":
    user_query = input("Enter Research Question: ")
    run_pipeline(user_query)