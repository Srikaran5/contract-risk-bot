def calculate_risk(clauses):
    risk_score = 0
    risk_details = {}

    for clause, status in clauses.items():
        if status == "Found":
            risk_score += 1
            risk_details[clause] = "Medium Risk"
        else:
            risk_details[clause] = "Low Risk"

    if risk_score >= 4:
        overall = "HIGH RISK"
    elif risk_score >= 2:
        overall = "MEDIUM RISK"
    else:
        overall = "LOW RISK"
    return overall, risk_details