from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


def init_db():
    conn = sqlite3.connect('comfort.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS preferences (
                        id INTEGER PRIMARY KEY,
                        softness INTEGER,
                        breathability INTEGER,
                        stretchiness INTEGER,
                        warmth INTEGER,
                        durability INTEGER,
                        location TEXT,
                        fit_preference TEXT,
                        sustainability INTEGER,
                        fabric_cotton INTEGER,
                        fabric_linen INTEGER,
                        fabric_silk INTEGER,
                        fabric_wool INTEGER,
                        fabric_polyester INTEGER
                    )''')
    conn.commit()
    conn.close()

# Initialize the database
init_db()

#@app.route('/')
#def home():
#   return "Welcome to the Comfort Score App! Go to /survey to fill out your preferences."
@app.route('/')
def home():
    return redirect(url_for('survey'))

@app.route('/survey')
def survey():
    return render_template('survey.html')

@app.route('/sumbit-feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/edit-avatar')
def avatar():
    return render_template('edit_avatar.html')

@app.route('/comfort-score')
def score():
    return render_template('comfort_score.html')

@app.route('/submit-survey', methods=['POST'])
def submit_survey():
    # Retrieve form data
    preferences = {
        "softness": request.form.get("softness"),
        "breathability": request.form.get("breathability"),
        "stretchiness": request.form.get("stretchiness"),
        "warmth": request.form.get("warmth"),
        "durability": request.form.get("durability"),
        "location": request.form.get("location"),
        "fit_preference": request.form.get("fit_preference"),
        "sustainability": request.form.get("sustainability"),
        "fabric_cotton": request.form.get("fabric_cotton"),
        "fabric_linen": request.form.get("fabric_linen"),
        "fabric_silk": request.form.get("fabric_silk"),
        "fabric_wool": request.form.get("fabric_wool"),
        "fabric_polyester": request.form.get("fabric_polyester")
    }
    
    # Save to database
    save_preferences(preferences)
    return redirect(url_for('home'))

def save_preferences(preferences):
    conn = sqlite3.connect('comfort.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO preferences (
                        softness, breathability, stretchiness, warmth, durability,
                        location, fit_preference, sustainability, fabric_cotton,
                        fabric_linen, fabric_silk, fabric_wool, fabric_polyester
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (
        preferences["softness"], preferences["breathability"], preferences["stretchiness"],
        preferences["warmth"], preferences["durability"], preferences["location"],
        preferences["fit_preference"], preferences["sustainability"], preferences["fabric_cotton"],
        preferences["fabric_linen"], preferences["fabric_silk"], preferences["fabric_wool"],
        preferences["fabric_polyester"]
    ))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    app.run(debug=True)
