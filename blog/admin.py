from django.contrib import admin
from .models import Post # models로부터 post class 가지고옴.

admin.site.register(Post) # admin 사이트에서 post를 보기 위해 등록함.
