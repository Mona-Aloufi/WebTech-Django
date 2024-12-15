from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Book
from django.db.models import Q
from django.db.models import Count, Sum, Avg, Max, Min
from .forms import BookForm


def index(request):
    name = request.GET.get("name") or "world!" 
    return render(request, "bookmodule/index.html" , {"name": name}) 

def index2(request, val1 = 0): #add the view function (index2)
 return HttpResponse("value1 = "+str(val1))

def viewbook(request, bookId):
 # assume that we have the following books somewhere (e.g. database)
 book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
 book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
 book3 = {'id':789, 'title':'programming with laughing', 'author':'Dr. Mona Aloufi'}
 targetBook = None
 if book1['id'] == bookId: targetBook = book1
 if book2['id'] == bookId: targetBook = book2
 if book3['id'] == bookId: targetBook = book3
 context = {'book':targetBook} # book is the variable name accessible by the template
 return render(request, 'bookmodule/show.html', context)


def index(request):
    return render(request, "bookmodule/index.html")

def list_books(request):
    return render(request, 'bookmodule/list_books.html')

def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def links_page(request):
    return render(request, 'bookmodule/links.html')

def text_formatting_page(request):
    return render(request, 'bookmodule/text_formatting.html')

def listing_page(request):
    return render(request, 'bookmodule/listing.html')

def table_page(request):
    return render(request, 'bookmodule/table.html')

def search_page(request):
    if request.method == "POST":
        string = request.POST.get('keyword', '').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        # Filter the books based on search criteria
        books = __getBooksList()
        newBooks = []
        
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower():
                contained = True
            if not contained and isAuthor and string in item['author'].lower():
                contained = True
            if contained:
                newBooks.append(item)
        # Render the filtered list of books
        return render(request, 'bookmodule/bookList.html', {'books': newBooks})
    # Render the search page for GET requests
    return render(request, 'bookmodule/search.html')
def __getBooksList():
 book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
 book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
 book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
 return [book1, book2, book3]

def add_sample_books(request):
    # Add books to the database
    mybook1 = Book(title='Continuous Delivery', author='J. Humble and D. Farley', edition=1)
    mybook1.save()

    mybook2 = Book.objects.create(title='The Phoenix Project', author='Gene Kim', edition=2)
    mybook2.save()
    
    return HttpResponse("Sample books have been added to the database!")



def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def lookup_query(request):
    mybooks=books=Book.objects.filter(author__isnull =
    False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if len(mybooks)>=1:
       return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
       return render(request, 'bookmodule/index.html')



def list_books_under_50(request):
    # Fetch books with price <= 50 using Q
    books = Book.objects.filter(Q(price__lte=50))
    
    # Render the results in a template
    return render(request, 'bookmodule/book_list less than 50.html', {'books': books})


def edition_auther(request):
    # Query for books with editions > 2 and title or author containing 'qu'
    books = Book.objects.filter(
        Q(edition__gt=2) & (Q(title__icontains='qu') | Q(author__icontains='qu'))
    )

    # Render the results in a template
    return render(request, 'bookmodule/book_list_task2.html', {'books': books})
def list_books_not_qu_and_editions(request):
    # Query for books with editions <= 2 and where neither the title nor the author contains 'qu'
    books = Book.objects.filter(
        Q(edition__lte=2) & ~(Q(title__icontains='qu') | Q(author__icontains='qu'))
    )

    # Render the results in a template
    return render(request, 'bookmodule/book_list_task3.html', {'books': books})

def list_books_ordered_by_title(request):
    # Query to get books ordered by title
    books = Book.objects.order_by('title')  # Ascending order
    # For descending order, use '-title'

    # Render the results in a template
    return render(request, 'bookmodule/book_list_task4.html', {'books': books})

def book_aggregations(request):
    # Using aggregation functions to get the required information
    aggregation_data = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        average_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    
    # Passing the aggregated data to the template
    return render(request, 'bookmodule/book_aggregations.html', aggregation_data)


    #lap9 task1
def view_one_book_lab9(request, bookId):
    # Fetch the book with the given ID or return a 404 error if not found
    book = get_object_or_404(Book, id=bookId)
    
    # Render the template with the book object
    return render(request, 'bookmodule/one_BOOKlap9.html', {'book': book})

def book_list_lab9(request):
    # Fetch all books from the database
    books = Book.objects.all()

    # Pass the books to the template context
    return render(request, 'bookmodule/bookList.html', {'books': books})
def addBookWithoutForms(request):
        if request.method=="POST":
            titleval=request.POST.get('title')
            autherval=request.POST.get('author')
            priceval=request.POST.get('price')
            editionval=request.POST.get('edition')
            obj=Book(title=titleval,author=autherval,price=priceval,edition=editionval)
            obj.save()
            return redirect('books.view_one_book_lap9',bookId=obj.id)
        return render(request,"bookmodule/addBook.html")
def UpdateBookWithoutForms(request,id):
    obj = Book.objects.get(id=id)
    if request.method=="POST":
        titleval=request.POST.get('title')
        autherval=request.POST.get('author')
        priceval=request.POST.get('price')
        editionval=request.POST.get('edition')
        obj.title=titleval
        obj.author=autherval
        obj.price=priceval
        obj.edition=editionval
        obj.save()
        return redirect('books.view_one_book_lap9',bookId=obj.id)
    return render(request,"bookmodule/UpdateBook.html",{"obj":obj})

def DeleteBOOK(request,id):
    obj = Book.objects.get(id=id)
    if request.method=='POST':
        obj.delete()
        return redirect("books.book_list_lab9")
    return render(request,"bookmodule/deleteBook.html",{'obj':obj})

#lab9 with DjangoForms
def addBookWForms(request):
    obj = None
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect('books.view_one_book_lap9', bookId=obj.id)
    else:
        form = BookForm()  # Initialize a blank form for GET requests
    
    return render(request, "bookmodule/addBookWForms.html", {'form': form})

def updateBookWForms(request,id):
    obj = Book.objects.get(id=id)
    form = BookForm(instance=obj)
    if request.method == "POST":
        form=BookForm(request.POST, instance=obj)
        if form.is_valid():
            obj.save()
            return redirect('books.view_one_book_lap9', bookId=obj.id)
    else:
        form = BookForm(instance=obj)  # Initialize a blank form for GET requests
    
    return render(request, "bookmodule/UpdateBookWForms.html", {'form': form})
