This repository is about Integrating LTI with Canvas API calls.
Note: you can create virtual environment and install all the necessary dependencies using
pip install -r requirements.txt
Steps to be followed:
1. create a new project
2. Install Django, sslserver : pip install django and pip install django-sslserver
3. Create Django project : django-admin startproject ProjectName
4. Create an App inside your Project : python ./manage.py startapp AppName
5. Now, need to make some changes to the files inside the Project
6. Open settings.py in your project and modify the following things.
   Add this inside INSTALLED_APPS
      'AppName.apps.AppNameConfig','sslserver'
   Comment the following line in MIDDLEWARE
        django.middleware.csrf.CsrfViewMiddleware
   
   PYLTI_CONFIG = {
        'consumers': {
            'consumerKey': {
               'secret': 'secretKey'
            }
        }
      }
7. create a new file named urls.py in your Appname folder and add the following code inside it.
    
    from django.urls import path
    from . import views
    urlpatterns = [
        path('', views.index, name='index'),
    ]
8. Make sure that you have index method inside views.py inside your Appname folder
9. Add the following line in urls.py located inside ProjectName folder
        
    urlpatterns = [
        path('lti/',include('Appname.urls')),
        path('admin/', admin.site.urls),
    ]
10. Finally, to apply all the migration changes that we specified use : python ./manage.py migrate AppName
11. Install canvasAPI using pip install canvasapi
12. Install dotenv using python -m pip install python-dotenv , This is used to load the canvas_api_key 