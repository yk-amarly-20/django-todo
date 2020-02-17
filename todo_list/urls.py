from django.urls import path

from . import views

app_name = 'todo_list'
urlpatterns = [
    path('', views.index, name='index'),  # 　一覧表示
    path('delete/<int:id>', views.delete, name='delete'),
    path('category', views.show_category, name='category'),  # カテゴリから絞りこみ
    path('category/<str:category_name>', views.todo_category,
         name='todo_category'),  # 絞り込んだtodoを表示
    path('add', views.add, name='add'),  # 新規に追加する
    path('complete/<int:id>', views.complete,
         name='complete'),  # 達成した際にフラッシュメッセージ
]
