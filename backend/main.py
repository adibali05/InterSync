from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any, Optional, List

app = FastAPI(title="InternSync Enterprise API", version="17.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ActionPayload(BaseModel):
    action_type: str
    target_id: str
    data: Dict[str, Any]

def generate_role_tasks(role: str):
    role_lower = role.lower()
    if "ai" in role_lower:
        modules = [
            "Python & NumPy Foundations", "Exploratory Data Analysis", "Scikit-Learn Regression Models", 
            "Classification & Metrics", "Deep Learning Neural Networks", "PyTorch Tensor Operations", 
            "Convolutional Neural Networks", "Recurrent Neural Networks (RNN)", "Transformers Architecture", 
            "Hugging Face Fine-Tuning", "RAG & Vector Databases", "LangChain Framework Integration", 
            "FastAPI Model Serving", "Docker Containerization", "Model Quantization", 
            "MLOps & CI/CD Pipelines", "Model Monitoring & Drift", "Scalable Cloud Deployment", 
            "Capstone Project Planning", "Capstone Model Training", "Capstone Evaluation", 
            "Documentation & Testing", "Security & Ethical AI Audit", "Final Industry Presentation"
        ]
    elif "backend" in role_lower:
        modules = [
            "Advanced Python & OOP", "FastAPI Core Routing", "Pydantic Data Validation", 
            "Relational Database Design", "SQLAlchemy ORM Modeling", "PostgreSQL Advanced Queries", 
            "MongoDB & NoSQL Concepts", "Async/Await Programming", "Authentication & JWT Security", 
            "Role-Based Access Control", "Unit Testing with Pytest", "API Documentation & Swagger", 
            "Caching with Redis", "Background Tasks & Celery", "Dockerization of Services", 
            "CI/CD Pipeline Setup", "Microservices Architecture", "API Rate Limiting", 
            "Logging & Error Handling", "Performance Load Testing", "Database Indexing & Tuning", 
            "Cloud Security Protocols", "System Architecture Review", "Final Production Handover"
        ]
    elif "data" in role_lower:
        modules = [
            "Advanced SQL & Joins", "Pandas & Data Wrangling", "Data Cleaning Techniques", 
            "Statistical Hypothesis Testing", "Data Visualization (Matplotlib/Seaborn)", "Interactive Dashboards (Tableau/PowerBI)", 
            "Time Series Forecasting", "Feature Engineering", "A/B Testing Methodologies", 
            "SQL Performance Tuning", "Big Data Basics (Spark)", "ETL Pipeline Design", 
            "Customer Segmentation", "Predictive Modeling", "Risk Analysis Framework", 
            "Data Governance & Privacy", "Business Metric Reporting", "Automated Reporting Scripts", 
            "Advanced Excel Modeling", "Stakeholder Presentation Prep", "Case Study Analysis", 
            "Data Quality Auditing", "Enterprise Data Strategy", "Final Analytics Presentation"
        ]
    else:
        modules = [
            "HTML5 & Semantic Markup", "Advanced CSS & Flexbox/Grid", "Tailwind CSS Framework", 
            "JavaScript ES6+ Concepts", "DOM Manipulation & Events", "Asynchronous JS & Fetch API", 
            "React Core Components", "React Hooks & State", "React Router Navigation", 
            "State Management (Context API)", "Form Validation & Handling", "RESTful API Integration", 
            "Responsive Web Design", "Performance Optimization", "Web Accessibility (a11y)", 
            "Component Testing (Jest)", "Git Version Control", "Webpack & Vite Bundlers", 
            "UI/UX Design Principles", "Cross-Browser Compatibility", "Progressive Web Apps", 
            "Security Best Practices", "Deployment & Hosting", "Final Portfolio Review"
        ]

    tasks = []
    for idx, title in enumerate(modules, start=1):
        tasks.append({
            "id": idx,
            "week": f"Week {idx}",
            "title": title,
            "status": "Pending"
        })
    return tasks

def calculate_ai_risk_score(app: dict):
    completed_tasks = sum(1 for t in app["tasks"] if t["status"] == "Completed")
    avg_score = (app["academic_cgpa"] * 10 + app["aptitude"] + app["coding"] + app["skills_match"]) / 4
    
    if avg_score >= 85 and completed_tasks >= 2:
        return {"level": "Top PPO Material", "color": "emerald", "badge": "🟢 Top Tier Candidate"}
    elif avg_score >= 70 or completed_tasks >= 1:
        return {"level": "Stable Performer", "color": "blue", "badge": "🔵 On Track"}
    else:
        return {"level": "High Risk / Lagging", "color": "red", "badge": "🔴 Intervention Needed"}

db = {
    "partnership": "G H Raisoni University Amravati x TechNova Solutions",
    "applications": [
        {
            "id": "APP001", "student": "Adib Ali", "email": "adib.ali@raisoni.edu", "role": "AI Engineer", 
            "academic_cgpa": 8.5, "aptitude": 92, "coding": 95, "skills_match": 94, "status": "Recommended by TPO",
            "mentor": "Mr. Vikram (Senior AI Lead)", "tasks": generate_role_tasks("AI Engineer"), "mentor_decision": "Pending", "letters": [], "passport_generated": False
        },
        {
            "id": "APP002", "student": "Anushka", "email": "anushka@raisoni.edu", "role": "Backend Dev", 
            "academic_cgpa": 8.8, "aptitude": 88, "coding": 91, "skills_match": 90, "status": "Recommended by TPO",
            "mentor": "Ms. Shruti (Backend Lead)", "tasks": generate_role_tasks("Backend Dev"), "mentor_decision": "Pending", "letters": [], "passport_generated": False
        },
        {
            "id": "APP003", "student": "Maithily", "email": "maithily@raisoni.edu", "role": "Data Analyst", 
            "academic_cgpa": 9.1, "aptitude": 85, "coding": 88, "skills_match": 89, "status": "Recommended by TPO",
            "mentor": "Mr. Rahul (Data Science Lead)", "tasks": generate_role_tasks("Data Analyst"), "mentor_decision": "Pending", "letters": [], "passport_generated": False
        },
        {
            "id": "APP004", "student": "Riya Sharma", "email": "riya.s@raisoni.edu", "role": "Frontend Dev", 
            "academic_cgpa": 6.8, "aptitude": 55, "coding": 45, "skills_match": 50, "status": "Recommended by TPO",
            "mentor": "Mr. Karan (UI/UX Lead)", "tasks": generate_role_tasks("Frontend Dev"), "mentor_decision": "Pending", "letters": [], "passport_generated": False
        }
    ]
}

@app.get("/api/v1/dashboard/{role}")
def get_dashboard_data(role: str, email: Optional[str] = None):
    for app in db["applications"]:
        app["ai_risk"] = calculate_ai_risk_score(app)

    if role in ["employer", "mentor"]:
        return {"status": "success", "partnership": db["partnership"], "data": db["applications"]}
    
    elif role == "tpo":
        total = len(db["applications"])
        offered = sum(1 for app in db["applications"] if app["status"] in ["Offered", "Mentor_Evaluated", "PPO_Offered", "PPO_Rejected"])
        rejected = sum(1 for app in db["applications"] if app["status"] == "Rejected")
        pending = total - offered - rejected
        stats = {"total": total, "offered": offered, "rejected": rejected, "pending": pending}
        return {"status": "success", "partnership": db["partnership"], "stats": stats, "data": db["applications"]}
    
    elif role == "student":
        if not email:
            raise HTTPException(status_code=400, detail="Email required")
        for app in db["applications"]:
            if app["email"].strip().lower() == email.strip().lower():
                return {"status": "success", "data": app}
        raise HTTPException(status_code=404, detail="Student email not found in database.")

@app.post("/api/v1/action")
def perform_action(payload: ActionPayload):
    for app in db["applications"]:
        if app["id"] == payload.target_id:
            
            if payload.action_type == "PROCESS_DECISION":
                decision = payload.data["decision"]
                app["status"] = "Offered" if decision == "APPROVE" else "Rejected"
                
                if decision == "APPROVE":
                    app["passport_generated"] = True
                    letter = {
                        "title": "1. Internship Offer Letter",
                        "subject": f"Official Internship Offer - {app['role']} at TechNova",
                        "body": f"Dear {app['student']},\n\nCongratulations! Based on your verification scores (CGPA: {app['academic_cgpa']}, Aptitude: {app['aptitude']}%, Coding: {app['coding']}%), TechNova Solutions is thrilled to offer you the 24-week internship role of {app['role']}.\n\nYou are assigned under mentor {app['mentor']}. Your AI Verified Internship Passport has now been successfully generated.\n\nBest Regards,\nCompany HR, TechNova Solutions"
                    }
                    app["letters"].append(letter)
                else:
                    app["passport_generated"] = False
                    letter = {
                        "title": "Status Update Letter",
                        "subject": f"Application Update - {app['role']}",
                        "body": f"Dear {app['student']},\n\nThank you for applying for the {app['role']} position through the G H Raisoni University Amravati placement drive. Unfortunately, your current scores do not meet the criteria for this role.\n\nBest Regards,\nCompany HR, TechNova Solutions"
                    }
                    app["letters"].append(letter)
                    
                return {"status": "success", "email_data": {"to": app["email"], "subject": letter["subject"], "body": letter["body"]}}
            
            elif payload.action_type == "SUBMIT_TASK":
                task_id = int(payload.data["task_id"])
                status = payload.data.get("status", "Completed")
                for task in app["tasks"]:
                    if task["id"] == task_id:
                        task["status"] = status
                return {"status": "success", "message": "Task updated."}

            elif payload.action_type == "BULK_UPDATE_TASKS":
                select_all = payload.data.get("select_all", False)
                new_status = "Completed" if select_all else "Pending"
                for task in app["tasks"]:
                    task["status"] = new_status
                return {"status": "success", "message": "Bulk tasks updated."}
            
            elif payload.action_type == "MENTOR_DECISION":
                app["mentor_decision"] = payload.data["decision"]
                app["status"] = "Mentor_Evaluated"
                return {"status": "success"}

            elif payload.action_type == "HR_FINAL_PPO":
                decision = payload.data["decision"]
                app["status"] = "PPO_Offered" if decision == "APPROVE" else "PPO_Rejected"
                
                if decision == "APPROVE":
                    letter = {
                        "title": "2. Full-Time Placement Offer Letter (PPO)",
                        "subject": f"Full-Time Junior Role Offer - TechNova Solutions",
                        "body": f"Dear {app['student']},\n\nBased on your outstanding completion of all 24-week tasks and your mentor's glowing evaluation, TechNova Solutions is proud to offer you a Full-Time Junior {app['role']} position!\n\nWelcome to the permanent team.\n\nBest Regards,\nCompany HR, TechNova Solutions"
                    }
                    app["letters"].append(letter)
                else:
                    letter = {
                        "title": "2. Internship Completion Notice",
                        "subject": f"Internship Completion Update - TechNova",
                        "body": f"Dear {app['student']},\n\nThank you for successfully finishing your 24-week internship. Based on final mentor reviews, we will not be extending a full-time placement offer at this moment.\n\nBest Regards,\nCompany HR, TechNova Solutions"
                    }
                    app["letters"].append(letter)
                    
                return {"status": "success", "email_data": {"to": app["email"], "subject": letter["subject"], "body": letter["body"]}}
            
    raise HTTPException(status_code=400, detail="Invalid action")