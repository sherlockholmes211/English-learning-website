from django.urls import path
from . import views
from .forms import ContactForm
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('about/',views.about,name='ESL-about'),
    path('',views.home,name='ESL-home'),
    path('home2/',views.home2,name='ESL-home2'),
    path('Contact_Us/',views.Contact_Us,name='ESL-Contact_Us'),
    path('practice/',views.prac,name='ESL-practice'),
    path('learning/',views.learning,name='ESL-learning'),
    path('form/',views.contact,name='ESL-form'),
    path('snippet/',views.snippet_detail,name='ESL-form'),
    path('login/',views.login,name='ESL-login'),
    path('signin/', views.loginpage, name='loginpage'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logot, name='logot'),
    path('signup/', views.signup, name='signup'),
    path('exam/', views.exam, name='ESL-exam'),
    path('Vgenre/', views.exam_genre, name='ESL-exam-genre'),
    path('Vexam/', views.Ques, name='ESL-exam-genre-exam'),
    path('audio/', views.audio, name='ESL-audio'),
    path('Agenre/', views.audio_genre, name='ESL-audio-genre'),
    path('Aexam/', views.QuesA, name='ESL-audio-genre-exam'),
    path('Editprof/', views.editprofile, name='ESL-editprofile'),
]
urlpatterns += staticfiles_urlpatterns()
