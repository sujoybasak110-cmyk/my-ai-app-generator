import streamlit as st
import google.generativeai as genai

# --- CONFIGURATION ---
# Yahan apni Google AI Studio wali API Key daalein
API_KEY = AIzaSyA-nr5V4yjRipA08bmKUwO9PGP6LrV2xnc
genai.configure(api_key=API_KEY)

# Gemini Model setup (Flash model fast aur free hai)
model = genai.GenerativeModel('gemini-1.5-flash')

# --- UI SETUP ---
st.set_page_config(page_title="AI App Builder", layout="wide")

st.title("🤖 Prompt to Web App Generator")
st.write("Bas bataiye aapko kya app chahiye, aur AI uska code likh dega!")

# User Input
user_prompt = st.text_area("Aapko kaisa app chahiye?", 
                         placeholder="Example: Ek unit converter app banao jo length aur weight convert kare...",
                         height=150)

if st.button("Generate My App 🚀"):
    if not user_prompt:
        st.warning("Pehle kuch toh likhiye!")
    else:
        with st.spinner("AI aapke liye app design kar raha hai..."):
            # AI ko instruction dena
            system_instruction = (
                "You are an expert web developer. Create a fully functional, single-file web application "
                "using HTML, CSS (Tailwind CSS for styling), and JavaScript based on the user's request. "
                "Return ONLY the code. Do not include any explanations or markdown formatting like ```html."
            )
            
            # Code generate karna
            response = model.generate_content(f"{system_instruction}\n\nUser Request: {user_prompt}")
            generated_code = response.text
            
            # --- OUTPUT ---
            st.success("Aapka App Taiyar Hai!")
            
            # Tabs for Preview and Code
            tab1, tab2 = st.tabs(["🌐 Live Preview", "💻 Source Code"])
            
            with tab1:
                # App ko live dikhana
                st.components.v1.html(generated_code, height=600, scrolling=True)
            
            with tab2:
                # Raw code dikhana
                st.code(generated_code, language='html')
                st.download_button("Download HTML File", generated_code, file_name="my_ai_app.html")
