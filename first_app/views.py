from django.shortcuts import render , HttpResponse
from .models import Article
# Create your views here.


def first_page(request):
    Article_data = Article.objects.filter(status='p').order_by('created_at')[:4]
    return render(request,'first_app/first_page.html',
                  {'article': Article_data}
                  )
    
def detail(request,slug):
    Article_data = Article.objects.filter(slug=slug)
    return render(request,'first_app/detail.html',{
        "article" : Article_data
    })