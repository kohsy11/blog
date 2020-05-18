from django.shortcuts import render, redirect
from .models import Article
import datetime
# Create your views here.

def index(request):
    movie = Article.objects.filter(category = 'Movie')
    movie_num = movie.count()
    drama = Article.objects.filter(category = 'Drama')
    drama_num = drama.count()
    ent = Article.objects.filter(category = 'Ent')
    ent_num = ent.count()
    return render(request, 'index.html', {'movie_num' : movie_num, 'drama_num' : drama_num, 'ent_num' : ent_num})

def movie(request):
    movie = Article.objects.filter(category = 'Movie')
    return render(request, 'movie.html', {'movie' : movie})

def drama(request):
    drama = Article.objects.filter(category = 'Drama')
    return render(request, 'drama.html', {'drama' : drama})

def ent(request):
    ent = Article.objects.filter(category = 'Ent')
    return render(request, 'ent.html', {'ent' : ent})

def detail(request, primekey):
    article = Article.objects.get(pk = primekey)
    return render(request, 'detail.html', {'detail' : article})

def new(request):
    now = datetime.datetime.now()
    nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
    if request.method == 'POST':
        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category'],
            date = nowDatetime,
        )
        return redirect('detail', primekey = new_article.pk)
        #new_article.pk = new_article 의 pk
    else:
        return render(request, 'new.html')
   
