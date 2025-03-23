from django.urls import path
from .views import AdminSignupView, AdminLoginView, BookListCreateView, BookRetrieveUpdateDestroyView, StudentView

urlpatterns = [
    path('admin/signup/', AdminSignupView.as_view(), name='admin-signup'),
    path('admin/login/', AdminLoginView.as_view(), name='admin-login'),
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),
    path('student/books/', StudentView.as_view(), name='student-books'),
]
