import streamlit as st
from agent import run_agent

st.set_page_config(layout="centered")

# 🎯 RTL יציב + שדה חיפוש "ריבועי"
st.markdown("""
<style>

/* RTL בסיסי */
.block-container {
    direction: rtl;
    text-align: right;
}

/* קונטיינר של השדה */
.stTextInput {
    max-width: 700px;
    margin: auto;
}

/* השדה עצמו */
.stTextInput input {
    direction: rtl !important;
    text-align: right !important;

    height: 80px !important;
    padding: 18px !important;
    font-size: 28px !important;

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

/* פוקוס */
.stTextInput input:focus {
    border: 1px solid #4c8bf5 !important;
    outline: none !important;
}

/* כפתור */
.stButton {
    max-width: 700px;
    margin: 10px auto;
}

.stButton button {
    width: 100%;
    height: 50px;
    font-size: 16px;
    border-radius: 12px;
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
