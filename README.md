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
     - sample output
  
      Name: smartwatch, Description: A watch with fitness tracking and notifiction features, Price: 1999.00, Created At: 2024-10-22 15:18:04.274620+00:00
      Name: Bluetooth Speaker, Description: A portable speaker with rich sound and deep bass, Price: 499.00, Created At: 2024-10-22 15:18:27.001584+00:00
      Name: Camera DSLR, Description: High resolution for professional usage and personal usage, Price: 59999.00, Created At: 2024-10-22 15:18:52.372676+00:00
      Name: External hard drive, Description: 2 TB external hard drive for storage and backup files, Price: 999.00, Created At: 2024-10-22 15:19:34.088642+00:00
      Name: Gaming console, Description: Next-gen gaming console with immersive gaming experience, Price: 12999.00, Created At: 2024-10-22 15:20:24.859726+00:00
      Name: TV(smart), Description: 55-inch 4k smart tv with streaming capabilities, Price: 8999.00, Created At: 2024-10-22 15:20:55.079672+00:00
      Name: Tablet, Description: A screen with 9 inches better in gaming for kids and learning content, Price: 30000.00, Created At: 2024-10-22 15:21:54.652200+00:00
            


  

    
