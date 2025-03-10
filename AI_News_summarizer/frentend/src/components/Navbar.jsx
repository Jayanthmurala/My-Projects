import React from 'react';
import { Navbar as BSNavbar, Nav, Button } from 'react-bootstrap';
import { Link } from 'react-router-dom';

function Navbar({ token, onLogout, onLoginClick, onRegisterClick }) {
  return (
    <BSNavbar bg="dark" variant="dark" expand="lg" sticky="top">
      <div className="container">
        <BSNavbar.Brand as={Link} to="/" className="fw-bold">
          AI News Summarizer
        </BSNavbar.Brand>
        <BSNavbar.Toggle aria-controls="basic-navbar-nav" />
        <BSNavbar.Collapse id="basic-navbar-nav">
          <Nav className="ms-auto">
            <Nav.Link as={Link} to="/" className="text-white">
              Home
            </Nav.Link>
            {token && (
              <Nav.Link as={Link} to="/saved" className="text-white">
                Saved Articles
              </Nav.Link>
            )}
            {token ? (
              <Button variant="outline-light" className="btn-custom ms-2" onClick={onLogout}>
                Logout
              </Button>
            ) : (
              <>
                <Button variant="primary" className="btn-custom ms-2" onClick={onLoginClick}>
                  Login
                </Button>
                <Button variant="outline-primary" className="btn-custom ms-2" onClick={onRegisterClick}>
                  Register
                </Button>
              </>
            )}
          </Nav>
        </BSNavbar.Collapse>
      </div>
    </BSNavbar>
  );
}

export default Navbar;