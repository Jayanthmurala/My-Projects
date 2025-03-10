from flask import Flask
from flask_cors import CORS
from database import engine, Base
from routes.users import users_bp
from routes.news import news_bp

app = Flask(__name__)
CORS(app)

app.config["SECRET_KEY"] = "jayanthmurala"  # Ensure this matches across files

Base.metadata.create_all(bind=engine)
app.register_blueprint(users_bp)
app.register_blueprint(news_bp)

@app.route("/")
def read_root():
    return {"message": "Welcome to AI News Summarizer"}

if __name__ == "__main__":
    app.run(debug=True)