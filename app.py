from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Olá, Mundo!"

@app.route('/new', methods = ['GET', 'POST'])
def new():
    return 'Cadastre algo'


if __name__ == '__main__':
    app.run(debug=True)