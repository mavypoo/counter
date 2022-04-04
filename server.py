from flask import Flask, render_template, session, redirect

app = Flask(__name__)

app.secret_key="maverick."

@app.route('/')
def index():
    if "num" not in session:
        session["num"] = 0
    else: 
        session["num"] += 1
    return render_template("index.html")

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)