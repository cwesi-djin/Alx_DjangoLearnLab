from django.urls import path
from .views import list_books, LibraryDetailView, list_books
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpattern = [
    path('books/', list_books, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),


    #Athentication URL's
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('admin-panel/', views.admin_view, name='admin_view'),
    path('librarian-panel/', views.librarian_view, name='librarian_view'),
    path('member-panel/', views.member_view, name='member_view'),
]