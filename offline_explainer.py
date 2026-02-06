EXPLANATIONS = {
    "Termination": (
        "This clause explains how the contract can be ended. "
        "It tells when one or both parties are allowed to stop the agreement."
    ),
    "Penalty": (
        "This clause explains the fine or money that must be paid "
        "if one party breaks the contract or fails to meet conditions."
    ),
    "Indemnity": (
        "This clause means one party agrees to cover losses, damages, "
        "or legal costs suffered by the other party."
    ),
    "Jurisdiction": (
        "This clause decides which city or court will handle "
        "any legal disputes related to the contract."
    ),
    "Non-Compete": (
        "This clause restricts a person or company from working "
        "with competitors for a certain period of time."
    )
}

def explain_clause_offline(clause_name):
    return EXPLANATIONS.get(
        clause_name,
        "This clause contains important legal conditions in the contract."
    )