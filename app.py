import streamlit as st
from PyPDF2 import PdfReader
from docx import Document

from contract_analyzer import extract_clauses, extract_entities
from risk_rules import calculate_risk
from similarity import check_similarity
from pdf_export import generate_pdf
from offline_explainer import explain_clause_offline
from translator import translate_to_english

st.set_page_config(page_title="Contract Risk Analyzer", layout="wide")

st.title("📄 Contract Analysis & Risk Assessment Bot")

uploaded_file = st.file_uploader(
    "Upload Contract (PDF / DOCX / TXT)",
    type=["pdf", "docx", "txt"]
)

def read_file(file):
    if file.name.endswith(".pdf"):
        reader = PdfReader(file)
        return " ".join([page.extract_text() for page in reader.pages])
    elif file.name.endswith(".docx"):
        doc = Document(file)
        return " ".join([p.text for p in doc.paragraphs])
    else:
        return file.read().decode("utf-8")

def translate_action():
    st.session_state.text_data = translate_to_english(st.session_state.text_data)

if uploaded_file:
    file_text = read_file(uploaded_file)

    if "text_data" not in st.session_state:
        st.session_state.text_data = file_text

    st.subheader("📌 Contract Text ")

    st.text_area(
        "Paste Contract Text here",
        key="text_data",
        height=280
    )

    st.button(
        "🌐 Translate Hindi → English",
        on_click=translate_action
    )

    text = st.session_state.text_data

    clauses = extract_clauses(text)
    entities = extract_entities(text)
    overall_risk, risk_details = calculate_risk(clauses)

    st.subheader("⚠️ Risk Assessment")
    st.write("**Overall Risk:**", overall_risk)

    st.subheader("📄 Clause Analysis")
    for k, v in risk_details.items():
        st.write(f"- **{k}** : {v}")

    st.subheader("📊 Clause Similarity Score")
    similarity_score = check_similarity(text)
    st.write(f"Similarity with known risky clauses: {round(similarity_score * 100, 2)}%")

    st.subheader("🧠 English Explanation")
    for clause in clauses:
        st.write(f"**{clause}**")
        st.info(explain_clause_offline(clause))

    st.subheader("🔍 Key Entities")
    st.json(entities)

    if st.button("📄 Download PDF Report"):
        pdf_path = generate_pdf(overall_risk, risk_details, entities)
        with open(pdf_path, "rb") as f:
            st.download_button(
                "Download Report",
                f,
                file_name="Contract_Report.pdf"
            )