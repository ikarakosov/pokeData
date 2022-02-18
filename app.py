from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "this is main page"


@app.route('/about')
def about():
    return "Some info about your mom"

if __name__ == "__main__":
    app.run(debug=True)