from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    password_hash = Column(String(64))
    created_at = Column(DateTime, default=datetime.utcnow)
    last_login = Column(DateTime)

    preferences = relationship("UserPreference", back_populates="user")
    saved_articles = relationship("SavedArticle", back_populates="user")

class Article(Base):
    __tablename__ = "articles"
    article_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(String(255), index=True)
    source = Column(String(100))
    url = Column(String(255), unique=True)
    published_at = Column(DateTime)
    fetched_at = Column(DateTime, default=datetime.utcnow)
    content = Column(Text)

    summary = relationship("Summary", uselist=False, back_populates="article")
    categories = relationship("Category", secondary="article_categories")

class Summary(Base):
    __tablename__ = "summaries"
    summary_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    article_id = Column(Integer, ForeignKey("articles.article_id"), unique=True)
    summary_text = Column(Text)
    generated_at = Column(DateTime, default=datetime.utcnow)
    sentiment = Column(String(20), nullable=True)

    article = relationship("Article", back_populates="summary")

class Category(Base):
    __tablename__ = "categories"
    category_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(50), unique=True)
    description = Column(String(255), nullable=True)

class ArticleCategory(Base):
    __tablename__ = "article_categories"
    article_id = Column(Integer, ForeignKey("articles.article_id"), primary_key=True)
    category_id = Column(Integer, ForeignKey("categories.category_id"), primary_key=True)

class UserPreference(Base):
    __tablename__ = "user_preferences"
    user_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True)
    category_id = Column(Integer, ForeignKey("categories.category_id"), primary_key=True)
    preference_level = Column(Integer, default=1)

    user = relationship("User", back_populates="preferences")

class SavedArticle(Base):
    __tablename__ = "saved_articles"
    save_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    article_id = Column(Integer, ForeignKey("articles.article_id"))
    saved_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="saved_articles")