from django.shortcuts import render

# Create your views here.
def home(request):
    content={
        'title':"hello"
    }
    return render(request, 'pages/home.html',content)