import os
import google.generativeai as genai


def generate_report(
    question: str,
    classified_claims: dict,
    analytics: dict,
    confidence: float
) -> str:
    """
    Generate a structured intelligence report using Gemini.
    Returns formatted report string.
    """

    if not question or not isinstance(question, str):
        return ""

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return ""

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")

        growth_claims = classified_claims.get("growth", [])
        investment_claims = classified_claims.get("investment", [])
        risk_claims = classified_claims.get("risk", [])
        regulation_claims = classified_claims.get("regulation", [])
        other_claims = classified_claims.get("other", [])

        prompt = f"""
You are a strategic research intelligence system.

Generate a structured professional research report.

Research Question:
{question}

Classified Claims:
Growth: {growth_claims}
Investment: {investment_claims}
Risk: {risk_claims}
Regulation: {regulation_claims}
Other: {other_claims}

Numerical Analytics:
Count: {analytics.get("count")}
Average: {analytics.get("average")}
Min: {analytics.get("min")}
Max: {analytics.get("max")}
Range: {analytics.get("range")}
Volatility Level: {analytics.get("volatility_level")}

Confidence Score: {confidence}

The report MUST contain these sections exactly:

1. Executive Summary
2. Growth Analysis
3. Investment Signals
4. Risk Factors
5. Regulatory Insights
6. Numerical Analysis
7. Confidence Score
8. Final Outlook

Rules:
- Professional tone
- Concise but analytical
- Do not mention AI or Gemini
- Do not add extra commentary
- Return only the formatted report
"""

        response = model.generate_content(prompt)
        return response.text.strip() if hasattr(response, "text") else ""

    except Exception:
        return ""