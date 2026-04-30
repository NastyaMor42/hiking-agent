import streamlit as st
from agent import run_agent

st.set_page_config(layout="centered")

# RTL עדין (בלי לשבור קומפוננטים)
st.markdown("""
<style>
html, body {
    direction: rtl;
}

.block-container {
    direction: rtl;
    text-align: right;
}
</style>
""", unsafe_allow_html=True)

# כותרת
st.title("חיפוש טיולים בישראל 🥾")

# 🔍 שורת חיפוש נקייה (בלי CSS שבור)
col1, col2 = st.columns([4,1])

with col1:
    query = st.text_input(
        "",
        placeholder="לדוגמה: טיול קל בצפון עם מים 🌿"
    )

with col2:
    search_clicked = st.button("חפש 🔍")

# תוצאות
if search_clicked and query:

    results = run_agent(query)

    st.divider()
    st.subheader("מסלולים מומלצים ✨")

    for r in results:
        st.markdown("### " + r["title"] + " 🥾")
        st.write(r["summary"])
        st.write("💡 " + r["why"])
        st.markdown(f"[מעבר למסלול 🔗]({r['link']})")
        st.divider()
