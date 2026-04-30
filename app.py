import streamlit as st
from agent import run_agent

st.set_page_config(layout="centered")

# 🎯 RTL יציב + שדה חיפוש "ריבועי"
st.markdown("""
<style>

/* קונטיינר */
.stTextInput {
    max-width: 700px;
    margin: auto;
}

/* השדה עצמו - מתוקן */
.stTextInput input {
    direction: rtl !important;
    text-align: right !important;

    height: 60px !important;              /* הורדנו קצת */
    padding: 0 16px !important;           /* רק צדדים */
    font-size: 18px !important;
    line-height: 60px !important;         /* 👈 זה מה שמתקן */

    border-radius: 14px !important;
    border: 1px solid #333 !important;
    background-color: #1c1f26 !important;
    color: white !important;
}

/* placeholder */
.stTextInput input::placeholder {
    color: #888 !important;
    font-style: italic;
}

</style>
""", unsafe_allow_html=True)

# כותרת
st.title("חיפוש טיולים בישראל 🥾")

# 🔍 שדה חיפוש
query = st.text_input(
    "",
    placeholder="לדוגמה: טיול קל בצפון עם מים 🌿"
)

search_clicked = st.button("חפש 🔍")

# תוצאות
if search_clicked and query:

    results = run_agent(query)

    st.divider()
    st.subheader("מסלולים מומלצים ✨")

    if not results:
        st.warning("לא נמצאו תוצאות 😅")

    for r in results:
        st.markdown(f"### {r['title']} 🥾")
        st.write(r["summary"])
        st.write(f"💡 {r['why']}")
        st.markdown(f"[מעבר למסלול 🔗]({r['link']})")
        st.divider()
