from django.urls import path
from . import views
from . import api_views


urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('car/<int:pk>/', views.car_detail, name='car_detail'),
    path('car/new/', views.car_create, name='car_create'),
    path('car/<int:pk>/edit/', views.car_update, name='car_update'),
    path('car/<int:pk>/delete/', views.car_delete, name='car_delete'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('api/cars/', api_views.CarListCreateView.as_view(), name='car_list_create_api'),
    path('api/cars/<int:pk>/', api_views.CarDetailView.as_view(), name='car_detail_api'),
    path('api/cars/<int:car_pk>/comments/', api_views.CommentListCreateView.as_view(), name='comment_list_create_api'),
]
