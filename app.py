# Flask Dashboard setup
from flask import Flask, render_template
from scraper import scrape_quotes, quotes_to_df

app = Flask(__name__)

@app.route("/")
def dashboard():
    quotes = scrape_quotes(limit=10)
    df = quotes_to_df(quotes)
    return render_template("dashboard.html", tables=[df.to_html(classes='data')], titles=df.columns.values)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5100, debug=True)