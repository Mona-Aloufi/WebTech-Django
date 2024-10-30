from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


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