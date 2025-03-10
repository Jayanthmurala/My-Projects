import React from 'react';
import { Card, Button } from 'react-bootstrap';
import { saveArticle } from '../services/api';

function ArticleCard({ article, token, userId, isSaved = false }) {
  const handleSave = async () => {
    if (!token) {
      alert('Please log in to save articles.');
      return;
    }
    try {
      await saveArticle(article.article_id, token);
      alert('Article saved successfully!');
    } catch (error) {
      alert('Failed to save: ' + (error.response?.data?.error || 'Unknown error'));
    }
  };

  return (
    <Card className="h-100">
      <Card.Body>
        <Card.Title className="fw-semibold">{article.title}</Card.Title>
        <Card.Subtitle className="mb-2 text-muted">
          {article.source} | {new Date(article.published_at).toLocaleString()}
        </Card.Subtitle>
        <Card.Text>{article.summary_text || 'Summary loading...'}</Card.Text>
        <div className="d-flex justify-content-between align-items-center">
          <Card.Link href={article.url} target="_blank" rel="noopener noreferrer">
            Read More
          </Card.Link>
          {!isSaved && (
            <Button variant="primary" className="btn-custom" onClick={handleSave}>
              Save
            </Button>
          )}
        </div>
      </Card.Body>
    </Card>
  );
}

export default ArticleCard;