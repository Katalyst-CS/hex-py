from flask import Flask
from infrastructure.http.controllers import routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(routes)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)