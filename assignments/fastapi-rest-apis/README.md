# 🚀 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a RESTful API with FastAPI using Pydantic models, HTTP endpoints, and query parameters.

## 📝 Tasks

### 🛠️ Create the FastAPI Application

#### Description
Set up a FastAPI app and define a simple GET endpoint to return a list of items.

#### Requirements
Completed program should:

- Import `FastAPI` and create an `app = FastAPI()` instance
- Define a GET endpoint at `/items/`
- Return a list of items in JSON format
- Include a clear function docstring for the endpoint

### 🛠️ Add Pydantic Models and a POST Endpoint

#### Description
Create a Pydantic model for item data and add a POST endpoint that accepts new items.

#### Requirements
Completed program should:

- Define an `Item` model using `pydantic.BaseModel`
- Include fields for `name`, `description`, `price`, and `in_stock`
- Add a POST endpoint at `/items/` that accepts an `Item`
- Return the created item with a generated `id`

### 🛠️ Add Query Parameters and Filtering

#### Description
Extend the item listing endpoint so it supports query parameters for pagination and availability.

#### Requirements
Completed program should:

- Accept optional query parameters `limit` and `available` on `/items/`
- Use `limit` to control the number of items returned
- Use `available` to filter items by their `in_stock` status
- Return filtered results in JSON format
