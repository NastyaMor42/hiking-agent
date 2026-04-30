from openai import OpenAI
import streamlit as st
from search import search_hikes
import json

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def run_agent(query):

    results = search_hikes(query + " מסלול טיול אתר מסלול נחל ישראל")

    if not results:
        return []

prompt = f"""
יש לך תוצאות חיפוש של טיולים בישראל:

{results}

⚠️ חשוב מאוד:
- אל תבחר כתבות כלליות (כמו "5 טיולים..." או "רשימת מסלולים")
- בחר רק מסלול ספציפי אחד (למשל: נחל כזיב, עין גדי, הר תבור)
- אם אין מסלול ברור — אל תשתמש בתוצאה

בחר עד 3 מסלולים אמיתיים בלבד.

לכל מסלול החזר:
- title (שם מסלול אמיתי בלבד)
- area (צפון / מרכז / דרום)
- duration (משך זמן)
- difficulty (קל / בינוני / קשה)
- description (תיאור קצר)
- link (קישור)

⚠️ אם אתה לא בטוח — תשאיר שדה ריק ""

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
