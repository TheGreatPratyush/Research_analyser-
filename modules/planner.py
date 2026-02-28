import os
import ast
from typing import List
import google.generativeai as genai


def generate_subquestions(query: str) -> List[str]:
    """
    Break a research question into 5–7 structured sub-questions.
    """

    if not query or not isinstance(query, str):
        return []

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return []

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")

        prompt = f"""
Break the following research question into EXACTLY 5–7
clear, specific, searchable sub-questions.

Return ONLY a Python list of strings.
Do NOT include explanation.

Question:
{query}
"""

        response = model.generate_content(prompt)
        raw_output = response.text.strip()

        # Try safe parsing
        try:
            sub_questions = ast.literal_eval(raw_output)
            if isinstance(sub_questions, list):
                return sub_questions[:7]
        except Exception:
            pass

        # Fallback: split by lines
        lines = raw_output.split("\n")
        cleaned = [line.strip("-• ").strip() for line in lines if line.strip()]

        return cleaned[:7]

    except Exception:
        return []
    