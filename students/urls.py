from django.urls import path
from .views import StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView

urlpatterns = [
    path('', StudentListView.as_view(), name='student-list'),
    path('create/', StudentCreateView.as_view(), name='student-create'),
    path('<int:pk>/edit/', StudentUpdateView.as_view(), name='student-edit'),
    path('<int:pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),
]
