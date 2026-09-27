import re

REQUIRED_SKILLS = ["python", "fastapi", "react", "mongodb", "sql", "machine learning", "nlp", "docker"]

def calculate_health_score(attendance: int, tasks_completed: int, tasks_total: int, report_score: int) -> int:
    task_ratio = (tasks_completed / tasks_total) * 100 if tasks_total > 0 else 0
    score = (attendance * 0.4) + (task_ratio * 0.4) + (report_score * 0.2)
    return int(score)

def detect_risk(health_score: int, attendance: int) -> str:
    if health_score < 60 or attendance < 75:
        return "High Risk"
    elif health_score < 80:
        return "Medium Risk"
    return "Low Risk"

def extract_skills(text: str) -> list:
    text_lower = text.lower()
    found_skills = [skill for skill in REQUIRED_SKILLS if re.search(r'\b' + re.escape(skill) + r'\b', text_lower)]
    return list(set(found_skills))

def detect_skill_gap(demonstrated_skills: list, role_required_skills: list) -> list:
    return [skill for skill in role_required_skills if skill not in demonstrated_skills]

def generate_recommendation(risk_level: str, skill_gaps: list) -> dict:
    actions = []
    if risk_level == "High Risk":
        actions.append("Schedule immediate mentor intervention.")
    if skill_gaps:
        actions.append(f"Complete mandatory modules for: {', '.join(skill_gaps)}")
    
    if not actions:
        actions.append("Maintain current progress trajectory.")
        
    return {
        "primary_action": actions[0],
        "all_actions": actions
    }