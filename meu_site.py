from flask import Flask, url_for, render_template, request

app = Flask(__name__)
# route -> teste.com/
# função -> o que você quer exibir naquela página
# template

@app.route("/")
def home():
    return 'Esta é a home'

#render_template("home.html")

# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)