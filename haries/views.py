from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import Diary


class DiariesList(ListView):
    model = Diary


class DiaryDetail(DetailView):
    model = Diary
