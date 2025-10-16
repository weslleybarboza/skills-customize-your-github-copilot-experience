# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

In this assignment, you will learn to build modern REST APIs using the FastAPI framework. You'll create a complete API for managing a digital library system with books, authors, and user reviews. This project will introduce you to web API development, HTTP methods, data validation, and API documentation.

## 📝 Tasks

### 🛠️ Task 1: Set Up FastAPI Project and Basic Endpoints

#### Description
Create a FastAPI application with basic CRUD (Create, Read, Update, Delete) operations for managing books in a digital library.

#### Requirements
Completed program should:

- Install and set up FastAPI with required dependencies (uvicorn, pydantic)
- Create a main.py file with FastAPI application instance
- Implement GET endpoint to retrieve all books
- Implement GET endpoint to retrieve a specific book by ID
- Implement POST endpoint to add a new book
- Include proper Pydantic models for data validation
- Return appropriate HTTP status codes

### 🛠️ Task 2: Advanced API Features

#### Description
Extend your API with additional functionality including authors, reviews, and advanced querying capabilities.

#### Requirements
Completed program should:

- Add Author model and CRUD endpoints for authors
- Add Review model linked to books with rating system
- Implement query parameters for filtering books (by author, genre, rating)
- Add PUT endpoint for updating book information
- Add DELETE endpoint for removing books
- Implement proper error handling with custom HTTP exceptions
- Include API documentation using FastAPI's automatic docs

### 🛠️ Task 3: Data Persistence and Testing

#### Description
Add data persistence using a simple database and create tests for your API endpoints.

#### Requirements
Completed program should:

- Integrate SQLite database using SQLAlchemy or similar ORM
- Create database models and tables
- Implement proper database session management
- Add at least 5 test cases using pytest
- Test both successful operations and error scenarios
- Include sample data seeding functionality
- Document API usage with example requests and responses

## 🚀 Getting Started

1. Create a new Python virtual environment
2. Install required packages: `pip install fastapi uvicorn pydantic sqlalchemy pytest`
3. Start with the provided starter code
4. Run your API server: `uvicorn main:app --reload`
5. Access the interactive API docs at `http://localhost:8000/docs`

## 📚 Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Models Guide](https://pydantic-docs.helpmanual.io/)
- [HTTP Status Codes Reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

## ⏰ Due Date

**Due: October 23, 2025**

Submit your completed assignment by uploading your project folder with all Python files, database files, and a brief README explaining how to run your API.

---

*Good luck and happy coding! 🐍✨*