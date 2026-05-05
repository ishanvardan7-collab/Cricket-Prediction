from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

def predict_score(player, match_type):
    file_map = {
        "dhoni": "dhoni.csv",
        "kohli": "kohli.csv",
        "rohit": "rohit.csv"
    }

    df = pd.read_csv(file_map[player])
    df = df[df["match_type"] == match_type]

    if len(df) == 0:
        return 0

    return int(df["runs"].mean())


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():
    player = request.form['player']
    match_type = request.form['match_type']

    score = predict_score(player, match_type)

    return render_template("cricket-result.html",
                           player=player.upper(),
                           score=score)


# IMPORTANT FOR DEPLOYMENT
if __name__ == "__main__":
    app.run()
