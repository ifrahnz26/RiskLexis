import streamlit as st
from transformers import pipeline, T5Tokenizer, T5ForConditionalGeneration
from PyPDF2 import PdfReader
from docx import Document
from io import StringIO
from fpdf import FPDF

# Load the model and tokenizer
@st.cache_resource
def load_pipeline():
    model_name = "valhalla/t5-base-qg-hl"  # Replace with a fine-tuned model for legal risk assessment
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)
    return pipeline("text2text-generation", model=model, tokenizer=tokenizer)

# Initialize pipeline
risk_assessment_pipeline = load_pipeline()

# Streamlit App UI
st.title("Enhanced Contract Risk Assessment Tool")
st.write("Analyze contract clauses for risks and get correction suggestions.")

# File Upload
uploaded_file = st.file_uploader("Upload a contract file (.txt, .docx, .pdf):", type=["txt", "docx", "pdf"])
max_clauses = st.slider("Select the maximum number of clauses to assess:", 1, 20, 5)

# Read file content
def read_uploaded_file(file):
    if file.name.endswith(".txt"):
        return StringIO(file.read().decode("utf-8")).read()
    elif file.name.endswith(".docx"):
        doc = Document(file)
        return "\n".join([p.text for p in doc.paragraphs])
    elif file.name.endswith(".pdf"):
        reader = PdfReader(file)
        return "\n".join([page.extract_text() for page in reader.pages])
    return ""

# Process the file
contract_text = ""
if uploaded_file:
    contract_text = read_uploaded_file(uploaded_file)

# Button to analyze risks
if st.button("Assess Risk"):
    if contract_text:
        st.subheader("Risk Assessment Results")
        with st.spinner("Assessing risks..."):
            try:
                clauses = contract_text.split(". ")
                clauses = clauses[:max_clauses]  # Limit number of clauses
                
                results = []
                for idx, clause in enumerate(clauses):
                    formatted_input = f"Assess the risk of the following contract clause: {clause}"
                    generated = risk_assessment_pipeline(formatted_input, max_length=128, num_return_sequences=1)
                    risk_assessment = generated[0]["generated_text"]

                    # Mock risk and correction logic
                    risk_score = 5  # Replace with model logic for score extraction
                    if "high" in risk_assessment.lower():
                        risk_level = "High"
                    elif "medium" in risk_assessment.lower():
                        risk_level = "Medium"
                    else:
                        risk_level = "Low"

                    results.append({
                        "Clause": clause,
                        "Risk Assessment": risk_assessment,
                        "Risk Level": risk_level,
                    })

                # Display results in Streamlit
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=12)

                for idx, result in enumerate(results):
                    st.markdown(f"### Clause {idx + 1}")
                    st.markdown(f"**Clause:** {result['Clause']}")
                    st.markdown(f"**Risk Level:** {result['Risk Level']}")
                    st.markdown(f"**Risk Assessment:** {result['Risk Assessment']}")
                    st.write("---")

                    # Add to PDF
                    pdf.cell(200, 10, txt=f"Clause {idx + 1}: {result['Clause']}", ln=True)
                    pdf.cell(200, 10, txt=f"Risk Level: {result['Risk Level']}", ln=True)
                    pdf.cell(200, 10, txt=f"Risk Assessment: {result['Risk Assessment']}", ln=True)
                    pdf.cell(200, 10, txt=" ", ln=True)

                # Allow download of the PDF
                pdf_output = StringIO()
                pdf.output(pdf_output)
                pdf_output.seek(0)

                st.download_button(
                    label="Download Results as PDF",
                    data=pdf_output.getvalue(),
                    file_name="risk_assessment_results.pdf",
                    mime="application/pdf",
                )
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.error("Please upload a file or input contract text to perform the risk assessment.")
else:
    st.info("Upload a contract file and click 'Assess Risk' to get started.")


