from modules.planner import generate_subquestions
from modules.search import search_and_extract
from modules.claims import extract_claims
from modules.claim_classifier import classify_claims
from modules.analytics import analyze_numbers
from modules.scoring import (
    collect_all_percentages,
    detect_conflict,
    compute_scores
)
from modules.credibility import analyze_sources
from modules.report import generate_report


def run_research_pipeline(question: str) -> str:
    """
    Runs the full Autonomous Research Intelligence pipeline.
    Returns final structured intelligence report.
    """

    # 1️⃣ Break question into sub-questions
    subquestions = generate_subquestions(question)

    all_articles = []
    all_claims = []

    # 2️⃣ Search and collect articles
    for subq in subquestions:
        articles = search_and_extract(subq)
        all_articles.extend(articles)

    # 3️⃣ Extract claims from all articles
    for article in all_articles:
        claims = extract_claims(article.get("content", ""))
        all_claims.extend(claims)

    # 4️⃣ Classify claims
    classified_claims = classify_claims(all_claims)

    # 5️⃣ Numerical percentage extraction
    values = collect_all_percentages(all_articles)

    # 6️⃣ Analytics layer
    analytics = analyze_numbers(values)

    # 7️⃣ Conflict detection + confidence score
    conflict_exists, difference = detect_conflict(values)
    conflict_index, confidence_score = compute_scores(values)

    # 8️⃣ Credibility analysis
    credibility = analyze_sources(all_articles)

    # 9️⃣ Generate final structured report
    report = generate_report(
        question=question,
        classified_claims=classified_claims,
        analytics=analytics,
        confidence=confidence_score
    )

    return report


if __name__ == "__main__":
    user_question = input("Enter your research question:\n\n")
    final_report = run_research_pipeline(user_question)
    print("\n\n===== AUTONOMOUS RESEARCH INTELLIGENCE REPORT =====\n")
    print(final_report)