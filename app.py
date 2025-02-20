import streamlit as st
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["generative_ai_papers"]
papers_collection = db["papers"]

st.title("📢 Generative AI Daily Papers")

# Fetch papers
papers = list(papers_collection.find().sort("_id", -1))

if papers:
    st.write(f"Showing {len(papers)} latest papers")
    for paper in papers:
        st.subheader(paper["title"])
        st.write(paper["summary"])
        st.write(f"[Read more]({paper['link']})")
        st.write("---")
else:
    st.write("No papers found.")
