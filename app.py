import streamlit as st
from agent import run_agent

st.set_page_config(layout="centered")

# RTL יציב (עדין אבל עובד)
st.markdown("""
<style>
.block-container {
    direction: rtl;
    text-align: right;
}

/* גם התוצאות */
.stMarkdown, .stText {
    direction: rtl !important;
    text-align: right !important;
}

/* שדה חיפוש */
.stTextInput input {
    direction: rtl !important;
    text-align: right !important;
    font-size: 18px !important;
    padding: 12px !important;
}

/* placeholder */
.stTextInput input::placeholder {
    direction: rtl;
    text-align: right;
    color: #888;
    font-style: italic;
}

/* כפתור */
.stButton button {
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# כותרת
st.title("חיפוש טיולים בישראל 🥾")

# שדה חיפוש
query = st.text_input(
    "",
    placeholder="לדוגמה: טיול קל בצפון עם מים 🌿"
)

search_clicked = st.button("חפש 🔍")

# 🛑 חשוב — לא נוגעים ב-results עד שהוא קיים
if search_clicked:

    if not query:
        st.warning("תכתבי משהו לחיפוש 🙂")
    else:
        results = run_agent(query)

        st.divider()
        st.subheader("מסלולים מומלצים ✨")

        if not results:
            st.warning("לא נמצאו תוצאות 😅")
        else:
            for r in results:
                st.markdown(f"### {r.get('title', 'מסלול ללא שם')} 🥾")

                st.markdown(f"📍 אזור: {r.get('area', 'לא ידוע')}")
                st.markdown(f"⏱️ משך: {r.get('duration', 'לא ידוע')}")
                st.markdown(f"🥵 קושי: {r.get('difficulty', 'לא ידוע')}")

                st.write(r.get("description", ""))

                if r.get("link"):
                    st.markdown(f"[🔗 מעבר למסלול]({r['link']})")

                st.divider()
