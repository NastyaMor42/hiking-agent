import requests
import streamlit as st

def search_hikes(query):
    url = "https://serpapi.com/search.json"

    params = {
        "q": query,
        "hl": "he",
        "gl": "il",
        "api_key": st.secrets["SERPAPI_KEY"]
    }

    response = requests.get(url, params=params)
    data = response.json()

    results = []

    for r in data.get("organic_results", [])[:5]:
        results.append({
            "title": r.get("title"),
            "snippet": r.get("snippet"),
            "link": r.get("link")
        })

    return results
