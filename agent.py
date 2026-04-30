from openai import OpenAI
import streamlit as st
from search import search_hikes
import json

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def run_agent(query):

    # 1. חיפוש אמיתי
    results = search_hikes(query)

    # 2. שליחה ל-AI
    prompt = f"""
יש לך תוצאות חיפוש של מסלולי טיול:

{results}

בחר 2 מסלולים הכי רלוונטיים.

לכל מסלול תן:
- שם
- תיאור קצר ברור ונעים
- למה כדאי ללכת אליו

ענה בפורמט JSON:
[
  {{
    "title": "",
    "summary": "",
    "why": "",
    "link": ""
  }}
]
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return json.loads(response.choices[0].message.content)
