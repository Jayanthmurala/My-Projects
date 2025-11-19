# AI News Summarizer

## Project Overview
The **AI News Summarizer** is a full-stack web application that fetches real-time news articles, generates AI-powered summaries, and allows users to save their favorite articles. It combines a **Flask backend**, **MySQL database**, and a **React frontend** styled with Bootstrap.

## Purpose
- Fetch news from **NewsAPI**
- Summarize using **facebook/bart-large-cnn**
- User authentication & article saving
- Responsive UI

## Key Features
- AI-generated summaries
- Category filtering
- JWT authentication
- Save & view saved articles

## Architecture
### Backend
- Flask, SQLAlchemy, MySQL
- Hugging Face Transformers
- JWT authentication

### Frontend
- React + Vite
- Bootstrap 5
- Axios

## Data Flow
1. Frontend → Backend → NewsAPI → AI Summary → MySQL → Frontend  
2. Authentication via JWT  
3. Saved articles fetched via token validation  

## Setup Instructions

### Backend Setup
```
news_summarizer_backend/
├── database.py
├── models.py
├── services/
│   ├── news.py
│   ├── summarizer.py
├── routes/
│   ├── users.py
│   ├── news.py
├── app.py
├── requirements.txt
```

Install:
```
pip install -r requirements.txt
```

Create MySQL DB:
```
CREATE DATABASE news_summarizer;
```

Run backend:
```
python app.py
```

### Frontend Setup
```
news-summarizer-frontend/
├── src/
├── public/
├── package.json
├── vite.config.js
```

Install:
```
npm install
```

Run frontend:
```
npm run dev
```

## API Endpoints
### Users
- POST `/users/register`
- POST `/users/login`

### News
- GET `/news?category=technology`
- GET `/news/categories`
- POST `/news/articles/save`
- GET `/news/articles/saved`

## Database Schema
Includes tables: users, articles, summaries, categories, saved_articles.

## Troubleshooting
- Check `.env` and DB configs  
- Ensure CORS enabled  
- Verify API keys  

## Future Enhancements
- Dark mode
- Article search
- Delete saved articles
- Deployment (Heroku/Vercel)

## Conclusion
A complete AI-powered news summarization application with backend, frontend, and database integration.
