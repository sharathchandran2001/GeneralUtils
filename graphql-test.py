from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
import strawberry
from typing import List, Optional

# Mocked data types
@strawberry.type
class User:
    id: int
    name: str

@strawberry.type
class Book:
    id: int
    title: str
    author: str
    owner: User

# Sample users
user1 = User(id=1, name="Alice")
user2 = User(id=2, name="Bob")

# Sample books
books = [
    Book(id=1, title="1984", author="George Orwell", owner=user1),
    Book(id=2, title="To Kill a Mockingbird", author="Harper Lee", owner=user2),
]

# Query definition
@strawberry.type
class Query:
    @strawberry.field
    def get_books(self) -> List[Book]:
        return books

    @strawberry.field
    def get_book_by_id(self, id: int) -> Optional[Book]:
        return next((book for book in books if book.id == id), None)

    @strawberry.field
    def get_users(self) -> List[User]:
        return [user1, user2]

    @strawberry.field
    def get_user_by_id(self, id: int) -> Optional[User]:
        return user1 if user1.id == id else user2 if user2.id == id else None

schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
