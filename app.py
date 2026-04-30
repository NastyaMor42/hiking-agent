import streamlit as st
from search import search_hikes

# חשוב: זה חייב להיות ראשון
st.set_page_config(layout="centered")

# 🔥 RTL FIX חזק (כולל override מלא)
st.markdown("""
<style>
/* כל האפליקציה */
html, body, [data-testid="stAppViewContainer"] {
    direction: rtl;
    text-align: right;
}

/* כל האלמנטים */
* {
    direction: rtl !important;
    text-align: right !important;
}

/* input */
input, textarea {
    text-align: right !important;
}

/* label */
label {
    width: 100%;
    text-align: right !important;
}

/* selectbox */
div[data-baseweb="select"] {
    direction: rtl !important;
}

/* כפתורים */
button {
    float: right;
}

/* בלוק מרכזי */
.block-container {
    direction: rtl;
    text-align: right;
}
</style>
""", unsafe_allow_html=True)

st.title("🥾 חיפוש טיולים בישראל")

query = st.text_input("מה לחפש?", "טיול קל בצפון ישראל")

if st.button("🔍 חפש"):
    results = search_hikes(query)

    if not results:
        st.error("לא נמצאו תוצאות 😅")

    for r in results:
        st.markdown("---")
        st.subheader(r["title"])
        st.write(r["snippet"])
        st.markdown(f"[🔗 מעבר למסלול]({r['link']})")
