from django.urls import path

from . import views

app_name = 'vocab'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('vocab/',views.index,name='index'),
    path('vocab/<int:vocab_id>/', views.detail, name='detail'),
    path('add/', views.addvocab, name='add'),
]

