# MultiLanguage Invoice Extractor

## Overview
MultiLanguage Invoice Extractor is a Streamlit-based web application that
leverages Google Gemini AI to extract invoice details from images. It supports
multilingual invoice processing and maintains a chat history of interactions.

## Features
- Upload an invoice image (JPG, JPEG, PNG)
- Extract key invoice details using Gemini AI
- Supports multilingual invoice processing
- Maintains chat history of extracted details and user interactions
- Simple and interactive UI using Streamlit

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Abubakar0011/MultiLanguage_Invoice_Extractor.git
   cd MultiLanguage-Invoice-Extractor
   ```
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Setup
1. Create a `.env` file in the root directory and add your Gemini API key:
   ```
   GIMINI_API_KEY=your_api_key_here
   ```
2. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage
1. Open the application in your browser.
2. Upload an invoice image.
3. Enter an optional input prompt.
4. Click "Extract Invoice" to retrieve extracted invoice details.
5. View chat history for past queries and responses.

## Dependencies
- Python 3.9+
- Streamlit
- streamlit
- google-generativeai
- python-dotenv
- langchain
- PyPDF2
- chromadb
- faiss-cpu


## Author
Developed by Abubakar Saddiq.

