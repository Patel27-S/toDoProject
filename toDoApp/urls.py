from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.mainPage, name='home'),
    path('addTodoItem/',views.toAddItems, name='add_content'),
    path('deleteTodoItem/<int:pk>',views.toDeleteItems, name='delete_content'),
]