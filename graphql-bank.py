from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
import strawberry
from typing import List, Optional

# Domain Models
@strawberry.type
class Address:
    street: str
    city: str
    postal_code: str
    country: str

@strawberry.type
class Account:
    id: int
    type: str
    balance: float

@strawberry.type
class Customer:
    id: int
    name: str
    address: Address
    accounts: List[Account]

# Sample data
address1 = Address(street="123 Main St", city="New York", postal_code="10001", country="USA")
address2 = Address(street="456 Maple Ave", city="San Francisco", postal_code="94105", country="USA")

accounts1 = [Account(id=1, type="Checking", balance=1500.0), Account(id=2, type="Savings", balance=3000.0)]
accounts2 = [Account(id=3, type="Checking", balance=700.0)]

customers = [
    Customer(id=1, name="Alice Johnson", address=address1, accounts=accounts1),
    Customer(id=2, name="Bob Smith", address=address2, accounts=accounts2),
]

# GraphQL Query type
@strawberry.type
class Query:
    @strawberry.field
    def all_customers(self) -> List[Customer]:
        return customers

    @strawberry.field
    def customer_by_id(self, id: int) -> Optional[Customer]:
        return next((c for c in customers if c.id == id), None)

schema = strawberry.Schema(query=Query)

app = FastAPI()
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")
