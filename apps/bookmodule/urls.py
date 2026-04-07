from django.urls import path
from . import views 

urlpatterns = [  
    path('', views.index, name="books.index"),   
    path('list_books/', views.list_books, name="books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links', views.task1_links),             
    path('html5/formatting', views.task2_formatting),
    path('html5/listing', views.task3_listing),         
    path('html5/tables', views.task4_tables),
    path('search', views.search, name="search"),

]
