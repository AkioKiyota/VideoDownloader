from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import input_form
from . import YoutubeModule


def home(request):
    return render(request, 'HomePage.html', {})


def youtube(request):
    if request.method == "POST":
        form = input_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data['data']
            YoutubeModule.get_video(data)

            return render(request, 'YoutubePage.html', {'form': form})
    else:
        form = input_form()

    return render(request, 'YoutubePage.html', {'form': form})


def instagram(request):
    return render(request, 'InstagramPage.html', {})


def twitter(request):
    return render(request, 'TwitterPage.html', {})
