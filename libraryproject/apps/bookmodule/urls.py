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
#lab9
path('oneBOOK/<int:bookId>', views.view_one_book_lab9, name="books.view_one_book_lap9"),
path('book_list_lab9', views.book_list_lab9, name="books.book_list_lab9"),
path('lab9_part1/addbook', views.addBookWithoutForms, name='ADDBook'),
path('lab9_part1/editbook/<id>', views.UpdateBookWithoutForms, name='updateBook'),
path('lab9_part1/deletebook/<id>', views.DeleteBOOK, name='DeleteBOOK'),
path('lab9_part2/addbookWForm', views.addBookWForms, name='addbookWForm'),
path('lab9_part2/editbook/<id>', views.updateBookWForms, name='updateBookWForms'),
]
