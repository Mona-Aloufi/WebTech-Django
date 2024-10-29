from django.urls import path
from . import views
urlpatterns = [
 path('index2/<int:val1>/', views.index2),
 path('<int:bookId>', views.viewbook),

 path('html5/links', views.links_page, name='books.html5.links'),
 path('html5/text/formatting', views.text_formatting_page, name="text_formatting"),
 path('html5/listing', views.listing_page, name="listing_page"),
 path('html5/tables', views.table_page, name="table_page"),

path('', views.index, name="books.index"),
path('list_books/', views.list_books, name="books.list_books"),
path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
path('aboutus/', views.aboutus, name="books.aboutus"),





]
