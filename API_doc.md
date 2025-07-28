# Inventory Management System – API Documentation

**Base URL**: `http://localhost:8000`

---

## Authentication

### POST `/auth/register`
Registers a new user and returns a JWT token.

**Request Body (JSON):**
```json
{
  "username": "admin",
  "password": "securepassword"
}
```

**Response:**
```json
{
  "access_token": "JWT_TOKEN",
  "token_type": "bearer"
}
```

---

### POST `/auth/login`
Authenticates a user and returns a JWT token.

**Content-Type**: `application/x-www-form-urlencoded`

**Request Body:**
- `username`: string
- `password`: string

**Response:**
```json
{
  "access_token": "JWT_TOKEN",
  "token_type": "bearer"
}
```

---

**Authorization Header (Required for all routes below):**
```
Authorization: Bearer <JWT_TOKEN>
```

---

## Products

### POST `/products`
Adds a new product.

**Request Body (JSON):**
```json
{
  "name": "Mouse",
  "description": "Wireless mouse",
  "price": 599.99,
  "quantity": 100
}
```

**Response:**
```json
{
  "id": 1,
  "name": "Mouse",
  "description": "Wireless mouse",
  "price": 599.99,
  "quantity": 100
}
```

---

### GET `/products`
Retrieves a paginated list of products.

**Query Parameters:**
- `skip`: integer (default: 0)
- `limit`: integer (default: 10)

**Response:**
```json
[
  {
    "id": 1,
    "name": "Mouse",
    "description": "Wireless mouse",
    "price": 599.99,
    "quantity": 100
  }
]
```

---

### PUT `/products/{product_id}`
Updates the details of a specific product.

**Request Body (JSON):**
```json
{
  "name": "Updated Name",
  "description": "Updated description",
  "price": 649.99,
  "quantity": 120
}
```

**Response:**
```json
{
  "id": 1,
  "name": "Updated Name",
  "description": "Updated description",
  "price": 649.99,
  "quantity": 120
}
```

---

### PATCH `/products/{product_id}/quantity`
Updates the quantity of a specific product.

**Request Body (JSON):**
```json
{
  "quantity": 50
}
```

**Response:**
```json
{
  "id": 1,
  "name": "Mouse",
  "quantity": 50
}
```

---

### DELETE `/products/{product_id}`
Deletes a product.

**Response:**
```json
{
  "detail": "Product deleted"
}
```

---

## Analytics

### GET `/analytics/most-added-products`
Returns a sorted list of products based on total quantity added (descending).

**Response:**
```json
[
  {
    "product_id": 1,
    "name": "Mouse",
    "total_quantity_added": 200
  },
  {
    "product_id": 2,
    "name": "Keyboard",
    "total_quantity_added": 150
  }
]
```
