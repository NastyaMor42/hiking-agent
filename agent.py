from openai import OpenAI
import streamlit as st
from search import search_hikes
import json

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def run_agent(query):
    results = search_hikes(query)

    if not results:
        return []

    prompt = f"""
יש לך תוצאות חיפוש של טיולים:

{results}

בחר 2 מסלולים הכי רלוונטיים.

לכל אחד תן:
- שם
- תיאור קצר ברור
- למה כדאי

ענה JSON בלבד:
[
  {{
    "title": "",
    "summary": "",
    "why": "",
    "link": ""
  }}
]
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        content = response.choices[0].message.content

        return json.loads(content)

    except Exception as e:
        print("ERROR:", e)
        return []
