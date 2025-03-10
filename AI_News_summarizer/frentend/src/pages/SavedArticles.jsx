import React, { useState, useEffect } from 'react';
import { Container, Row, Col, Spinner } from 'react-bootstrap';
import ArticleCard from '../components/ArticleCard';
import { getSavedArticles } from '../services/api';

function SavedArticles({ token, userId }) {
  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    const loadSavedArticles = async () => {
      if (!token) {
        setError('Please log in to view saved articles.');
        return;
      }
      setLoading(true);
      try {
        const data = await getSavedArticles(token);
        setArticles(data);
        setError('');
      } catch (err) {
        setError(err.response?.data?.error || 'Failed to load saved articles');
      } finally {
        setLoading(false);
      }
    };
    loadSavedArticles();
  }, [token]);

  return (
    <Container className="py-4">
      <h2 className="mb-4 fw-bold">Saved Articles</h2>
      {loading && (
        <div className="text-center">
          <Spinner animation="border" variant="primary" />
        </div>
      )}
      {error && <p className="text-danger text-center">{error}</p>}
      {!loading && !error && articles.length === 0 && (
        <p className="text-center text-muted">No saved articles yet.</p>
      )}
      <Row xs={1} md={2} lg={3} className="g-4">
        {articles.map((article) => (
          <Col key={article.article_id}>
            <ArticleCard article={article} token={token} userId={userId} isSaved={true} />
          </Col>
        ))}
      </Row>
    </Container>
  );
}

export default SavedArticles;