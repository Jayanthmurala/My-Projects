import React, { useState, useEffect } from 'react';
import { Container, Row, Col, Form, Spinner } from 'react-bootstrap';
import ArticleCard from '../components/ArticleCard';
import { fetchNews, fetchCategories } from '../services/api';

function Home({ token, userId }) {
  const [articles, setArticles] = useState([]);
  const [categories, setCategories] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState('technology');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    const loadCategories = async () => {
      try {
        const data = await fetchCategories();
        setCategories(data);
      } catch (err) {
        setError('Failed to load categories');
      }
    };
    loadCategories();
  }, []);

  useEffect(() => {
    const loadNews = async () => {
      setLoading(true);
      try {
        const data = await fetchNews(selectedCategory);
        setArticles(data);
        setError('');
      } catch (err) {
        setError('Failed to load news');
      } finally {
        setLoading(false);
      }
    };
    loadNews();
  }, [selectedCategory]);

  return (
    <Container className="py-4">
      <Form.Group className="mb-4">
        <Form.Label className="fw-semibold">Category</Form.Label>
        <Form.Select
          value={selectedCategory}
          onChange={(e) => setSelectedCategory(e.target.value)}
          style={{ maxWidth: '200px' }}
        >
          {categories.map((cat) => (
            <option key={cat.category_id} value={cat.name}>
              {cat.name}
            </option>
          ))}
        </Form.Select>
      </Form.Group>
      {loading && (
        <div className="text-center">
          <Spinner animation="border" variant="primary" />
        </div>
      )}
      {error && <p className="text-danger text-center">{error}</p>}
      <Row xs={1} md={2} lg={3} className="g-4">
        {articles.map((article) => (
          <Col key={article.article_id}>
            <ArticleCard article={article} token={token} userId={userId} />
          </Col>
        ))}
      </Row>
    </Container>
  );
}

export default Home;