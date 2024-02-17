from django.urls import path
from .views import index, get_books, get_category, user_register, user_login, user_logout

app_name = 'book'

urlpatterns = [
    path('', index, name='home'),
    path('detail/<slug:book_slug>/', get_books, name='detail'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]