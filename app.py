from flask import Flask, render_template, Response, request, redirect, url_for

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/login/", methods=['POST'])
def get_nome():
    nomeLogin = request.form.get('textarea')
    return render_template("home.html", nome = nomeLogin)

if __name__ == "__main__":
	app.run(debug=True)