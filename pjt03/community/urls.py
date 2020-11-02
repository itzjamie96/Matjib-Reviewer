from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.index, name='index'),
    path('new_review/', views.new_review, name='new_review'),
    path('create_review/', views.create_review, name='create_review'),
    path('review_detail/<int:pk>/', views.review_detail, name='review_detail')

]