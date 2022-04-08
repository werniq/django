from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Category
from .forms import NewsForm, UserRegisterForm, UserLoginForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    categories = Category.objects.all()
    return render(request, 'news/register.html', {"form": form,
                                                  "categories": categories})


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    categories = Category.objects.all()
    return render(request, 'news/login.html', {"categories": categories,
                                               "form": form})

def user_logout(request):
    logout(request)
    return redirect('login')


class HomeNews(ListView):
    model = News
    template_name = 'news_list.html'
    context_object_name = 'news'
    categories = Category.objects.all()
    extra_context = {'title': "Главная",
                     'categories': categories}
    paginate_by = 2


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class NewsByCategory(ListView):
    model = News
    template_name = 'news/home_list_news.html'
    context_object_name = 'news'
    categories = Category.objects.all()
    extra_context = {'title': "Главная",
                     'categories': categories}
    allow_empty = False


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context


    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)


class ViewNews(DetailView):
    model = News
    categories = Category.objects.all()
    pk_url_kwarg = 'news_id'
    template_name = 'news/news_detail.html'
    extra_context = {'categories': categories}
    context_object_name = 'news_item'


class CreateNews(CreateView):
    form_class = NewsForm
    categories = Category.objects.all()
    extra_context = {'categories': categories}
    template_name = 'news/add_news.html'

