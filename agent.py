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
יש לך תוצאות חיפוש של טיולים בישראל:

{results}

המטרה:
להחזיר מידע מסודר וברור על מסלולים.

בחר 3 מסלולים הכי רלוונטיים.

לכל מסלול החזר:
- title (שם המסלול)
- area (צפון / מרכז / דרום)
- duration (משך זמן משוער)
- difficulty (קל / בינוני / קשה)
- description (תיאור קצר ונעים)
- link (קישור אמיתי מתוך התוצאות)

⚠️ חשוב:
- אל תמציא מידע שלא קיים
- אם לא בטוח – תשאיר ריק ""

ענה רק JSON בפורמט הזה:

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

        # ניסיון לפרסר JSON
        return json.loads(content)

    except Exception as e:
        print("Agent error:", e)

        # fallback בסיסי
        fallback = []
        for r in results[:3]:
            fallback.append({
                "title": r.get("title", ""),
                "area": "",
                "duration": "",
                "difficulty": "",
                "description": r.get("snippet", ""),
                "link": r.get("link", "")
            })

        return fallback
