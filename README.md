# 🚀 FastAPI Social Backend

A production-ready **FastAPI backend** that implements authentication, CRUD posts, a voting system, testing, and deployment pipelines.  
This project was built to learn **FastAPI, PostgreSQL, SQLAlchemy, Alembic, Docker, and CI/CD pipelines**.

---

## 📌 Features

- **User Authentication**
  - Register new users
  - Login with JWT authentication
  - Password hashing with Passlib

- **Posts CRUD**
  - Create, read, update, delete posts
  - Retrieve posts with filters, search, and pagination
  - Ownership validation (only owners can edit/delete)

- **Voting System**
  - Like/Unlike posts
  - Aggregate votes per post

- **Database**
  - PostgreSQL with SQLAlchemy ORM
  - Alembic for schema migrations

- **Testing**
  - Extensive **Pytest** coverage
  - Fixtures, parametrized tests, and database test setup

- **Deployment**
  - Docker & Docker Compose
  - Heroku deployment
  - Ubuntu + Gunicorn + Nginx + SSL
  - GitHub Actions CI/CD pipeline

---

## 🛠️ Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) - High performance Python web framework
- [PostgreSQL](https://www.postgresql.org/) - Relational database
- [SQLAlchemy](https://www.sqlalchemy.org/) - ORM for database interaction
- [Alembic](https://alembic.sqlalchemy.org/) - Database migrations
- [Pytest](https://docs.pytest.org/) - Testing framework
- [Docker](https://www.docker.com/) - Containerization
- [Heroku](https://www.heroku.com/) & [Ubuntu Server](https://ubuntu.com/) - Deployment
- [NGINX](https://www.nginx.com/) + [Gunicorn](https://gunicorn.org/) - Production server setup

---