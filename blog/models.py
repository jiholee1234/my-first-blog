from django.db import models
from django.utils import timezone


class Post(models.Model): # Post 모델 생성.
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) #다른 모델과의 링크를 위해 외래키 생성
    title = models.CharField(max_length=200) # 200자 제한 짧은글.
    text = models.TextField() #글자수 제한없는 긴글.
    created_date = models.DateTimeField( # 날짜 시간 필드의미.
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self): #publish 메서드 생성.
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
