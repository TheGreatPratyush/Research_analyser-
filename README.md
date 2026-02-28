🚀 Autonomous Research Intelligence Engine

AI-powered system that automatically decomposes complex strategic research questions into structured, actionable sub-questions for faster and more comprehensive analysis.

🧩 Problem Statement
Problem Title

The Research That Takes a Week and Shouldn’t

Problem Description

Researchers spend significant time manually breaking complex strategic questions into smaller, searchable sub-questions. This manual process is:

Inconsistent

Slow (2–3 hours per question)

Prone to cognitive bias

Lacking systematic decomposition frameworks

🎯 Target Users

Academic Researchers (Students, Professors, PhD Candidates)

Market Analysts (Investment Firms, Consulting Companies)

Business Strategists (Product Managers, Growth Teams)

Policy Researchers (Government Think Tanks, NGOs)

⚠️ Existing Gaps

❌ No automated question decomposition tools

❌ Manual and time-intensive workflow

❌ Inconsistent sub-question quality

❌ Missed research dimensions

❌ Lack of team-wide standardization

🔍 Problem Understanding & Approach
Root Cause Analysis

Process Breakdown:

Complex Question 
    ↓
Manual Breakdown 
    ↓
Inconsistent Sub-questions 
    ↓
Incomplete Research
Root Causes

Human cognitive bias

No structured decomposition framework

Time constraints

Lack of automation

💡 Proposed Solution
Solution Overview

Transforms:

“What are the best EV strategies in India?”

Into:

What is the current market size of EVs in India?

Who are the key competitors?

What government regulations affect EV adoption?

What infrastructure challenges exist?

What are projected growth trends?

🧠 Core Idea

LLM-powered question decomposition using structured prompting via API-based inference.

✨ Key Features

Input: Complex research question (string)

Output: 5–7 actionable sub-questions (List[str])

Zero-shot inference (no model training required)

Modular Python architecture

Integration-ready with search & scoring modules

🏗️ System Architecture
High-Level Flow
User 
  ↓
Backend (FastAPI)
  ↓
Planner Module
  ↓
Search Module
  ↓
Scoring Module
  ↓
Final Structured Report
Architecture Description

The system follows a modular backend design:

main.py → Handles user input and orchestration

planner.py → Generates structured sub-questions

search.py → Retrieves relevant information

scoring.py → Ranks and filters results

🖼️ Architecture Diagram

(Add system architecture diagram image here)

🗄️ Database Design
Database Approach

No database used.
The system is stateless and operates in real time.

Design Rationale

No persistence required

Simplified architecture

Scalable serverless deployment compatibility

📊 Dataset
Dataset Name

None (Zero-shot inference)

Source

LLM API

Data Type

Pre-trained large-scale language model corpus

Selection Reason

Trained on diverse research and business content

Fast inference (<1 second per query)

Strong structured output capability

🔧 Preprocessing Steps

Structured prompt engineering

Output validation

Enforcing 5–7 question constraint

Response formatting validation

🤖 Model Selected
Model Name

API-based LLM (e.g., Gemini 1.5 Flash)

Selection Reasoning

Low latency

Cost-effective

Reliable structured output

Suitable for real-time decomposition

🔄 Alternatives Considered
Model	Pros	Cons
GPT-4o	High reasoning quality	Expensive
Claude	Strong reasoning	Less structured output
Llama3	Open-source	Requires self-hosting
📏 Evaluation Metrics

Completeness → Always 5–7 sub-questions

Specificity → Searchable phrasing

Consistency → Low output variation

Relevance → Alignment with original query

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

ML / AI

API-based LLM

Structured Prompt Engineering

Database

None (Stateless Architecture)

Deployment

Vercel (Frontend)

Docker (Backend – Planned)

📡 API Documentation
Endpoint
POST /generate
Input
{
  "query": "EV market strategies in India?"
}
Output
{
  "subquestions": [
    "What is the current market size of EVs in India?",
    "Who are the major competitors?",
    "What regulatory policies affect EV adoption?",
    "What infrastructure challenges exist?",
    "What are projected growth trends?"
  ]
}

API tested using Thunder Client / Postman

(Add Postman screenshots here)

🧱 Module-wise Development & Deliverables
✅ Checkpoint 1: Research & Planning

Problem definition

Architecture design

✅ Checkpoint 2: Backend Development

modules/planner.py

⏳ Checkpoint 3: Frontend Development

Minimal UI integration

☑️ Checkpoint 4: Model Training (Skipped)

Zero-shot LLM used

✅ Checkpoint 5: Model Integration

Planner integrated with API

⏳ Checkpoint 6: Deployment

Docker setup (planned)

🔄 End-to-End Workflow

User enters research question

Planner generates 5–7 sub-questions

Search module retrieves information

Scoring module ranks quality

Structured research output delivered

🎥 Demo & Repository

Run Locally:

python main.py

GitHub Repository:
https://github.com/TheGreatPratyush/Research_analyser-

🏆 Hackathon Deliverables Summary

✅ AI Planner Module

✅ Structured Output System

✅ Modular Backend Architecture

⏳ Search & Scoring Integration

⏳ UI Enhancement

👥 Team Roles & Responsibilities
Member	Role	Responsibilities
Shanmukha Sai Chakali	Planner Module	modules/planner.py
Vishal Kumar Gowda	Search Module	modules/search.py
Pratyush Gupta	Scoring & Integration	modules/scoring.py
🔮 Future Scope & Scalability
Short-Term

Sub-question relevance scoring

Multi-language support

Query caching

Long-Term

Custom fine-tuned research LLM

Academic database integration

Enterprise SaaS deployment

⚠️ Known Limitations

API dependency

English-only support

No offline mode

No persistent storage

🌍 Impact

Reduces research planning time

Improves research completeness

Standardizes decomposition across teams

Enables scalable autonomous research pipelines
