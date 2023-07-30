from . import views
from django.urls import path
from .views import my_view, get_subcategories



from django.conf.urls.static import static

urlpatterns = [

    path('',views.demo,name='index'),
    path('', my_view, name='my_view'),
    path('my_view',views.my_view, name='my_view'),
    path('get_subcategories/', get_subcategories, name='get_subcategories'),
    path('home', views.home,name='home'),
    path('submit_form/', views.submit_form, name='submit_form')





]