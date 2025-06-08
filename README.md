# Employee Management System with APIs and Visualization

This is a Django-based backend application that provides a fully functional employee management system. It includes database models, REST APIs, token authentication, Swagger documentation, a visualization dashboard, and optional Docker deployment support.

## Features

- Django models for Employees, Departments, Attendance, and Performance
- Token-based authentication using DRF TokenAuth
- RESTful CRUD APIs with pagination, filtering, and sorting
- Swagger UI for API documentation
- Admin panel for data management
- Dashboard with Chart.js visualizations (Employees by Department, Monthly Attendance)
- Management command to seed the database with realistic fake data using Faker
- Dockerfile and docker-compose support
- Unit tests for core API endpoints

## Technologies Used

- Python 3.11
- Django 5
- Django REST Framework
- PostgreSQL
- Chart.js (with Tailwind CSS)
- drf-yasg for Swagger documentation
- Docker & docker-compose
- Faker (for data generation)

## Setup Instructions

### Local Setup

1. Clone this repository.

2. Copy the `.env.example` file to `.env` and configure your local PostgreSQL credentials.

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations and seed the database:

   ```bash
   python manage.py migrate
   python manage.py seed_data
   ```

5. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

Access:

- Admin panel: `http://localhost:8000/admin/`
- Swagger docs: `http://localhost:8000/swagger/`
- Dashboard: `http://localhost:8000/dashboard/`

### Docker Setup

1. Ensure Docker is installed and running.

2. Copy `.env.example` to `.env` and use the following `DB_HOST=db` setting.

3. Start the containers:

   ```bash
   docker-compose up --build
   ```

4. After startup, apply migrations and seed data:

   ```bash
   docker-compose exec web python manage.py migrate
   docker-compose exec web python manage.py seed_data
   docker-compose exec web python manage.py createsuperuser
   ```

Visit the same URLs via `http://localhost:8000/`.

## Deployment on Render

This project has been successfully deployed to Render using Docker.

Live URL (if initialized):

- https://employee-management-system-with-apis-and.onrender.com

> Note: Render’s free tier does not support interactive shell access. Migrations and seed data must be initialized either by:
>
> - Including a startup script in `Dockerfile`, or
> - Executing via shell if using Render Pro plan.

## Environment Variables

Example `.env`:

```env
DB_NAME=glynac_db
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
```

For Docker/Render, use:

```env
DB_HOST=db  # for Docker
DB_HOST=dpg-xxxx.onrender.com  # for Render Internal DB host
```

## API Endpoints

All API endpoints are available under `/api/`. For example:

- `GET /api/employees/`
- `POST /api/attendance/`
- `GET /api/performance/?ordering=-rating`
- `GET /api/employees/?department=HR&ordering=date_joined`

Authentication is required for most endpoints via token-based header:

```
Authorization: Token <your-token>
```

## Testing

Run all tests with:

```bash
python manage.py test
```

---

For inquiries, please contact: carlyiu14@gmail.com
