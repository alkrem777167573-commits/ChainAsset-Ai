import os
from google import genai
from google.genai import types

class ChainAssetRadar:
    def __init__(self):
        """
        Initialize the radar engine and connect to Google GenAI API.
        """
        self.client = genai.Client()
        self.model_name = "gemini-2.5-pro"

    def audit_invoice(self, invoice_file_path: str, historical_market_data: str) -> str:
        """
        1️⃣ Fraud Detection & Invoice Auditing Radar (Vision & Multimodal)
        Analyzes invoice images/PDFs and flags overcharging or statistical anomalies.
        """
        if not os.path.exists(invoice_file_path):
            return "Error: Invoice file not found."
            
        invoice_uploaded = self.client.files.upload(file=invoice_file_path)
        
        prompt = f"""
        You are the Lead Forensic Auditor for ChainAsset AI. Analyze this maintenance invoice/receipt 
        and calculate an integrity score by cross-referencing it with the provided market baseline data.
        
        Market Baseline Data:
        {historical_market_data}
        
        Strictly evaluate pricing anomalies or fraud flags, and output an 'Operational Integrity Score' (0-100%).
        """
        
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=[invoice_uploaded, prompt]
        )
        return response.text

    def check_warranty_compliance(self, contract_file_path: str, incident_details: str) -> str:
        """
        2️⃣ Smart Warranty & Compliance Radar (Long Context Handling)
        Parses dense legal contracts to check if a field incident is covered by active warranties.
        """
        if not os.path.exists(contract_file_path):
            return "Error: Contract/Warranty file not found."
            
        contract_uploaded = self.client.files.upload(file=contract_file_path)
        
        prompt = f"""
        You are the Legal & Operations Officer for ChainAsset AI. Review this legal asset/warranty contract and determine 
        if the following operational incident is covered under active vendor liability or warranty periods.
        
        Reported Field Incident Details:
        {incident_details}
        
        Provide a verdict and draft a formal claim message to the vendor if covered.
        """
        
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=[contract_uploaded, prompt]
        )
        return response.text

if __name__ == "__main__":
    radar = ChainAssetRadar()
    print("🚀 ChainAsset AI Operational Radar Engine initialized successfully!")
