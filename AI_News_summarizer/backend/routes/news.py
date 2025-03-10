from flask import Blueprint, request, jsonify, current_app
from sqlalchemy.orm import Session
from database import get_db
from models import Article, Summary, Category, SavedArticle
from services.news import fetch_news
from services.summarizer import summarize_text
from datetime import datetime
import jwt

news_bp = Blueprint("news", __name__, url_prefix="/news")

API_KEY = "76980147d70e4ade9fc0954c7e61b7f9"  # Replace with your NewsAPI key

def verify_token():
    token = request.headers.get("Authorization")
    if not token or not token.startswith("Bearer "):
        return None, jsonify({"error": "Token required"}), 401
    token = token.split(" ")[1]
    try:
        data = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
        return data["user_id"], None, None
    except jwt.ExpiredSignatureError:
        return None, jsonify({"error": "Token expired"}), 401
    except jwt.InvalidTokenError:
        return None, jsonify({"error": "Invalid token"}), 401

@news_bp.route("/", methods=["GET"])
def get_news():
    category = request.args.get("category", "general")
    db = next(get_db())
    articles = fetch_news(API_KEY, category)
    result = []
    for article in articles[:5]:
        db_article = db.query(Article).filter(Article.url == article["url"]).first()
        if not db_article:
            published_at = datetime.strptime(article["publishedAt"], "%Y-%m-%dT%H:%M:%SZ")
            db_article = Article(
                title=article["title"],
                source=article["source"]["name"],
                url=article["url"],
                published_at=published_at,
                content=article["content"] or article["description"]
            )
            db.add(db_article)
            db.commit()
            db.refresh(db_article)

            summary_text = summarize_text(db_article.content or db_article.title)
            db_summary = Summary(article_id=db_article.article_id, summary_text=summary_text)
            db.add(db_summary)
            db.commit()

        result.append({
            "article_id": db_article.article_id,
            "title": db_article.title,
            "source": db_article.source,
            "url": db_article.url,
            "published_at": db_article.published_at.isoformat() if db_article.published_at else None,
            "summary_text": db_article.summary.summary_text if db_article.summary else None
        })
    return jsonify(result), 200

@news_bp.route("/categories", methods=["GET"])
def get_categories():
    db = next(get_db())
    categories = db.query(Category).all()
    return jsonify([{"category_id": c.category_id, "name": c.name} for c in categories]), 200

@news_bp.route("/articles/save", methods=["POST"])
def save_article():
    user_id, error, status = verify_token()
    if error:
        return error, status
    
    data = request.get_json()
    db = next(get_db())
    try:
        saved = SavedArticle(user_id=user_id, article_id=data["article_id"])
        db.add(saved)
        db.commit()
        return jsonify({"message": "Article saved successfully"}), 201
    except Exception as e:
        db.rollback()
        return jsonify({"error": "Failed to save article, check article_id"}), 400

@news_bp.route("/articles/saved", methods=["GET"])
def get_saved_articles():
    user_id, error, status = verify_token()
    if error:
        return error, status
    db = next(get_db())
    saved = db.query(SavedArticle).filter(SavedArticle.user_id == user_id).all()
    articles = db.query(Article).filter(Article.article_id.in_([s.article_id for s in saved])).all()
    result = [{
        "article_id": a.article_id,
        "title": a.title,
        "source": a.source,
        "url": a.url,
        "published_at": a.published_at.isoformat() if a.published_at else None,
        "summary_text": a.summary.summary_text if a.summary else None
    } for a in articles]
    return jsonify(result), 200