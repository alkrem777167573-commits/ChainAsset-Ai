import streamlit as st
import os
from radar_core import ChainAssetRadar

# Initialize the ChainAsset AI Radar Engine
@st.cache_resource
def load_radar():
    return ChainAssetRadar()

radar = load_radar()

# Configure the Streamlit Web Interface Page
st.set_page_config(page_title="ChainAsset AI Dashboard", page_icon="🚀", layout="wide")

st.title("🌐 ChainAsset AI: Autonomous Enterprise Asset & Warranty Radar")
st.subheader("Leveraging Google Gemini & Blockchain for Fraud-Proof Operations")
st.markdown("---")

# Create Two Functional Tabs for the Two Core Radar Tasks
tab1, tab2 = st.tabs(["📊 Invoice Auditing & Fraud Detection", "📜 Legal Warranty Compliance"])

# -------------------------------------------------------------------------
# TAB 1: Invoice Auditing & Fraud Detection
# -------------------------------------------------------------------------
with tab1:
    st.header("Invoice Auditing & Fraud Detection Radar")
    st.write("Upload an invoice or receipt image/PDF to compute its Operational Integrity Score against market data.")
    
    # Inputs
    uploaded_invoice = st.file_uploader("Upload Maintenance Invoice (PDF/PNG/JPG)", type=["pdf", "png", "jpg"], key="invoice")
    market_data_input = st.text_area(
        "Current Market Baseline Data (Context)", 
        value="Chiller Sensor Replacement: $40 - $60\nAC Compressor Labor: $150 - $200 per hour\nStandard Electrical Cable (per meter): $5",
        height=100
    )
    
    if st.button("Run Forensic Audit", type="primary"):
        if uploaded_invoice is not None:
            with st.spinner("Gemini Multimodal Vision is auditing the invoice..."):
                # Save uploaded file temporarily to pass to the radar core
                temp_path = f"temp_{uploaded_invoice.name}"
                with open(temp_path, "wb") as f:
                    f.write(uploaded_invoice.getbuffer())
                
                # Execute the audit via Gemini
                audit_result = radar.audit_invoice(temp_path, market_data_input)
                
                # Display Results
                st.success("Audit Analysis Completed Successfully!")
                st.markdown("### 📋 Audit Report & Integrity Score")
                st.write(audit_result)
                
                # Clean up temp file
                if os.path.exists(temp_path):
                    os.remove(temp_path)
        else:
            st.error("Please upload an invoice file first.")

# -------------------------------------------------------------------------
# TAB 2: Legal Warranty Compliance
# -------------------------------------------------------------------------
with tab2:
    st.header("Smart Warranty & Liability Compliance Radar")
    st.write("Upload dense vendor contracts and input field incident logs to determine active warranty coverage.")
    
    # Inputs
    uploaded_contract = st.file_uploader("Upload Legal Contract / Warranty Document (PDF)", type=["pdf"], key="contract")
    incident_details_input = st.text_area(
        "Reported Field Incident Details", 
        placeholder="Example: Chiller Unit 3 in Sector B failed due to a compressor burnout on May 29, 2026. Installed 8 months ago.",
        height=100
    )
    
    if st.button("Check Warranty Status", type="primary"):
        if uploaded_contract is not None and incident_details_input.strip() != "":
            with st.spinner("Gemini Long-Context Engine is parsing legal liabilities..."):
                # Save uploaded file temporarily to pass to the radar core
                temp_path = f"temp_{uploaded_contract.name}"
                with open(temp_path, "wb") as f:
                    f.write(uploaded_contract.getbuffer())
                
                # Execute compliance verification via Gemini
                compliance_result = radar.check_warranty_compliance(temp_path, incident_details_input)
                
                # Display Results
                st.success("Compliance Check Completed Successfully!")
                st.markdown("### ⚖️ Legal Verdict & Vendor Claims")
                st.write(compliance_result)
                
                # Clean up temp file
                if os.path.exists(temp_path):
                    os.remove(temp_path)
        else:
            st.error("Please upload the contract document and provide incident details.")

# Footer
st.markdown("---")
st.caption("ChainAsset AI v1.0.0 • Developed for the XPRIZE Gemini Hackathon 2026")
