"""
FastAPI Library Management System - Starter Code
Student: [Your Name Here]
Assignment: Building REST APIs with FastAPI

This starter code provides the basic structure for your library management API.
Complete the TODO sections to implement the required functionality.
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
import uvicorn

# Initialize FastAPI app
app = FastAPI(
    title="Digital Library API",
    description="A REST API for managing books, authors, and reviews",
    version="1.0.0"
)

# Pydantic Models (Data Schemas)

class BookBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    author: str = Field(..., min_length=1, max_length=100)
    genre: str = Field(..., min_length=1, max_length=50)
    publication_year: int = Field(..., ge=1000, le=datetime.now().year)
    isbn: str = Field(..., min_length=10, max_length=17)
    description: Optional[str] = Field(None, max_length=1000)

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    author: Optional[str] = Field(None, min_length=1, max_length=100)
    genre: Optional[str] = Field(None, min_length=1, max_length=50)
    publication_year: Optional[int] = Field(None, ge=1000, le=datetime.now().year)
    isbn: Optional[str] = Field(None, min_length=10, max_length=17)

class Book(BookBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

# TODO: Add Author and Review models here

# In-memory storage (replace with database in Task 3)
books_db = []
next_book_id = 1

# Sample data
sample_books = [
    {
        "id": 1,
        "title": "The Python Programming Language",
        "author": "Guido van Rossum",
        "genre": "Technology",
        "publication_year": 2020,
        "isbn": "978-0123456789",
        "description": "A comprehensive guide to Python programming",
        "created_at": datetime.now()
    },
    {
        "id": 2,
        "title": "FastAPI for Modern Web APIs",
        "author": "Bill Lubanovic",
        "genre": "Technology", 
        "publication_year": 2023,
        "isbn": "978-0987654321",
        "description": "Building fast and scalable web APIs with FastAPI",
        "created_at": datetime.now()
    }
]

# Initialize with sample data
books_db.extend(sample_books)
next_book_id = len(sample_books) + 1

# API Endpoints

@app.get("/")
async def root():
    """Welcome endpoint"""
    return {"message": "Welcome to the Digital Library API"}

@app.get("/books", response_model=List[Book])
async def get_all_books():
    """Get all books in the library"""
    # TODO: Add query parameters for filtering (genre, author, etc.)
    return books_db

@app.get("/books/{book_id}", response_model=Book)
async def get_book(book_id: int):
    """Get a specific book by ID"""
    # TODO: Implement this endpoint
    # Find book by ID and return it
    # Raise HTTPException with 404 if not found
    pass

@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
async def create_book(book: BookCreate):
    """Add a new book to the library"""
    global next_book_id
    
    # TODO: Implement this endpoint
    # Create new book with auto-generated ID and current timestamp
    # Add to books_db and return the created book
    pass

@app.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: int, book_update: BookUpdate):
    """Update an existing book"""
    # TODO: Implement this endpoint
    # Find book by ID, update provided fields, return updated book
    # Raise HTTPException with 404 if not found
    pass

@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    """Delete a book from the library"""
    # TODO: Implement this endpoint
    # Find and remove book by ID
    # Return success message or 404 if not found
    pass

# TODO: Add author endpoints in Task 2
# @app.get("/authors")
# @app.post("/authors") 
# etc.

# TODO: Add review endpoints in Task 2
# @app.get("/books/{book_id}/reviews")
# @app.post("/books/{book_id}/reviews")
# etc.

if __name__ == "__main__":
    # Run the application
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)