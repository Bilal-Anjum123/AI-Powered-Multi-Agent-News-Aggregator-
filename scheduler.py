from apscheduler.schedulers.background import BackgroundScheduler
import time
from multi_agent_news import fetch_news_from_techcrunch
from summarizer import filter_and_summarize
from database import store_news
# Define job to run daily at 9 AM
scheduler = BackgroundScheduler()

def run_daily_job():
    # Fetch, filter, and summarize the articles
    articles = fetch_news_from_techcrunch()  # You can add other sources too
    articles = filter_and_summarize(articles)
    store_news(articles)
    print("Daily news update completed.")

scheduler.add_job(run_daily_job, 'cron', hour=9, minute=0)
scheduler.start()

# Keep the scheduler running
while True:
    time.sleep(1)
