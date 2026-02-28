import streamlit as st
import google.generativeai as genai

# --- 1. CONFIGURATION ---
# Apni API Key yahan quotes ke beech mein check kar lein
API_KEY = "AIzaSyA-nr5V4yjRlpA08bmKUwO9PGP6LrV2xnc" 
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

# --- 2. UI SETUP ---
st.set_page_config(page_title="Pro Financial AI", page_icon="📊", layout="wide")

st.title("📊 AI Financial Report Builder")
st.markdown("""
    **Instruction:** Niche box mein bas apne data ka chota sa description likhiye. 
    AI ek aisa tool banayega jo **CSV/Excel file upload** lega aur uska **Pie Chart** bana dega.
""")

# --- 3. MASTER PROMPT ---
# Maine aapka manga hua detail wala prompt yahan fix kar diya hai
master_prompt = """
Act as an expert Data Scientist. Create a high-end Financial Dashboard web app in a single HTML file.
1. File Input Section: Add a uploader that can parse CSV data.
2. Data Processing: Identify columns like 'Category' and 'Amount'. Calculate Total Spending and Top Category.
3. Visualizations: Create a beautiful Pie Chart using Chart.js for 'Expense by Category'. Use a modern dark-blue theme.
4. UI Design: Use Tailwind CSS for a professional SaaS look.
Output ONLY the raw HTML/JS code.
"""

user_input = st.text_area("Kuch extra features add karne hain? (Optional)", 
                         placeholder="Example: Add a 'Download PDF' button also...")

if st.button("Build My Financial Analyzer 🚀"):
    with st.spinner("AI aapka Financial Tool design kar raha hai..."):
        try:
            # AI ko master prompt + user ki extra demand bhejna
            final_query = f"{master_prompt} \nExtra User Demand: {user_input}"
            response = model.generate_content(final_query)
            
            clean_code = response.text.replace("```html", "").replace("```", "").strip()
            
            # App Preview
            st.subheader("✅ Aapka Tool Taiyar Hai!")
            st.info("Niche diye gaye tool mein apni CSV file upload karein.")
            st.components.v1.html(clean_code, height=700, scrolling=True)
            
            # Code Backup
            with st.expander("Source Code Copy Karein"):
                st.code(clean_code, language='html')
                
        except Exception as e:
            st.error(f"Error: {e}")

st.divider()
st.caption("Sujoy's AI Financial Project - 2026")
