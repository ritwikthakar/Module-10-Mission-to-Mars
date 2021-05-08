from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)
mars_db = mongo.db.mars

@app.route("/")
def index():
    scraped_data_from_db = mars_db.find_one()
    return render_template("index.html", mars=scraped_data_from_db)

@app.route("/scrape")
def scrape():
    scraped_data = scraping.scrape_all()
    mars_db.update({}, scraped_data, upsert=True)
    return redirect('/', code=302)

if __name__ == "__main__":
    app.run()