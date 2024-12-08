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

 path('search', views.search_page, name="search_page"),

path('add-sample-books/', views.add_sample_books, name='add_sample_books'),
path('simple/query', views.simple_query, name="simple_query"),
path('complex/query', views.lookup_query, name="lookup_query"),

path('lab8/task1/', views.list_books_under_50, name='list_books_under_50'),
path('lab8/task2/', views.edition_auther, name='list_books_under_50'),
path('lab8/task3/', views.list_books_not_qu_and_editions, name='list_books_not_qu_and_editions'),
path('lab8/task4/', views.list_books_ordered_by_title, name='list_books_ordered_by_title'),
path('lab8/task5', views.book_aggregations, name='book_aggregations'),

]
