from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Cloud Computing Lab, experiment 5, CI/CD Integration, This is 1st update to file 1, hehuehuee"

@app.route("/student")
def student():
    return {
        "name": "Student",
        "course": "Cloud Computing and DevOps"
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)