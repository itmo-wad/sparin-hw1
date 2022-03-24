from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route('/', defaults={'full_name': 'Medveditskov Yuriy Sergeevich'})
@app.route('/<string:full_name>')
def index(full_name):
    return render_template("index.html", title="Poo CV", full_name=full_name)

@app.route("/profile")
def profile():
    return redirect("/")

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)