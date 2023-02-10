# from django.conf.urls import url
from basic_app import views
from django.urls import path

#Template Tagging
app_name = 'basic_app'   #this is a universal name that django looks for.  the 'basic_app' name is what is in the html file as in <a href="{% url 'basic_app:' %}">The Other Page</a>

urlpatterns = [
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),

]