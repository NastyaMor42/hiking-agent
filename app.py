import streamlit as st
from search import search_hikes

st.title("🧪 בדיקת חיפוש מסלולים")

query = st.text_input("מה לחפש?", "טיול קל בצפון ישראל")

if st.button("🔍 חפש"):
    results = search_hikes(query)

    for r in results:
        st.subheader(r["title"])
        st.write(r["snippet"])
        st.markdown(f"[🔗 מעבר למסלול]({r['link']})")
