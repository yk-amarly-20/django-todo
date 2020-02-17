from django.shortcuts import render, redirect, get_object_or_404
from todo_list.models import Category, Todo
from .forms import AddTodo
from django.contrib import messages

# Create your views here.


def index(request):
    """
    全てのtodoを表示
    """
    todo = Todo.objects.order_by('title')

    return render(request, 'todo/index.html', {'todolist': todo})


def delete(request, id):
    """
    idを指定して、そのtodoを削除

    Parameters
    ----------
    id: int
        todoのid
    """

    todo = get_object_or_404(Todo, pk=id)
    todo.delete()
    messages.success(request, '削除に成功しました')
    return redirect('todo_list:index')


def show_category(request):
    """
    カテゴリの一覧を表示　
    """

    category = Category.objects.all()

    return render(request, 'todo/category.html', {'categories': category})


def todo_category(request, category_name):
    """
    カテゴリを指定して、todoから絞り込み表示

    Parameters
    ----------
    category: string
        カテゴリ
    """

    category = Category.objects.get(title=category_name)
    todo = Todo.objects.filter(category=category).order_by('title')

    return render(request, 'todo/todo_category.html', {'todolist': todo, 'category': category})
    # return render(request, 'todo/todo_category.html', {'todo_list': todo})


def add(request):
    """
    フォームから受け取ったtodoを作成
    """

    form = AddTodo(request.POST or None)
    if form.is_valid():
        todo = Todo()
        title = form.cleaned_data['title']
        dead_line = form.cleaned_data['dead_line']
        categories = form.cleaned_data['category']

        todo = Todo.objects.create(
            title=title,
            dead_line=dead_line,
        )

        for category in categories:
            todo.category.add(category)

        messages.success(request, '追加に成功しました')

        return redirect('todo_list:index')
    return render(request, 'todo/add.html', {'form': form})


def complete(request, id):
    """
    todoが完了した際に褒める

    Parameters
    ----------
    id: int
        完了したtodoのid
    """

    todo = get_object_or_404(Todo, pk=id)
    todo.completed = True
    todo.save()                  # 忘れてた

    messages.success(request, 'todoを達成しました！えらい！！')

    return redirect('todo_list:index')
