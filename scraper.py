#Scraping functions
import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

def scrape_quotes(limit=5):
    url = "https://quotes.toscrape.com/"
    response = requests.get(url) #fetch webpage
    if response.status_code != 200:
        logging.error("Failed to fetch website")
        return []
    soup = BeautifulSoup(response.text, "html.parser") # parse HTML
    quotes = [q.text for q in soup.find_all("span", class_="text")] # find all quotes
    return quotes[:limit] # return only first few

def quotes_to_df(quotes):
    df = pd.DataFrame(quotes, columns=["Quote"])
    return df
