from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for the voting system
votes = {
    "Project Alpha": 0,
    "Project Beta": 0,
    "Project Gamma": 0
}

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", votes=votes, total=sum(votes.values()))

@app.route("/vote", methods=["POST"])
def vote():
    choice = request.form.get("choice")
    if choice in votes:
        votes[choice] += 1
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run()
