from django.urls import path

from . import views

urlpatterns = [
    path('',
         views.DiariesList.as_view(),
         name='home'),
    path('diarys',
         views.DiariesList.as_view(),
         name='diarys_list'),
    path('diary/<pk>',
         views.DiaryDetail.as_view(),
         name='diary_details'),
]
