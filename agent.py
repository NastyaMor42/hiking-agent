from openai import OpenAI
import streamlit as st
from search import search_hikes
import json

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


def run_agent(query):
    results = search_hikes(query + " מסלול טיול ישראל נחל")

    if not results:
        return []

    prompt = f"""
יש לך תוצאות חיפוש של טיולים בישראל:

{results}

⚠️ חשוב מאוד:
- אל תבחר כתבות כלליות (כמו "5 טיולים..." או "רשימות")
- בחר רק מסלול ספציפי (למשל: נחל כזיב, עין גדי)
- אם אין מסלול ברור — אל תשתמש

בחר עד 3 מסלולים אמיתיים בלבד.

לכל מסלול החזר:
- title
- area
- duration
- difficulty
- description
- link

ענה JSON בלבד:

[
  {{
    "title": "",
    "area": "",
    "duration": "",
    "difficulty": "",
    "description": "",
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
        print("Agent error:", e)
        return []
