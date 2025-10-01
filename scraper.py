#Scraping functions
import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

def scrape_quotes(limit=5):
    url = "https://quotes.toscrape.com/"
    response = requests.get(url)
    if response.status_code != 200:
        logging.error("Failed to fetch website")
        return []
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = [q.text for q in soup.find_all("span", class_="text")]
    return quotes[:limit]

def quotes_to_df(quotes):
    df = pd.DataFrame(quotes, columns=["Quote"])
    return df
