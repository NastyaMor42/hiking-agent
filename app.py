import streamlit as st
from search import search_hikes

st.set_page_config(layout="centered")

# 🎨 RTL + עיצוב מודרני
st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"] {
    direction: rtl;
    text-align: right;
    background-color: #0e1117;
}

/* כותרת */
h1 {
    text-align: center;
    margin-bottom: 30px;
}

/* שדה חיפוש */
.stTextInput input {
    text-align: right !important;
    border-radius: 10px;
    padding: 10px;
}

/* כפתור */
.stButton button {
    width: 100%;
    border-radius: 10px;
    padding: 10px;
    font-size: 16px;
    font-weight: bold;
}

/* כרטיסים */
.card {
    background-color: #1c1f26;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 20px;
    transition: 0.2s;
}

.card:hover {
    transform: scale(1.01);
}

/* קו הפרדה */
.divider {
    height: 1px;
    background: #2c2f36;
    margin: 25px 0;
}
</style>
""", unsafe_allow_html=True)

# 🏷️ כותרת
st.markdown("<h1>חיפוש טיולים בישראל 🥾</h1>", unsafe_allow_html=True)

# 🔍 שדה חיפוש
query = st.text_input("מה בא לך למצוא? 🔎", "טיול קל בצפון ישראל")

# 🔘 כפתור
if st.button("חפש מסלולים 🔍"):
    results = search_hikes(query)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    if not results:
        st.warning("לא נמצאו תוצאות 😅")
    else:
        st.subheader("מסלולים מומלצים ✨")

        for r in results:
            st.markdown('<div class="card">', unsafe_allow_html=True)

            st.markdown(f"### {r['title']} 🥾")
            st.write(r["snippet"])

            st.markdown(f"[מעבר למסלול 🔗]({r['link']})")

            st.markdown('</div>', unsafe_allow_html=True)
