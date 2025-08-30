# PFT-API (Personal Finance Tracker API)

PFT-API is a robust and secure RESTful backend service for a personal finance tracking application. Built with Django and Django Rest Framework, it provides a streamlined foundation for managing users, categories, and financial transactions. The entire focus is on clean backend logic, a well-structured database, and a secure, easy-to-use API.

This project was built as a capstone project to demonstrate core backend development principles.

## Core Features

*   **JWT User Authentication**: Secure user registration and login using JSON Web Tokens (JWT). Endpoints are protected, ensuring users can only access their own data.
*   **Category Management (CRUD)**: Users can create, view, update, and delete their own custom spending/income categories (e.g., "Groceries", "Salary").
*   **Transaction Management (CRUD)**: Users can log, view, filter, update, and delete their financial transactions, linking each to a specific category.
*   **Simple Reporting**: A dedicated endpoint provides a simple monthly summary, calculating total income, total expenses, and net savings.

## Tech Stack

*   **Backend**: Python, Django
*   **API**: Django Rest Framework
*   **Authentication**: DRF Simple JWT
*   **Database**: SQLite (for development)

---

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing.

### Prerequisites

Make sure you have the following installed on your system:
*   Python (3.8 or newer)
*   `pip` (Python package installer)
*   `git` (for cloning the repository)

### Installation & Setup

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/beabzk/pft-api.git
    cd pft-api
    ```

2.  **Create and activate a virtual environment:**
    *   On macOS/Linux:
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```
    *   On Windows:
        ```sh
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Navigate to the Django project directory:**
    ```sh
    cd pft_project
    ```

5.  **Apply the database migrations:**
    ```sh
    python manage.py migrate
    ```

6.  **Run the development server:**
    ```sh
    python manage.py runserver
    ```

The API should now be running at `http://127.0.0.1:8000/`.

---

## API Endpoints

All protected routes require an `Authorization: Bearer <access_token>` header.

### Authentication

| Method | Endpoint                  | Description                                |
| :----- | :------------------------ | :----------------------------------------- |
| `POST` | `/api/auth/register/`     | Register a new user.                       |
| `POST` | `/api/auth/token/`        | Log in to obtain JWT access/refresh tokens. |
| `POST` | `/api/auth/token/refresh/`| Refresh an expired access token.           |

### Category Management (Protected)

| Method   | Endpoint             | Description                           |
| :------- | :------------------- | :------------------------------------ |
| `GET`    | `/api/categories/`     | Get a list of all user's categories.  |
| `POST`   | `/api/categories/`     | Create a new category.                |
| `GET`    | `/api/categories/{id}/`| Get a single category by ID.          |
| `PUT`    | `/api/categories/{id}/`| Update a category.                    |
| `DELETE` | `/api/categories/{id}/`| Delete a category.                    |

### Transaction Management (Protected)

| Method   | Endpoint               | Description                               |
| :------- | :--------------------- | :---------------------------------------- |
| `GET`    | `/api/transactions/`     | Get all user's transactions (filterable). |
| `POST`   | `/api/transactions/`     | Log a new transaction.                    |
| `GET`    | `/api/transactions/{id}/`| Get a single transaction by ID.           |
| `PUT`    | `/api/transactions/{id}/`| Update a transaction.                     |
| `DELETE` | `/api/transactions/{id}/`| Delete a transaction.                     |

### Reporting (Protected)

| Method | Endpoint                      | Description                                                  |
| :----- | :---------------------------- | :----------------------------------------------------------- |
| `GET`  | `/api/reports/monthly-summary/` | Get a summary of income, expenses, and savings for the current month. |