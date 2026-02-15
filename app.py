from flask import Flask, request, jsonify, render_template
import mysql.connector
import os

app = Flask(
    __name__,
    template_folder=r"C:\Users\deva7\valentine-quiz"  # <-- your index.html location
)

# ----------------- MySQL Connection -----------------
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="dpeovojaa",  # replace with your MySQL password
    database="valentine_quiz"
)
cursor = db.cursor(dictionary=True)

# ----------------- Routes -----------------

@app.route('/')
def index():
    # Flask will look for index.html in template_folder
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    name = data.get('name')
    q1 = data.get('q1')
    q2 = data.get('q2')
    q3 = data.get('q3')
    q4 = data.get('q4')

    cursor.execute(
        "INSERT INTO responses (name, q1, q2, q3, q4) VALUES (%s, %s, %s, %s, %s)",
        (name, q1, q2, q3, q4)
    )
    db.commit()
    return jsonify({"status": "success"})

@app.route('/responses', methods=['GET'])
def responses():
    cursor.execute("SELECT * FROM responses ORDER BY ts DESC")
    rows = cursor.fetchall()
    return jsonify(rows)

# ----------------- Run App -----------------
if __name__ == '__main__':
    app.run(debug=True)
