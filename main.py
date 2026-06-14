
from flask import Flask, render_template, request
from src.data import fetch_breweries, brewery_generator
from src.utils import sort_breweries, filter_breweries

app = Flask(__name__)


@app.route("/")
def home():

    breweries = fetch_breweries()

    breweries = list(brewery_generator(breweries))

    country = request.args.get("country", "")
    brewery_type = request.args.get("type", "")

    breweries = filter_breweries(
        breweries,
        country,
        brewery_type
    )

    breweries = sort_breweries(breweries)

    return render_template(
        "index.html",
        breweries=breweries,
        selected_country=country,
        selected_type=brewery_type
    )


if __name__ == "__main__":
    app.run(debug=True)