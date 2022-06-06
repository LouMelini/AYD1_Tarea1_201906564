from flask_cors import CORS
from flask import Flask, request


app = Flask(__name__)
CORS(app)


@app.route('/info', methods=['GET'])
def main():
    return "Lourdes Rosario Velásquez Melini - 201906564"


if __name__ == '__main__':
    app.run(
        port=4000
    )
