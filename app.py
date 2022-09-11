from flask import Flask, render_template
from game_of_life import GameOfLife

app = Flask(__name__)


@app.route("/")
def index():
    GameOfLife(width=25, height=25)
    return render_template("index.html")

@app.route("/live")
def live():
    g = GameOfLife()
    g.form_new_generation()
    return render_template("live.html", game=g)


if __name__ == "__main__":
    app.run(debug=True)