from flask import Flask, render_template
from game_of_life import GameOfLife

app = Flask(__name__)


@app.route("/")
def index():
    GameOfLife(width=25, height=15)
    return render_template("index.html")

@app.route("/live")
def live():
    g = GameOfLife()
    if g.counter > 0:
        g.form_new_generation()
    g.counter += 1
    return render_template("live.html", game=g, counter=g.counter)


if __name__ == "__main__":
    app.run(debug=True)