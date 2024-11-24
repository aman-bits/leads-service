### Lead Management Service

This repository contains a Django REST framework-based application for managing leads, activities, and stages in a property management service. The APIs are fully documented using **drf-yasg** to generate API documentation with ReDoc.

---

### **Features**
- **CRUD Operations** for:
  - **Stages** (Lead pipeline stages).
  - **Leads** (Customer information and status tracking).
  - **Lead Activities** (Specific actions related to a lead).
- **Email Notifications** for follow-ups.
- **PostgreSQL Integration** for data persistence.
- **Dockerized Deployment** for easy setup and scaling.

---

### **Project Setup**

#### 1. **Clone the Repository**
```bash
git clone https://github.com/<username>/lead-management.git
cd lead-management
```

#### 2. **Environment Setup**
Create a `.env` file with the following:
```env
POSTGRES_USER=lead_admin
POSTGRES_PASSWORD=strongpassword
POSTGRES_DB=lead_management_db
DB_HOST=db
DB_PORT=5432
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_password
EMAIL_USE_TLS=True
```

#### 3. **Build and Run Docker Containers**
```bash
docker-compose up --build
```

#### 4. **Access the Application**
- **API**: [http://localhost:8000/lead/api/](http://localhost:8000/lead/api/)
- **ReDoc API Documentation**: [http://localhost:8000/lead/docs](http://localhost:8000/lead/docs)

---

### **Endpoints**

#### 1. **Stage Management**
Manage stages in the lead pipeline.

| Method | Endpoint           | Description             |
|--------|--------------------|-------------------------|
| GET    | `/api/stages/`     | List all stages         |
| POST   | `/api/stages/`     | Create a new stage      |
| GET    | `/api/stages/{id}/`| Retrieve a specific stage|
| PUT    | `/api/stages/{id}/`| Update a stage          |
| DELETE | `/api/stages/{id}/`| Delete a stage          |

---

#### 2. **Lead Management**
Manage customer leads.

| Method | Endpoint           | Description                 |
|--------|--------------------|-----------------------------|
| GET    | `/api/leads/`      | List all leads              |
| POST   | `/api/leads/`      | Create a new lead           |
| GET    | `/api/leads/{id}/` | Retrieve a specific lead    |
| PUT    | `/api/leads/{id}/` | Update a lead               |
| DELETE | `/api/leads/{id}/` | Delete a lead               |
| POST   | `/api/leads/{id}/send_email/` | Send email to the lead |

- **Email Example**:
  Sends an email to the lead with their details for follow-up.

---

#### 3. **Lead Activity Management**
Track activities related to leads.

| Method | Endpoint                  | Description                     |
|--------|---------------------------|---------------------------------|
| GET    | `/api/activities/`        | List all lead activities        |
| POST   | `/api/activities/`        | Create a new activity           |
| GET    | `/api/activities/{id}/`   | Retrieve a specific activity    |
| PUT    | `/api/activities/{id}/`   | Update an activity              |
| DELETE | `/api/activities/{id}/`   | Delete an activity              |

---

### **Tech Stack**
- **Backend**: Django REST Framework
- **Database**: PostgreSQL
- **Containerization**: Docker & Docker Compose
- **Documentation**: drf-yasg (ReDoc)

---

### **API Documentation**
Visit [http://localhost:8000/lead/docs/](http://localhost:8000/lead/docs) for interactive API documentation.

---

### **Development Notes**
- Use `docker-compose` for a seamless development environment.
- For local development:
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver
  ```

---

### **Contact**
For any queries or contributions, please contact:
- **Name**: Aman Kumar Srivastav
- **Email**: [2023mt93339@wilp.bits-pilani.ac.in](mailto:2023mt93339@wilp.bits-pilani.ac.in)

---
