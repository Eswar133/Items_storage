# Item Storage Project

## Project Overview
This Django project is designed to manage items with functionalities for user authentication, including signup, login, and logout. Users can view a paginated list of items, which can be sorted by different criteria.

## Tech Stack

### Languages and Frameworks
- Python (v3.x)
- Django (v5.0.7)

### Libraries and Tools
- Django 
- Paginator
- User Authentication (Django’s built-in auth system)

### Database
- SQLite (default)
- PostgreSQL (if configured)

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/item_storage.git
   cd item_storage
2. **set Up a Virtual Environment:**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use: env\Scripts\activate
3. **Install Dependencies: Create a requirements.txt file with the following contetn and then run**
   ```bash
   pip install -r requirements.txt
4. **Migrate Database:**
    ```bash
    python manage.py migrate
5. **Run the Development Server**
   ```bash
   python manage.py runserver
6. **Access the Application:Open your browser and go to http://127.0.0.1:8000/**



## API Endpoints
### User Authentication
- signup:Allows users to create an account
   - Request Method:POST
   - Endpoint:/signup/
   - sample Input
     ```json 
     "username": "testuser",
     "password": "mypassword123",
     "email": "test@example.com"
- Login:Allows users to log in.
   - Request Method:POST
   - Endpoint:/login/
   - sample Input
     ```json
     "username": "testuser",
     "password": "mypassword123"
- Logout: Logs the user out.
   - Request Method:POST
   - Endpoint:/logout/
### Item Management
- Get Item List: Retrieves a paginated list of items.
     - Request Method:GET
     - Endpoint:/
     - Query Parameters:
          - sort_by : filed to sort items(default is by name)
          - page : page number for pagination
            


  

    
