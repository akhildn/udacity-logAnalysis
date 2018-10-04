from flask import Flask, render_template
from newsdb import popular_articles, popular_authors, get_error_rates

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/popular_articles")
def p_articles():
    slugs = popular_articles()
    return render_template("popular_articles.html", slugs=slugs)


@app.route("/popular_authors")
def p_authors():
    authors = popular_authors()
    return render_template("popular_authors.html", authors=authors)


@app.route("/display_error_rate")
def w_errors():
    errors = get_error_rates()
    return render_template("errors.html", errors=errors)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
