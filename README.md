Autonomous Research Intelligence Engine
One-line Project Description
AI-powered system that automatically decomposes complex strategic research questions into structured, actionable sub-questions for faster and more comprehensive analysis.

1. Problem Statement
Problem Title
The Research That Takes a Week and Shouldn't
Problem Description
Researchers spend significant time manually breaking complex strategic questions into smaller, searchable sub-questions. This manual process is inconsistent, slow (2–3 hours per question), and often misses critical research angles due to cognitive bias and the absence of systematic decomposition frameworks.
Target Users
Academic Researchers (Students, Professors, PhD Candidates)
Market Analysts (Investment Firms, Consulting Companies)
Business Strategists (Product Managers, Growth Teams)
Policy Researchers (Government Think Tanks, NGOs)
Existing Gaps
No automated question decomposition tools
Manual and time-intensive workflow
Inconsistent sub-question quality
Missed research dimensions
Lack of team-wide standardization

2. Problem Understanding & Approach
Root Cause Analysis
Process Breakdown:
Complex Question → Manual Breakdown → Inconsistent Sub-questions → Incomplete Research
Root Causes:
Human cognitive bias
No structured decomposition framework
Time constraints
Lack of automation
Solution Strategy
Develop an AI Planner Module that automatically generates 5–7 optimized, specific, and searchable sub-questions using structured prompting.

3. Proposed Solution
Solution Overview
Transforms:
“What are the best EV strategies in India?”
Into:
What is the current market size of EVs in India?
Who are the key competitors?
What are government regulations affecting EV adoption?
What infrastructure challenges exist?
What are projected growth trends?
Core Idea
LLM-powered question decomposition using structured prompting via API-based inference.
Key Features
Input: Complex research question (string)
Output: 5–7 actionable sub-questions (List[str])
Zero-shot inference (no model training required)
Modular Python architecture
Integration-ready with search & scoring modules

4. System Architecture
High-Level Flow
User → Backend (FastAPI) → Planner Module → Search Module → Scoring Module → Final Report
Architecture Description
The system follows a modular backend design:
main.py handles user input and orchestration
planner.py generates structured sub-questions
search.py retrieves relevant information
scoring.py ranks and filters results
Final structured research output is returned
Architecture Diagram
[User Input]
     ↓
[FastAPI Backend]
     ↓
[Planner Module]
     ↓
[Search Module]
     ↓
[Scoring Module]
     ↓
[Structured Research Report]

5. Database Design
Database Approach
No database used. The system is stateless and operates in real time.
Design Rationale
No persistence required
Simplified architecture
Scalable serverless deployment compatibility

6. Dataset Selected
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
Preprocessing Steps
Structured prompt engineering
Output validation
Enforcing 5–7 question constraint
Response formatting validation

7. Model Selected
Model Name
API-based LLM (e.g., Gemini 1.5 Flash)
Selection Reasoning
Low latency
Cost-effective
Reliable structured output
Suitable for real-time decomposition
Alternatives Considered
Model
Pros
Cons
GPT-4o
High reasoning quality
Expensive
Claude
Strong reasoning
Less structured output
Llama3
Open-source
Requires self-hosting

Evaluation Metrics
Completeness (Always 5–7 sub-questions)
Specificity (Searchable phrasing)
Consistency (Low output variation)
Relevance (Aligned to original query)

8. Technology Stack
Frontend
HTML, CSS, JavaScript (Minimal UI)
Backend
Python 3.11
FastAPI
google-generativeai
python-dotenv
ML/AI
API-based LLM
Structured Prompt Engineering
Database
None (Stateless Architecture)
Deployment
Vercel (Frontend)
Docker (Backend – Planned)

9. API Documentation & Testing
Endpoint 1
POST /generate
Input:
{
 "query": "EV market strategies in India?"
}
Output:
{
 "subquestions": [
   "What is the current market size of EVs in India?",
   "Who are the major competitors?",
   "What regulatory policies affect EV adoption?",
   "What infrastructure challenges exist?",
   "What are projected growth trends?"
 ]
}
API tested using Thunder Client / Postman.

10. Module-wise Development & Deliverables
Checkpoint 1: Research & Planning ✅
Deliverables: Problem definition, architecture design
Checkpoint 2: Backend Development ✅
Deliverables: modules/planner.py
Checkpoint 3: Frontend Development ⏳
Deliverables: Minimal UI integration
Checkpoint 4: Model Training ☑️ Skipped
Zero-shot LLM used
Checkpoint 5: Model Integration ✅
Deliverables: Planner integrated with API
Checkpoint 6: Deployment ⏳
Deliverables: Docker setup (planned)

11. End-to-End Workflow
User enters research question
Planner module generates 5–7 sub-questions
Search module retrieves information
Scoring module ranks quality
Structured research output delivered

12. Demo & Repository
Live Demo: python main.py
GitHub Repository:
https://github.com/TheGreatPratyush/Research_analyser-

13. Hackathon Deliverables Summary
✅ AI Planner Module
✅ Structured Output System
✅ Modular Backend Architecture
⏳ Search & Scoring Integration
⏳ UI Enhancement

14. Team Roles & Responsibilities
Member
Role
Responsibilities
Shanmukha Sai Chakali
Planner Module
modules/planner.py
Vishal Kumar Gowda
Search Module
modules/search.py
Pratyush Gupta
Scoring & Integration
modules/scoring.py


15. Future Scope & Scalability
Short-Term
Sub-question relevance scoring
Multi-language support
Query caching
Long-Term
Custom fine-tuned research LLM
Academic database integration
Enterprise SaaS deployment

16. Known Limitations
API dependency
English-only support
No offline mode
No persistent storage

17. Impact
Reduces research planning time
Improves research completeness
Standardizes decomposition across teams
Enables scalable autonomous research pipelines
