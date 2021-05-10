from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.views.generic import CreateView, ListView


def log_home(request):
    news = Article.objects.order_by('-date')
    return render(request, 'UpdatesLog/log_home.html', {'news': news})


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('log_home')

    form = ArticleForm()

    data = {
        'form': form,
    }

    return render(request, 'UpdatesLog/create.html', data)
