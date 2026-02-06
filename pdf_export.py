from fpdf import FPDF

def generate_pdf(overall_risk, clauses, entities):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, "Contract Risk Assessment Report", ln=True)
    pdf.cell(0, 10, f"Overall Risk: {overall_risk}", ln=True)
    pdf.cell(0, 10, "Clause Analysis:", ln=True)
    for k, v in clauses.items():
        pdf.cell(0, 10, f"{k}: {v}", ln=True)
        
    pdf.cell(0, 10, "Key Entities:", ln=True)
    pdf.multi_cell(0, 10, str(entities))
    file_path = "contract_report.pdf"
    pdf.output(file_path)
    return file_path