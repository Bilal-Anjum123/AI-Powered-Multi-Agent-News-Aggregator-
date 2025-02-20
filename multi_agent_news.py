import requests
from bs4 import BeautifulSoup

def fetch_latest_arxiv_papers():
    url = "https://arxiv.org/list/cs.AI/recent"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    papers = []
    for paper in soup.find_all("div", class_="list-title"):
        title = paper.text.replace("Title: ", "").strip()
        link = "https://arxiv.org" + paper.find_previous("a")["href"]
        papers.append({"title": title, "link": link})

    return papers

# Test the scraper
if __name__ == "__main__":
    papers = fetch_latest_arxiv_papers()
    print(papers[:5])  # Show first 5 papers
