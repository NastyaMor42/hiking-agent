import streamlit as st
from search import search_hikes

# 🔥 RTL FIX אמיתי
st.set_page_config(layout="centered")

st.markdown("""
<style>
html, body, [class*="css"] {
    direction: rtl !important;
    text-align: right !important;
}

section.main > div {
    direction: rtl;
}

label {
    text-align: right !important;
    display: block;
}

input, textarea {
    text-align: right !important;
}

.stTextInput > div > div > input {
    text-align: right !important;
}

.stSelectbox div[data-baseweb="select"] {
    direction: rtl !important;
}

button {
    direction: rtl !important;
}
</style>
""", unsafe_allow_html=True)

# 📦 עטיפה כללית (עוד חיזוק ל-RTL)
st.markdown("<div dir='rtl'>", unsafe_allow_html=True)

# 🧪 UI בדיקה
st.title("🧪 בדיקת חיפוש מסלולים")

query = st.text_input("מה לחפש?", "טיול קל בצפון ישראל")

if st.button("🔍 חפש"):
    results = search_hikes(query)

    if not results:
        st.error("לא נמצאו תוצאות 😅")

    for r in results:
        st.subheader(r["title"])
        st.write(r["snippet"])
        st.markdown(f"[🔗 מעבר למסלול]({r['link']})")

st.markdown("</div>", unsafe_allow_html=True)
