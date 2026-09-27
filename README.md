# Smart Internship Enterprise System | InternAI Edition

An enterprise-grade, AI-powered platform designed to manage, monitor, and improve the complete lifecycle of internships through continuous tracking, automated NLP-based skill extraction, and proactive risk management.

## 🚀 Key Innovation Features (Hackathon Highlights)

1. **AI Internship Digital Twin:** Provides a live, data-driven model of a student's internship journey, calculating dynamic Health Scores and real-time risk assessments based on performance metrics.
2. **Evidence-Based Skill Graph & Radar Engine:** Utilizes natural language processing to parse student reports, extract technical skills with confidence scores, and dynamically map them against target role requirements using an interactive Radar Chart.
3. **Live AI Activity Terminal:** Features an interactive audit trail that visualizes the AI's step-by-step processing pipeline (tokenization, entity extraction, and gap analysis) during live demonstrations.
4. **Continuous Feedback Loop:** Proactively detects performance drops, explains underlying causes, and triggers automated recommendations and mentor interventions.

## 🛠 Tech Stack

* **Frontend:** HTML5, Tailwind CSS, Vanilla JavaScript, Chart.js (Radar & Dynamic Analytics)
* **Backend:** FastAPI (Python), Pydantic, Uvicorn
* **AI/NLP Engine:** Custom heuristic NLP extraction pipeline with dynamic confidence scoring
* **Database:** MongoDB (PyMongo integration)

## 📂 Project Structure

* `backend/main.py`: Core FastAPI application and REST endpoints.
* `backend/ai_scorer.py`: Intelligence module for health scoring, skill gap detection, and risk analysis.
* `backend/database.py`: Database connection configuration.
* `Frontend/index.html`: Complete enterprise UI/UX with glassmorphism and real-time visualization.
* `requirements.txt`: Python package dependencies.

## ⚙️ Setup & Installation

1. Create a virtual environment:
   ```bash
   python -m venv venv