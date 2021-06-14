from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
        return "Welcome To My Drink API"
        
@app.route('/drinks')
def get_drinks():
    return {"name": "Grape", "description": "Delicious grape fruit drink"}

# @app.route('/drinks/<id>')
# def get_drink():


if __name__ == "__main__":
    app.debug = True
    app.run()