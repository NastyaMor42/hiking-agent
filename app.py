import streamlit as st
from search import search_hikes

st.set_page_config(layout="centered")

# 🎨 RTL + עיצוב
st.markdown("""
<style>

/* RTL חזק */
html, body, [data-testid="stAppViewContainer"], .block-container {
    direction: rtl !important;
    text-align: right !important;
}

/* כותרת */
h1 {
    text-align: center;
    margin-bottom: 30px;
}

/* שדה חיפוש גדול */
.stTextInput input {
    text-align: right !important;
    font-size: 18px !important;
    padding: 16px !important;
    height: 60px !important;
    border-radius: 12px !important;
}

/* placeholder (טקסט עזרה בתוך השדה) */
.stTextInput input::placeholder {
    color: #aaa !important;
    font-style: italic !important;
    opacity: 1 !important;
}

/* כפתור */
.stButton button {
    width: 100%;
    border-radius: 12px;
    padding: 12px;
    font-size: 16px;
    font-weight: bold;
}

/* כרטיסים */
.card {
    background-color: #1c1f26;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 25px;
    text-align: right;
}

/* divider */
.divider {
    height: 1px;
    background: #2c2f36;
    margin: 25px 0;
}

</style>
""", unsafe_allow_html=True)

# 🏷️ כותרת
st.markdown("<h1>חיפוש טיולים בישראל 🥾</h1>", unsafe_allow_html=True)

# 🔍 שדה חיפוש עם placeholder אמיתי
query = st.text_input(
    label="",
    placeholder="לדוגמה: טיול קל בצפון עם מים 🌿",
)

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
