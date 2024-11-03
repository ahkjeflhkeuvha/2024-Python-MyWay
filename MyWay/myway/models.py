from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # 이메일 필드 추가

class Combination(models.Model):
    user_name = models.CharField(max_length=100)
    menu_name = models.CharField(max_length=100)
    items = models.JSONField()  # JSON 형식으로 여러 아이템을 저장할 수 있는 필드

    def __str__(self):
        return self.menu_name