import os
import re
import google.generativeai as genai


def extract_claims(article_text: str) -> list:
    if not article_text or not isinstance(article_text, str):
        return []

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return []

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")

        prompt = f"""
You are an information extraction system.

From the article below, extract 5 to 10 clear, measurable, factual claims.

Rules:
- Focus on numbers, percentages, investments, statistics, growth rates.
- Keep each claim concise.
- Return each claim as a single sentence.
- Do NOT add explanations.
- Do NOT add numbering.
- Only return the claims.

Article:
{article_text}
"""

        response = model.generate_content(prompt)
        raw_output = response.text if hasattr(response, "text") else ""

        lines = raw_output.split("\n")
        claims = []

        for line in lines:
            clean_line = line.strip()

            # Remove bullet points or numbering if present
            clean_line = re.sub(r"^[\-\*\d\.\)\s]+", "", clean_line)

            if clean_line:
                claims.append(clean_line)

        # Ensure 5–10 results max
        return claims[:10]

    except Exception:
        return []
        