
# RiskLexis: Contract Clause Analysis and Risk Assessment

RiskLexis is an AI-powered solution that leverages advanced Natural Language Processing (NLP) techniques for analyzing contract clauses and assessing their risk levels. Built using the T5 Transformer model, this project streamlines contract review processes, enhancing efficiency and accuracy in legal risk management.

# Contributors
- Ifrah Naaz 
- Lekhya Biridepalli

## Table of Contents
- [Overview](#overview)  
- [Features](#features)  
- [Technologies Used](#technologies-used)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Results](#results)  
- [Future Work](#future-work)  

## Overview
This project automates the identification of high-risk clauses in contracts, replacing traditional manual workflows with an intuitive and interactive platform. The model outperforms the BERT Transformer, demonstrating superior accuracy, precision, and recall in clause classification and risk assessment.

## Features
- **Clause Risk Assessment**: Classifies clauses as Low, Medium, or High risk.  
- **Interactive Streamlit Interface**: Upload contracts in various formats and get real-time analysis.  
- **Detailed Reports**: Generate downloadable risk assessment reports in PDF format.  
- **Improved Legal Efficiency**: Reduces manual review time, allowing legal professionals to focus on critical issues.

## Technologies Used
- **Programming Language**: Python  
- **Libraries and Frameworks**:  
  - Transformers (Hugging Face)  
  - PyTorch  
  - Streamlit  
  - Pandas, Scikit-learn  
  - PyPDF2, python-docx, FPDF  

## Installation
1. Clone the repository:  
   ```bash
   git clone https://github.com/username/RiskLexis.git
   cd RiskLexis
   ```
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:  
   ```bash
   streamlit run app.py
   ```

## Usage
1. Upload a contract file (PDF, DOCX, or TXT).  
2. Select the number of clauses to analyze.  
3. Click "Assess Risk" to get a detailed risk assessment.  
4. Download the report for further review.

## Results
- Achieved an accuracy of **88.14%** with the T5 model.  
- Outperformed BERT in all key metrics: Precision, Recall, and F1 Score.  
- Reduced the time required for manual contract reviews by automating clause analysis.
  
![image](https://github.com/user-attachments/assets/4028e249-d679-472b-967a-7b28b2a50c54)
![image](https://github.com/user-attachments/assets/841375d1-d389-4a4e-8f60-91c90ebf6401)


## Future Work
- Expand the dataset to include more diverse contract types.  
- Integrate multi-language support.  
- Enhance explainability of model predictions for better user trust.  
- Adapt the model for region-specific legal frameworks.

