import streamlit as st
from openai import OpenAI

# OpenRouter API
client = OpenAI(
    api_key=st.secrets["OPENROUTER_API_KEY"],
    base_url="https://openrouter.ai/api/v1"
)

def review_code(code):
    prompt = f"""
You are an AI code reviewer for students.

Analyze the code and provide:
1. Syntax Errors
2. Logical Errors
3. Simple Explanation
4. Suggestions
5. Improved Code

Code:
{code}
"""

    response = client.chat.completions.create(
    model="openai/gpt-4o-mini",   # ✔ This works 100%
    messages=[
        {"role": "system", "content": "You are a helpful code reviewer."},
        {"role": "user", "content": prompt}
    ]
)
    return response.choices[0].message.content

# UI
st.set_page_config(page_title="AI Code Reviewer", page_icon="👨‍💻")
st.title("👨‍💻 AI Code Reviewer")

code = st.text_area("Paste your code here:", height=300)

if st.button("Review Code"):
    if code.strip():
        with st.spinner("Analyzing your code..."):
            result = review_code(code)
            st.success("Review Completed!")
            st.write(result)
    else:
        st.warning("Please paste some code first!")
