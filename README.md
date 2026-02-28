🚀 Autonomous Research Intelligence Engine

AI-powered system that automatically decomposes complex strategic research questions into structured, actionable sub-questions for faster and more comprehensive analysis.

🧩 Problem Statement
📌 The Research That Takes a Week — and Shouldn’t

Researchers spend significant time manually breaking complex strategic questions into smaller, searchable sub-questions.

This process is:

❌ Inconsistent

❌ Slow (2–3 hours per question)

❌ Prone to cognitive bias

❌ Lacking structured decomposition frameworks

Result → Incomplete or inefficient research.

🎯 Target Users

Academic Researchers (Students, Professors, PhD Candidates)

Market Analysts (Investment Firms, Consulting Firms)

Business Strategists (Product Managers, Growth Teams)

Policy Researchers (Think Tanks, NGOs, Government Bodies)

⚠️ Existing Gaps

❌ No automated question decomposition tools

❌ Manual and time-intensive workflow

❌ Inconsistent sub-question quality

❌ Missed research dimensions

❌ No team-wide standardization

💡 Proposed Solution
🔍 Example

Input:

“What are the best EV strategies in India?”

Output:

What is the current EV market size in India?

Who are the key competitors?

What government regulations affect EV adoption?

What infrastructure challenges exist?

What are projected growth trends?

🧠 Core Idea

LLM-powered question decomposition using structured prompt engineering via API-based inference.

Zero-shot (no training required)

Structured output enforcement

Fast real-time response (< 1 sec)

✨ Key Features

Input: Complex research question (string)

Output: 5–7 structured sub-questions (List[str])

Zero-shot LLM inference

Modular backend architecture

Integration-ready with search & scoring modules

Stateless and scalable design

🏗️ System Architecture
High-Level Flow
User
  ↓
FastAPI Backend
  ↓
Planner Module
  ↓
Search Module
  ↓
Scoring Module
  ↓
Structured Research Report
Module Breakdown
File	Responsibility
main.py	API routing & orchestration
modules/planner.py	Generates structured sub-questions
modules/search.py	Retrieves relevant information
modules/scoring.py	Ranks and filters results
🗄️ Database Design

No database used.

Stateless system

Real-time inference

Serverless-compatible

Simplified architecture

🤖 Model Selection

Model Used: API-based LLM (e.g., Gemini 1.5 Flash)

Why?

Low latency

Cost-effective

Reliable structured output

Suitable for real-time inference

🔄 Alternatives Considered
Model	Pros	Cons
GPT-4o	High reasoning quality	Expensive
Claude	Strong reasoning	Less structured output
Llama 3	Open-source	Requires self-hosting
📏 Evaluation Metrics

Completeness → Always 5–7 sub-questions

Specificity → Search-friendly phrasing

Consistency → Low output variation

Relevance → Strong alignment with original query

🛠️ Technology Stack
Frontend

HTML

CSS

JavaScript

Backend

Python 3.11

FastAPI

google-generativeai

python-dotenv

AI

API-based LLM

Structured Prompt Engineering

Deployment

Vercel (Frontend)

Docker (Backend – Planned)

📡 API Documentation
Endpoint
POST /generate
Request
{
  "query": "EV market strategies in India?"
}
Response
{
  "subquestions": [
    "What is the current market size of EVs in India?",
    "Who are the major competitors?",
    "What regulatory policies affect EV adoption?",
    "What infrastructure challenges exist?",
    "What are projected growth trends?"
  ]
}

Tested using Postman / Thunder Client.

🔄 End-to-End Workflow

User enters research question

Planner generates 5–7 sub-questions

Search module retrieves relevant data

Scoring module ranks results

Structured research output is delivered

🧱 Development Progress

✅ Research & Architecture Planning

✅ Planner Module

⏳ Search Module Integration

⏳ Scoring Module Integration

⏳ Frontend Enhancement

⏳ Docker Deployment

👥 Team Roles
Member	Role	Responsibility
Shanmukha Sai Chakali	Planner	modules/planner.py
Vishal Kumar Gowda	Search	modules/search.py
Pratyush Gupta	Scoring & Integration	modules/scoring.py
🔮 Future Scope
Short-Term

Sub-question relevance scoring

Multi-language support

Query caching

Long-Term

Fine-tuned research LLM

Academic database integration

Enterprise SaaS deployment

⚠️ Known Limitations

API dependency

English-only support

No offline mode

No persistent storage

🌍 Impact

Reduces research planning time

Improves completeness of analysis

Standardizes research decomposition

Enables scalable autonomous research pipelines

▶️ Run Locally
git clone https://github.com/TheGreatPratyush/Research_analyser-
cd Research_analyser-
pip install -r requirements.txt
python main.py
🎥 Repository

GitHub:
https://github.com/TheGreatPratyush/Research_analyser-

Standardizes decomposition across teams

Enables scalable autonomous research pipelines
