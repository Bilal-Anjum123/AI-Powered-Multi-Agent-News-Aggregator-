from pymongo import MongoClient
import hashlib
from multi_agent_news import fetch_latest_arxiv_papers
from summarizer import summarize_with_deepseek
client = MongoClient("mongodb://localhost:27017/")
db = client["generative_ai_papers"]
papers_collection = db["papers"]

def is_duplicate(title):
    """Check if the paper title already exists in the database."""
    title_hash = hashlib.md5(title.encode()).hexdigest()
    return papers_collection.find_one({"title_hash": title_hash}) is not None

def store_papers(papers):
    for paper in papers:
        if not is_duplicate(paper["title"]):
            print(f"Inserting: {paper['title']}")

            paper["summary"] = summarize_with_deepseek(paper["title"])
            paper["title_hash"] = hashlib.md5(paper["title"].encode()).hexdigest()

            papers_collection.insert_one(paper)
        else:
            print(f"Skipping duplicate: {paper['title']}")

# Test storage
if __name__ == "__main__":
    papers = fetch_latest_arxiv_papers()
    store_papers(papers)
