from django.shortcuts import render
from .models import News

# Create your views here.
def home(request):
    all_news = News.objects.all
    
    
    news_data = {'news_data': all_news}
    return render(request, 'pages/home.html',news_data)

def contact(request):
    return render(request, 'pages/contact.html')

def about(request):
    return render(request, 'pages/about.html')      

def news(request):
    return render(request, 'pages/news.html')

def add_news(request):
    return render(request, 'pages/add_news.html')
