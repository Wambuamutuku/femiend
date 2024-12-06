
from django.contrib import admin
from django.urls import path
from femiapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('service/', views.service, name='service'),
    path('femicide/', views.femicide, name='femicide'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('story/', views.story, name='story'),
    path('post/', views.post, name='post'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),


    #mpesa integration
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),

]
