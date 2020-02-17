from django.db import models

from django.utils import timezone

# Create your models here.


class Category(models.Model):
    """
  　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　todoのカテゴリ
    """

    title = models.CharField('タイトル', max_length=50)     # カテゴリーのタイトル

    def __str__(self):
        return self.title


class Todo(models.Model):
    """
    TODO作成
    """

    title = models.CharField('タイトル', max_length=50)  # TODOのタイトル
    dead_line = models.DateTimeField('締め切り', default=timezone.now())
    created_at = models.DateTimeField('日付', auto_now_add=True)  # 投稿日時
    category = models.ManyToManyField(Category, blank=True)  # カテゴリとの連携
    completed = models.BooleanField('completed', default=False)

    def __str__(self):
        return self.title
