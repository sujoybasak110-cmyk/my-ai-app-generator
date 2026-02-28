import streamlit as st
import google.generativeai as genai

# --- CONFIGURATION ---
# Dhyan dein: Quotes " " lagana zaroori hai
API_KEY = "AIzaSyA-nr5V4yjRlpA08bmKUwO9PGP6LrV2xnc" 
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

# --- UI SETUP ---
st.set_page_config(page_title="AI App Builder", layout="wide")

st.title("🤖 Prompt to Web App Generator")
st.write("Bas bataiye aapko kya app chahiye, aur AI uska code likh dega!")

user_prompt = st.text_area("Aapko kaisa app chahiye?", placeholder="Example: Ek unit converter banao...")

if st.button("Generate My App 🚀"):
    if not user_prompt:
        st.warning("Pehle kuch likhiye!")
    else:
        with st.spinner("AI dimaag laga raha hai..."):
            # AI ko prompt bhejna
            response = model.generate_content(f"Create a single file HTML/CSS web app for: {user_prompt}. Output ONLY the code.")
            generated_code = response.text.replace("```html", "").replace("```", "")
            
            # Result dikhana
            st.subheader("Aapka App Taiyar Hai!")
            st.components.v1.html(generated_code, height=600, scrolling=True)
            st.code(generated_code, language='html')