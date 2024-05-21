# TELAVERGE MART

TELAVERGE MART is a full-stack e-commerce website built using Django, HTML, CSS, and JavaScript. This platform features an AI recommendation system that monitors your viewing history and provides personalized product recommendations on the home screen(you must be logged in to get personalized recommendations).

## Live Website Link



## Contents
- [Features](#features)
- [Technologies used](#technologies-used)
- [Deployment](#deployment)
- [Libraries Used](#libraries-used)
- [In-app Video](#in-app-video)
- [In-app Screenshots](#in-app-screenshots)
- [Installation](#installation)


## Features

- **User Authentication**: Sign up, login, and manage your account.
- **Product Listings**: Browse and search for products across various categories.
- **Product Details**: View detailed information and images for each product.
- **AI Recommendations**: Personalized product recommendations based on your browsing history.
- **Enhanced Search**: Search results include recommendations, showing recommended products first.
- **Filter Products**: Filter products based on different parameters such as brands, colors, occasion, etc.
- **Shopping Cart**: Add products to your cart and proceed to checkout.
- **Order Management**: Track your orders and view order history.
- **Admin Panel**: 
  - Django admin plus custom admin panel integrated.
  - Manage products: Add, edit, and delete products.
  - View and manage current orders.
  - View and manage users.
- **Responsive Design**: Optimized for both desktop and mobile devices.


## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **AI**: Machine Learning algorithms for recommendation system
- **Database**: MySQL


## Deployment

- **Website**: The website is deployed on pythonanywhere
- **MySQL DataBase**: MySQL is deployed on aivencloud


## Libraries Used

#### Libraries for Django
- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Django Crispy Forms**: Helps to manage Django forms easily and create beautiful, flexible, and DRY forms.
- **Django Widget Tweaks**: Provides utilities for modifying the form field rendering in templates without writing custom form fields.
- **Django Jazzmin**: Give custom template design to default Django admin panel.
- **Pillow**: A Python Imaging Library (PIL) fork that adds image processing capabilities to your Python interpreter.
- **PyMySQL**: A pure-Python MySQL client library, used for connecting to a MySQL database.

#### Machine Learning Libraries
- **NLTK (Natural Language Toolkit)**: A leading platform for building Python programs to work with human language data, used for text processing.
- **Pandas**: A powerful data manipulation and analysis library for Python, providing data structures like DataFrame.
- **NumPy**: A fundamental package for scientific computing with Python, offering support for arrays and matrices.
- **Scikit-learn**: A machine learning library for Python, used for implementing and evaluating machine learning models.


## In-app Video
- https://github.com/SanchitDang/...mp4


## In-app Screenshots
- Splash Screen
- <img src="" width="200" height="400" />


## Installation

1. **Clone the repository**
    ```bash
    git clone https://github.com/yourusername/telaverge-mart.git
    cd telaverge-mart
    ```

2. **Create a virtual environment**
    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure the MySQL database**

    Update the `DATABASES` setting in `settings.py` with your MySQL configuration:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'your_database_name',
            'USER': 'your_database_user',
            'PASSWORD': 'your_database_password',
            'HOST': 'your_host',
            'PORT': 'port',
        }
    }
    ```

5. **Apply migrations**
    ```bash
    python manage.py migrate
    ```

6. **Create a superuser**
    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server**
    ```bash
    python manage.py runserver
    ```

8. **Visit the site**
    Open your web browser and go to `http://127.0.0.1:8000`
