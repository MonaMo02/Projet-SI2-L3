# Inventory management System.

## Introduction:

This web application is a simple Inventory management System
that enbales the user to perform the CRUD operations on all the 
included tables.
The frameworks Django and Bootstrap were used to build this app.

## Requierments:

  - [Python](https://www.python.org/downloads/)
  
  - [Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/download/)

## Usage

### In the case of only downloading the project folder (GestStockMagasin), you need to run the following command is the root of your project:
```
Python  –m  venv  env_name
```
### Once your environment is created, run the following commande to activate it: 
(If you are downloading both folders you can jump straight to this step) 
```
env_name\Scripts\activate
```

### Once your environment is created and activated, run the following commande to install Django:
```
pip install django
```
### Once the install is complete access the application folder (the one you downloaded:GestStockMagasin) then run the follwing commands and you are ready to use our application: 
```
Python  manage.py makemigrations
Python  manage.py migrate
Python  manage.py runserver
```

### In order to use Bootstrap, after downloading you must add the CSS and JS files downloaded into a folder called 'static' in your application folder
then add the following links to your templates: 
```
<!DOCTYPE html> 
  <html lang="en">    
  {% load static %} 
    <head>     
      <!-- link to compiled css file-->
    
      <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
    
    </head> 
    
    <body>     
      <!-- link to compiled js file-->
    
      <script src="{% static 'js/bootstrap.bundle.min.js' %}"></script>
    
    </body>  
    
  </html> 
```


