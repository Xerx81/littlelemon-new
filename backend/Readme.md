# Little Lemon Backend (Django REST Framework)

This is the backend for the Little Lemon web application. It is built using Django and Django REST Framework (DRF) and provides RESTful APIs for managing menu items and table bookings.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)

---

## Features

- Exposes APIs to:
  - Fetch menu items.
  - Manage bookings.
- Token-based authentication using Djoser.
- Cross-Origin Resource Sharing (CORS) support for frontend integration.
- Fully customizable and extensible.

---

## Tech Stack

- **Framework:** Django
- **API Framework:** Django REST Framework
- **Authentication:** Djoser
- **Database:** SQLite
- **CORS:** django-cors-headers

---

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.10+
- pip
- virtualenv (optional but recommended)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Xerx81/LittleLemonAPI.git
   cd LittleLemonAPI
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Access the application at:

   ```
   http://127.0.0.1:8000
   ```

## API Endpoints

- /restaurant/menu/items
- /restaurant/menu/items/{id}
- /restaurant/booking
- /restaurant/booking/tables
- /auth
- /auth/users
- /auth/token/login
- /auth/token/logout
