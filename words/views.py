from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from words.forms import WordForm
from words.models import Word


def index(request):
    """
    Renders the home
    :param request:
    :return:
    """
    if request.user.is_authenticated:
        return redirect('/home')
    return redirect('/login')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        return redirect('/home')
    else:
        return render(request, 'words/login.html')


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect('/login')


@login_required
def home(request):
    return render(request, 'words/home.html')


@login_required
def word(request):
    """
    If the method is GET, we render the add-word view.
    If the method is POST we create a new word.
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, 'words/addword.html')
    elif request.method == "POST":
        form = WordForm(request.POST)

        if form.is_valid():
            model = Word(
                word=form.cleaned_data['word'],
                freeTrans=form.cleaned_data['freeTrans'],
                freeTrans2=form.cleaned_data['freeTrans2'],
                comment=form.cleaned_data['comment'],
                owner_id=1
            )
            model.save()
        return render(request, 'words/addword.html')
    else:
        return HttpResponse(status=409)


@login_required
def my_words(request):
    """
    Renders an overview over my words, with pagination
    :param request:
    :return:
    """
    words_all = Word.objects.filter(owner_id=1)
    paginator = Paginator(words_all, 50)
    page = request.GET.get('page')

    try:
        words = paginator.page(page)
    except PageNotAnInteger:
        words = paginator.page(1)
    except EmptyPage:
        words = paginator.page(paginator.num_pages)

    return render(request, 'words/mywords.html', {'words': words})
