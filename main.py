from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello</h1>"


@app.route("/about/")
def about_us():
    return "<h1>Про нас</h1>"


@app.route("/services/")
def services():
    return "<h1>Тут інформація про наші послуги</h1>"


@app.route("/contact/")
def contact():
    return "<h1>На цій сторінці ви можете зв'язатись з нами</h1>"



if __name__ == '__main__':
    app.run(debug=True)
