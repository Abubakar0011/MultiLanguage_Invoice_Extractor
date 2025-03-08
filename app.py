import google.generativeai as genai
import streamlit as st
import os
from dotenv import load_dotenv
from PIL import Image

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GIMINI_API_KEY")

if not API_KEY:
    st.error("Error: GEMINI_API_KEY is missing. Check environment variables.")
    st.stop()

genai.configure(api_key=API_KEY)

# Load Gemini Vision model
model = genai.GenerativeModel("models/gemini-2.0-flash")


def get_response(input_text, image, prompt):
    """
    Generates a response using Gemini Vision model.
    
    Args:
        input_text (str): The user's input prompt.
        image (list): The processed image data.
        prompt (str): Additional prompt for the model.
    
    Returns:
        str: The extracted invoice details.
    """
    response = model.generate_content([input_text, image[0], prompt])
    return response.text


def process_uploaded_image(uploaded_file):
    """
    Processes the uploaded image and converts it into model-compatible format.
    
    Args:
        uploaded_file: The uploaded image file.
    
    Returns:
        list: A list containing image type and data.
    """
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        return [{"mime_type": uploaded_file.type, "data": bytes_data}]
    else:
        raise FileNotFoundError("No image uploaded")

# Initialize Streamlit app


st.set_page_config(page_title="MultiLanguage Invoice Extractor")
st.header("MultiLanguage Invoice Extractor")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# User input
input_text = st.text_input("Input Prompt:", key="input")
uploaded_file = st.file_uploader("Choose an invoice image...",
                                 type=["jpg", "jpeg", "png"])

# Display uploaded image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

# Button for extracting invoice details
submit = st.button("Extract Invoice")
input_prompt = """
Extract the invoice details from the image and answer all related questions.
"""

if submit:
    try:
        image_data = process_uploaded_image(uploaded_file)
        response = get_response(input_text, image_data, input_prompt)
        st.subheader("Extracted Invoice Details")
        st.write(response)
        
        # Store chat history
        st.session_state["chat_history"].append(("You", input_text))
        st.session_state["chat_history"].append(("Bot", response))
    except FileNotFoundError as e:
        st.error(str(e))

# Display chat history
st.subheader("Chat History")
for role, text in st.session_state["chat_history"]:
    st.write(f"{role}: {text}")
