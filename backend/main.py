from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import random

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
    "attendance": 10,
    "tasks_completed": 0,
    "tasks_total": 10,
    "report_score": 0,
    "verified_skills": [],
    "lifecycle_stage": 5 
}

def calculate_health_score(attendance, tasks_done, tasks_total, report_score):
    if tasks_total == 0: return 0
    task_ratio = tasks_done / tasks_total
    score = (attendance * 0.4) + (task_ratio * 100 * 0.4) + (report_score * 0.2)
    return int(score)

def detect_risk(health_score, attendance):
    if attendance < 50 or health_score < 40: return "High Risk"
    if 50 <= attendance < 75 or 40 <= health_score < 70: return "Medium Risk"
    return "Low Risk"

def extract_skills_mock(text):
    skills_list = ["python", "fastapi", "react", "mongodb", "sql", "docker", "machine learning"]
    found = [s for s in skills_list if s in text.lower()]
    return found

@app.get("/api/v1/dashboard/{role}")
def get_dashboard_data(role: str):
    if role == "student":
        health_score = calculate_health_score(
            student_live_data["attendance"], 
            student_live_data["tasks_completed"], 
            student_live_data["tasks_total"], 
            student_live_data["report_score"]
        )
        risk_level = detect_risk(health_score, student_live_data["attendance"])
        return {
            "role": "student",
            "metrics": {
                "health_score": health_score,
                "risk_status": risk_level,
                "core_stats": student_live_data
            }
        }
    elif role == "mentor":
        return {"role": "mentor", "metrics": {"pending_reports": 12, "at_risk_students": 3, "tasks_to_approve": 8}}
    elif role == "admin":
        return {"role": "admin", "metrics": {"total_interns": 245, "avg_health_score": 82, "active_companies": 15}}

@app.post("/api/v1/submit-report")
def submit_report(payload: ReportPayload):
    extracted_raw = extract_skills_mock(payload.report_content)
    new_skills_with_conf = [{"skill": s, "confidence": random.randint(85, 98)} for s in extracted_raw]
    
    existing_skill_names = [s["skill"] for s in student_live_data["verified_skills"]]
    added_skills = [s for s in new_skills_with_conf if s["skill"] not in existing_skill_names]
    
    student_live_data["verified_skills"].extend(added_skills)
    student_live_data["tasks_completed"] = min(student_live_data["tasks_completed"] + 1, student_live_data["tasks_total"])
    student_live_data["report_score"] = min(student_live_data["report_score"] + random.randint(15, 25), 100)
    student_live_data["attendance"] = min(student_live_data["attendance"] + random.randint(20, 30), 100)
    
    health_score = calculate_health_score(
        student_live_data["attendance"], 
        student_live_data["tasks_completed"], 
        student_live_data["tasks_total"], 
        student_live_data["report_score"]
    )
    risk_level = detect_risk(health_score, student_live_data["attendance"])
    
    return {
        "status": "success",
        "analysis_pipeline": {
            "new_skills_extracted": added_skills,
            "health_score_updated": health_score,
            "ai_action": f"Verified {len(added_skills)} new skills. Advancing to next learning module."
        }
    }
