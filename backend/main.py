from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import random
import backend.ai_scorer as ai_scorer

app = FastAPI(title="Smart Internship Engine API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ReportPayload(BaseModel):
    student_id: str
    report_content: str
    target_role_skills: List[str]

student_live_data = {
    "attendance": 85,
    "tasks_completed": 7,
    "tasks_total": 10,
    "report_score": 75,
    "verified_skills": [{"skill": "python", "confidence": 98}, {"skill": "react", "confidence": 85}],
    "lifecycle_stage": 5 
}

@app.get("/api/v1/dashboard/{role}")
def get_dashboard_data(role: str):
    if role == "student":
        health_score = ai_scorer.calculate_health_score(
            student_live_data["attendance"], 
            student_live_data["tasks_completed"], 
            student_live_data["tasks_total"], 
            student_live_data["report_score"]
        )
        risk_level = ai_scorer.detect_risk(health_score, student_live_data["attendance"])
        return {
            "role": "student",
            "metrics": {
                "health_score": health_score,
                "risk_status": risk_level,
                "core_stats": student_live_data
            }
        }
    elif role == "mentor":
        return {
            "role": "mentor",
            "metrics": {
                "pending_reports": 12,
                "at_risk_students": 3,
                "tasks_to_approve": 8
            }
        }
    elif role == "admin":
        return {
            "role": "admin",
            "metrics": {
                "total_interns": 245,
                "avg_health_score": 82,
                "active_companies": 15
            }
        }

@app.post("/api/v1/submit-report")
def submit_report(payload: ReportPayload):
    extracted_raw = ai_scorer.extract_skills(payload.report_content)
    
    new_skills_with_conf = [{"skill": s, "confidence": random.randint(75, 99)} for s in extracted_raw]
    
    existing_skill_names = [s["skill"] for s in student_live_data["verified_skills"]]
    added_skills = [s for s in new_skills_with_conf if s["skill"] not in existing_skill_names]
    
    student_live_data["verified_skills"].extend(added_skills)
    
    student_live_data["tasks_completed"] = min(student_live_data["tasks_completed"] + 1, student_live_data["tasks_total"])
    student_live_data["report_score"] = min(student_live_data["report_score"] + random.randint(2, 5), 100)
    
    current_skill_names = [s["skill"] for s in student_live_data["verified_skills"]]
    skill_gaps = ai_scorer.detect_skill_gap(current_skill_names, payload.target_role_skills)
    
    health_score = ai_scorer.calculate_health_score(
        student_live_data["attendance"], 
        student_live_data["tasks_completed"], 
        student_live_data["tasks_total"], 
        student_live_data["report_score"]
    )
    risk_level = ai_scorer.detect_risk(health_score, student_live_data["attendance"])
    recommendations = ai_scorer.generate_recommendation(risk_level, skill_gaps)
    
    return {
        "status": "success",
        "analysis_pipeline": {
            "new_skills_extracted": added_skills,
            "current_gaps": skill_gaps,
            "health_score_updated": health_score,
            "ai_action": recommendations["primary_action"]
        }
    }