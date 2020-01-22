from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    list_books = ['physics', 'math', 'biology', 'computer']
    context = {
        'list_books': list_books,
        'list_auths': ['a', 'b', 'c'],
        'is_login': True
    }
    return render(request, "index.html",
                  context=context)
