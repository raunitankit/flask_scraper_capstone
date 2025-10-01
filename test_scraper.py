from scraper import scrape_quotes, quotes_to_df

def test_scrape_quotes():
    quotes = scrape_quotes(limit=3)
    assert len(quotes) == 3

def test_quotes_to_df():
    df = quotes_to_df(["Hello", "World"])
    assert df.shape[0] == 2
    assert "Quote" in df.columns