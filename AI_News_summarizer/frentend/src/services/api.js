import axios from 'axios';

const API_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:5000';

const api = axios.create({
  baseURL: API_URL,
});

export const fetchNews = async (category) => {
  const response = await api.get(`/news?category=${category}`);
  return response.data;
};

export const fetchCategories = async () => {
  const response = await api.get('/news/categories');
  return response.data;
};

export const loginUser = async (username, password) => {
  const response = await api.post('/users/login', { username, password });
  return response.data;
};

export const registerUser = async (username, email, password) => {
  const response = await api.post('/users/register', { username, email, password });
  return response.data;
};

export const saveArticle = async (articleId, token) => {
  const response = await api.post(
    '/news/articles/save',
    { article_id: articleId },
    { headers: { Authorization: `Bearer ${token}` } }
  );
  return response.data;
};

export const getSavedArticles = async (token) => {
  const response = await api.get('/news/articles/saved', {
    headers: { Authorization: `Bearer ${token}` }
  });
  return response.data;
};