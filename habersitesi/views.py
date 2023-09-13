from django.shortcuts import render

# Create your views here.
def home(request):
    
    news_data=[{
        'title':"hello",
        'description':"description"
        
    },
    {'title':"hello",
    'description':"description"   
    }
    
    ]
    context = {'news_data': news_data}
    return render(request, 'pages/home.html',context)