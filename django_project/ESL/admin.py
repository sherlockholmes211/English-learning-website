from django.contrib import admin
from .models import Snippet,ExamQ,ExamV,TMarks,Dmarks,Profile
# Register your models here.
admin.site.register(Snippet)
admin.site.register(ExamQ)
admin.site.register(ExamV)
admin.site.register(TMarks)
admin.site.register(Dmarks)
admin.site.register(Profile)