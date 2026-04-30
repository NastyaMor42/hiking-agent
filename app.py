import streamlit as st
from agent import run_agent

st.set_page_config(layout="centered")

# RTL עדין בלבד (בלי לשבור קומפוננטים)
st.markdown("""
<style>
.block-container {
    direction: rtl;
    text-align: right;
}
</style>
""", unsafe_allow_html=True)

# כותרת
st.title("חיפוש טיולים בישראל 🥾")

# שורת חיפוש נקייה
col1, col2 = st.columns([4,1], vertical_alignment="bottom")

with col1:
    query = st.text_input(
        label="",
        placeholder="לדוגמה: טיול קל בצפון עם מים 🌿",
        label_visibility="collapsed"
    )

with col2:
    search_clicked = st.button("חפש 🔍", use_container_width=True)

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
