import spacy
from spacy.cli import download

try:
    nlp = spacy.load("en_core_web_sm")
except:
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

IMPORTANT_KEYWORDS = {
    "Penalty": ["penalty", "fine", "charge"],
    "Termination": ["terminate", "termination"],
    "Indemnity": ["indemnify", "indemnification"],
    "Jurisdiction": ["jurisdiction", "court", "law"],
    "Non-Compete": ["non-compete", "restriction"]
}

def extract_clauses(text):
    clauses = {}
    lower_text = text.lower()
    for clause, keywords in IMPORTANT_KEYWORDS.items():
        for word in keywords:
            if word in lower_text:
                clauses[clause] = "Found"
                break
        else:
            clauses[clause] = "Not Found"
    return clauses

def extract_entities(text):
    doc = nlp(text)
    entities = {"ORG": [], "DATE": [], "MONEY": []}
    for ent in doc.ents:
        if ent.label_ in entities:
            entities[ent.label_].append(ent.text)
    return entities